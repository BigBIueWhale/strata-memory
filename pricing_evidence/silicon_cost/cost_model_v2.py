#!/usr/bin/env python3
"""
Per-unit silicon MANUFACTURING cost model, v2 (NRE/masks/design EXCLUDED)
for the 2-die converter ASIC set on TSMC N5:
  ROOT die : 512-lane GDDR7 device-mode PHY (28 Gb/s PAM3) + 9x UCIe-class
             fan-out, ~125 mm2, ~6,000-ball FCBGA (SP5-class 72x75 mm body).
  LEAF die : 5x DDR5-5600 channels + root-facing UCIe-class link, ~43 mm2,
             ~1,500-2,000-ball FCBGA (~42x42 mm body).
  1 system = 1 root + 9 leaves. Deterministic / high-reliability part class
  (silent-data-corruption-sensitive), so screening is sized to the server/
  hyperscaler flow, not the consumer flow.

v2 REFINES v1 (cost_model.py) in the two soft spots flagged by review:
  * TEST/SCREENING: explicit wafer sort + at-speed final test + burn-in +
    SLT + interface-hardware amortization + test-yield scrap (v1: flat $6/$3).
  * SUBSTRATE: server/AI-class ABF pricing (v1 used chiplet-class $90/$20).
Die-area and raw-silicon economics are carried over from v1 unchanged
(they were reviewed as sound).

Every parameter is tagged [S#]=sourced (see MANIFEST.md v2 section) or
[E]=estimate derived from sourced anchors. Low/central/high bands throughout.
Low = efficient/optimistic, Central = conservative-realistic (the number to
quote), High = things-go-badly bound.
"""

import math

LCH = ['low', 'central', 'high']

# ----------------------------------------------------------------------------
# 1. SILICON (carried over from v1 -- [S1..S8]; unchanged)
# ----------------------------------------------------------------------------
WAFER_PRICE = dict(low=15000.0, central=16500.0, high=18000.0)   # [S1][S2][S3]
D0_PER_CM2 = dict(low=0.05, central=0.07, high=0.10)             # [S4]+[E]
PARAMETRIC_YIELD = dict(low=0.98, central=0.97, high=0.95)       # [E]
WAFER_DIAM_MM, EDGE_EXCLUSION_MM, SCRIBE_MM = 300.0, 3.0, 0.1

ROOT_AREA = dict(low=99.4, central=124.9, high=180.0)            # [v1 sect. A]
LEAF_AREA = dict(low=33.1, central=42.8, high=57.0)              # [v1 sect. A]

# Wafer finishing: bump (C4) + backgrind + dice + optical inspect, $/wafer [E]
WAFER_FINISH = dict(low=150.0, central=250.0, high=400.0)

def gross_dpw(area_mm2, aspect=1.35):
    w = math.sqrt(area_mm2 * aspect); h = area_mm2 / w
    w += SCRIBE_MM; h += SCRIBE_MM
    d = WAFER_DIAM_MM - 2 * EDGE_EXCLUSION_MM
    usable = math.pi * (d / 2) ** 2
    return int(usable / (w * h) - math.pi * d / math.sqrt(2 * w * h))

def murphy_yield(area_mm2, d0_cm2):
    ad = (area_mm2 / 100.0) * d0_cm2
    return 1.0 if ad == 0 else ((1 - math.exp(-ad)) / ad) ** 2

def die_econ(case, area):
    g = gross_dpw(area)
    y = murphy_yield(area, D0_PER_CM2[case]) * PARAMETRIC_YIELD[case]
    good = g * y
    die = WAFER_PRICE[case] / good + WAFER_FINISH[case] / good
    return g, y, good, die

# ----------------------------------------------------------------------------
# 2. SUBSTRATE, v2  (server/AI-class ABF; replaces v1's chiplet-class anchor)
# ----------------------------------------------------------------------------
# Method: body area x build-up layer count x $/(cm2*layer), calibrated so the
# LOW end reproduces the Fraunhofer "advanced chiplet package $10-20" class
# [S11] (~10-15 cm2, 10-12L -> $0.06-0.16 /cm2*layer at OSAT sell-through),
# with CENTRAL/HIGH carrying the server/AI premium: server ABF substrates are
# the layer-count/area/complexity drivers of the $9.3B->$15B ABF market
# [S12][S27], supply remains tight with 2025-26 price increases on T-glass/BT
# and "medium- to long-term price increases" expected for high-end ABF [S28].
# Root body = SP5 class 72x75.4 mm = 54.3 cm2 [S9], 20 build-up-layer class
# (server CPU class [S12][S27]); leaf 42x42 mm = 17.6 cm2, 12L class.
ROOT_SUB_AREA_CM2 = dict(low=48.0, central=54.3, high=58.0)      # [S9]+[E]
ROOT_SUB_LAYERS   = dict(low=18,   central=20,   high=22)        # [S12][S27]+[E]
LEAF_SUB_AREA_CM2 = dict(low=15.2, central=17.6, high=20.3)      # [E] 39-45 mm sq
LEAF_SUB_LAYERS   = dict(low=10,   central=12,   high=14)        # [E]
USD_PER_CM2LAYER  = dict(low=0.11, central=0.138, high=0.18)     # [S11][S12][S27][S28]+[E]

def substrate_cost(case, root):
    a = (ROOT_SUB_AREA_CM2 if root else LEAF_SUB_AREA_CM2)[case]
    l = (ROOT_SUB_LAYERS if root else LEAF_SUB_LAYERS)[case]
    return a * l * USD_PER_CM2LAYER[case]
# Central: root 54.3*20*0.138 = $149.9 ; leaf 17.6*12*0.138 = $29.1
# (v1: $90 / $20 -- the "too low for server/AI ABF" soft spot.)

# ----------------------------------------------------------------------------
# 3. ASSEMBLY, v2  (flip-chip attach, underfill, lid/IHS, ball attach, OSAT)
# ----------------------------------------------------------------------------
ROOT_ASSY = dict(low=22.0, central=35.0, high=55.0)   # [E anchored S10..S12]
LEAF_ASSY = dict(low=8.0,  central=12.0, high=20.0)
ASSY_YIELD_ROOT = dict(low=0.995, central=0.99, high=0.98)   # [E] 6k-bump FC
ASSY_YIELD_LEAF = dict(low=0.997, central=0.995, high=0.99)

# ----------------------------------------------------------------------------
# 4. TEST + SCREENING, v2  (the big refinement)
# ----------------------------------------------------------------------------
# 4a. ATE cell hourly rate, built up from sourced capital anchors:
#     - High-perf ASIC/MPU tester = base $250-400k + $2,700-6,000/pin at 512
#       pins => $1.6M-$3.5M capital class [S16]; modern HPC/AI configs with
#       HSIO serial instruments (UltraPHY 112/224G [S23]; Pin Scale Multilevel
#       Serial [S24]) sit at/above the top of that class [E].
#     - Tester depreciation "typically 5 or 6 years", and depreciation is
#       "less than half the cost to operate a complete test cell" [S15]
#       => cell $/h = capital/(depr_years*hours*util) x cell-overhead(>=2.0).
HI_TESTER_CAPITAL  = dict(low=2.0e6, central=3.0e6, high=5.0e6)  # [S16][S23][S24]+[E]
MID_TESTER_CAPITAL = dict(low=1.0e6, central=1.5e6, high=2.5e6)  # [S16]+[E]
DEPR_YEARS   = dict(low=6.0, central=5.0, high=5.0)              # [S15]
UTIL_HOURS   = dict(low=7500.0, central=7000.0, high=6500.0)     # [E] 74-86%
CELL_OVERHEAD = dict(low=2.0, central=2.2, high=2.5)             # [S15]

def cell_rate_per_s(case, capital):
    hourly = capital[case] / DEPR_YEARS[case] / UTIL_HOURS[case] * CELL_OVERHEAD[case]
    return hourly / 3600.0
# central: high-end cell $188.6/h = $0.0524/s ; mid cell $94.3/h = $0.0262/s
# (industry folklore "a few cents per test-second" [S15][S16] -- reproduced.)

# 4b. Insertion times and site counts [E, anchored]:
#     - Server-class parts get "longer test patterns at both wafer probe and
#       package test" and 100% SLT of 40-60 min [S17]; SLT runs minutes to
#       >1 hour vs tens of seconds on ATE [S18].
#     - SOC parallelism 2-16 sites typical [S15]; a ~6,000-ball 28G root is
#       pin/power-limited to ~2 sites at sort, 1 at FT [E from S15 socket
#       bandwidth limits: ">20 GHz for high-ball-count sockets is difficult"].
#     - 512-lane at-speed front: full-lane coverage via on-die loopback/BIST
#       (DRAM-side GDDR7 is tested on 36 Gbps PAM3-class memory ATE [S22];
#       device-side loopback + sampled true-at-speed lanes on HSIO cards
#       [S23][S24] is the economic flow [S15 multi-die trend]).
SORT_S  = dict(root=dict(low=90.0,  central=150.0, high=300.0),   # [S17]+[E]
               leaf=dict(low=45.0,  central=75.0,  high=120.0))
FT_S    = dict(root=dict(low=180.0, central=300.0, high=600.0),   # [S17]+[E]
               leaf=dict(low=90.0,  central=150.0, high=240.0))
SORT_SITES = dict(root=2, leaf=4)                                 # [S15]+[E]
FT_SITES   = dict(root=1, leaf=2)                                 # [S15]+[E]

# 4c. Burn-in (production screen, packaged parts): 24-48 h typical, longer
#     per quality target [S20]; HPC/data-center parts are putting burn-in
#     BACK into the production flow (Advantest, 2025) [S19]; enterprise
#     mission-critical flows run 100% burn-in [S26]; test-during-burn-in
#     systems run 48 boards in parallel [S25].
BURNIN_H = dict(low=12.0, central=24.0, high=48.0)                # [S20]
BURNIN_SYS_CAPITAL = dict(low=1.0e6, central=1.5e6, high=2.5e6)   # [S25][S26]+[E]
BURNIN_SLOTS = dict(root=500, leaf=1200)                          # [E] board area
BURNIN_W = dict(root=60.0, leaf=15.0)                             # [E] stress power
KWH_USD = 0.15                                                    # [E]

def burnin_cost(case, die):
    slot_h = (BURNIN_SYS_CAPITAL[case] * 2.0 / 5.0 / 8760.0 / 0.85) / BURNIN_SLOTS[die]
    energy = BURNIN_W[die] * BURNIN_H[case] / 1000.0 * KWH_USD
    return slot_h * BURNIN_H[case] + energy

# 4d. SLT: massively-parallel asynchronous sites; cost dominated by
#     device-specific fixture hardware, not the cell [S15][S18].
SLT_MIN = dict(root=dict(low=15.0, central=30.0, high=60.0),      # [S17][S18]
               leaf=dict(low=10.0, central=20.0, high=40.0))
SLT_SITE_CAPITAL = dict(low=5.0e3, central=8.0e3, high=15.0e3)    # [E]

def slt_cost(case, die):
    rate = SLT_SITE_CAPITAL[case] * 2.0 / 5.0 / 8760.0 / 0.8      # $/site-h
    return rate * SLT_MIN[die][case] / 60.0

# 4e. Interface / consumable hardware (probe cards, FT loadboards+sockets,
#     SLT boards, burn-in boards). "Since 2015 consumables are the leading
#     capital expenditure relative to test" for large SOC [S15]; advanced
#     probe cards run up to ~$500k [S21]; 6,000-ball >20GHz sockets are at
#     the engineering limit [S15]. Fixed set F amortizes over the PROGRAM
#     part count (dominant at low/mid volume) + a wear-replacement floor.
IFACE_F = dict(root=dict(low=4.0e5, central=6.0e5, high=9.0e5),   # [S15][S21]+[E]
               leaf=dict(low=1.8e5, central=2.8e5, high=4.5e5))
IFACE_F_MIN = dict(root=4.0e5, leaf=2.0e5)     # [E] min viable set, tiny runs
IFACE_WEAR = dict(root=dict(low=2.0, central=3.0, high=6.0),      # [E] $/part
                  leaf=dict(low=0.35, central=0.5, high=1.0))
# amortization shares across insertions (sort/FT/BI/SLT) [E]
IFACE_SHARE = dict(sort=0.50, ft=0.22, burnin=0.13, slt=0.15)

# 4f. Package-stage test yields (scrap: a part failing FT/burn-in/SLT is lost
#     WITH its substrate+assembly value) [E; "KGD does not mean 100% pass"
#     S15; SDC-class escapes exist even after all screens S17].
FT_YIELD  = dict(root=dict(low=0.985, central=0.97, high=0.94),
                 leaf=dict(low=0.99,  central=0.98, high=0.96))
BI_YIELD  = dict(root=dict(low=0.997, central=0.993, high=0.985),
                 leaf=dict(low=0.997, central=0.995, high=0.99))
SLT_YIELD = dict(root=dict(low=0.995, central=0.99, high=0.98),
                 leaf=dict(low=0.9975, central=0.995, high=0.99))

# 4g. Outgoing QA / per-lot monitors (sample retest, SPC, periodic
#     reliability monitors; ESD/qual boards excluded as NRE) [E]
QA_FLOOR = dict(root=0.5, leaf=0.25)
QA_FRAC = 0.015

# ----------------------------------------------------------------------------
# 5. PER-UNIT ASSEMBLY-AND-TEST STAGING (value-at-stage scrap accounting)
# ----------------------------------------------------------------------------
def unit_cost(case, die, n_parts_program):
    """Full staged per-part cost. die in {'root','leaf'}."""
    root = (die == 'root')
    area = (ROOT_AREA if root else LEAF_AREA)[case]
    g, y, good, die_cost = die_econ(case, area)
    hi = cell_rate_per_s(case, HI_TESTER_CAPITAL)
    mid = cell_rate_per_s(case, MID_TESTER_CAPITAL)
    rate = hi if root else mid

    iface_total = min(IFACE_F[die][case], max(IFACE_F_MIN[die],
                      IFACE_F[die][case])) / n_parts_program + IFACE_WEAR[die][case]
    if n_parts_program <= 1000:   # tiny runs: min viable set only
        iface_total = IFACE_F_MIN[die] / n_parts_program + IFACE_WEAR[die][case]

    # -- wafer sort (KGD-grade): every gross die probed; good dies pay for all
    sort = (SORT_S[die][case] / SORT_SITES[die]) * rate * (g / good)
    sort_if = iface_total * IFACE_SHARE['sort']

    # -- packaging
    sub = substrate_cost(case, root)
    assy = (ROOT_ASSY if root else LEAF_ASSY)[case]
    ay = (ASSY_YIELD_ROOT if root else ASSY_YIELD_LEAF)[case]
    packaged = (die_cost + sort + sort_if + sub + assy) / ay

    # -- final test (at-speed)
    ft = (FT_S[die][case] / FT_SITES[die]) * rate
    ft_if = iface_total * IFACE_SHARE['ft']
    after_ft = (packaged + ft + ft_if) / FT_YIELD[die][case]

    # -- burn-in
    bi = burnin_cost(case, die)
    bi_if = iface_total * IFACE_SHARE['burnin']
    after_bi = (after_ft + bi + bi_if) / BI_YIELD[die][case]

    # -- SLT
    slt = slt_cost(case, die)
    slt_if = iface_total * IFACE_SHARE['slt']
    after_slt = (after_bi + slt + slt_if) / SLT_YIELD[die][case]

    # -- outgoing QA / monitors
    test_spend = sort + ft + bi + slt + iface_total
    qa = QA_FLOOR[die] + QA_FRAC * test_spend
    total = after_slt + qa

    return dict(case=case, die=die, area=area, gross=g, wafer_yield=y,
                good=good, die_cost=die_cost, sub=sub, assy=assy, ay=ay,
                sort=sort, ft=ft, bi=bi, slt=slt, iface=iface_total, qa=qa,
                test_spend=test_spend + qa,
                packaged=packaged, total=total,
                scrap=total - (die_cost + sub + assy + test_spend + qa))

def system_cost(case, n_systems):
    r = unit_cost(case, 'root', n_systems)
    l = unit_cost(case, 'leaf', 9 * n_systems)
    return r, l, r['total'] + 9 * l['total']

# ----------------------------------------------------------------------------
# 6. VOLUME CURVE (wafer quantization + small-lot pkg/test multipliers + the
#    explicit interface-set amortization above)
# ----------------------------------------------------------------------------
PKG_MULT  = {10: 2.0, 100: 1.4, 1000: 1.1, 10000: 1.0, 50000: 0.97}  # [E]
TEST_MULT = {10: 1.5, 100: 1.25, 1000: 1.1, 10000: 1.0, 50000: 0.97} # [E]

def volume_row(case, n):
    r = unit_cost(case, 'root', n)
    l = unit_cost(case, 'leaf', 9 * n)
    rw = max(1, math.ceil(n / r['good']))
    lw = max(1, math.ceil(9 * n / l['good']))
    silicon = (rw + lw) * (WAFER_PRICE[case] + WAFER_FINISH[case]) / n
    pm, tm = PKG_MULT[n], TEST_MULT[n]

    def staged(u, root, pkg_mult, test_mult):
        ay = u['ay']
        pk = (u['sub'] + u['assy']) * pkg_mult
        pre = u['die_cost'] + (u['sort'] + u['iface'] * IFACE_SHARE['sort']) * test_mult
        packaged = (pre + pk) / ay
        a = (packaged + (u['ft'] + u['iface'] * IFACE_SHARE['ft']) * test_mult) / FT_YIELD[u['die']][case]
        b = (a + (u['bi'] + u['iface'] * IFACE_SHARE['burnin']) * test_mult) / BI_YIELD[u['die']][case]
        c = (b + (u['slt'] + u['iface'] * IFACE_SHARE['slt']) * test_mult) / SLT_YIELD[u['die']][case]
        return c + u['qa'] * test_mult

    root_t = staged(r, True, pm, tm)
    leaf_t = staged(l, False, pm, tm)
    # replace per-unit die cost with wafer-quantized silicon
    per_sys = root_t + 9 * leaf_t - (r['die_cost'] + 9 * l['die_cost']) + silicon
    return n, rw, lw, silicon, root_t, leaf_t, per_sys

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    W = 104
    print('=' * W)
    print('COST MODEL v2 -- recurring per-unit manufacturing only (NRE/masks/design excluded).')
    print('Refines v1: server/AI-class substrate + full test/screening stack. Silicon side unchanged from v1.')
    print('=' * W)

    print('\nA. SUBSTRATE (v2): body-area x layers x $/(cm2*layer)  [S9,S11,S12,S27,S28]')
    for c in LCH:
        rs, ls = substrate_cost(c, True), substrate_cost(c, False)
        print(f'  {c:8s} ROOT {ROOT_SUB_AREA_CM2[c]:5.1f}cm2 x {ROOT_SUB_LAYERS[c]:2d}L x '
              f'{USD_PER_CM2LAYER[c]:.3f} = {rs:6.1f} | LEAF {LEAF_SUB_AREA_CM2[c]:5.1f}cm2 x '
              f'{LEAF_SUB_LAYERS[c]:2d}L = {ls:5.1f}   (v1: 90.0 / 20.0)')

    print('\nB. ATE CELL RATES from capital anchors [S15,S16,S23,S24]')
    for c in LCH:
        hi, mid = cell_rate_per_s(c, HI_TESTER_CAPITAL), cell_rate_per_s(c, MID_TESTER_CAPITAL)
        print(f'  {c:8s} high-end cell ${hi*3600:6.1f}/h = ${hi:.4f}/s | mid cell ${mid*3600:6.1f}/h = ${mid:.4f}/s')

    print('\nC. TEST + SCREENING per part, central case, 10k-system program (per-insertion):')
    for die in ['root', 'leaf']:
        u = unit_cost('central', die, 10000 if die == 'root' else 90000)
        print(f'  {die.upper():4s}: sort {u["sort"]:6.2f} + FT {u["ft"]:6.2f} + burn-in {u["bi"]:5.2f}'
              f' + SLT {u["slt"]:5.2f} + interface {u["iface"]:6.2f} + QA {u["qa"]:4.2f}'
              f'  = {u["test_spend"]:7.2f}   (v1: {6.0 if die=="root" else 3.0:.1f})')

    print('\nD. PER-UNIT STEADY STATE (10k-system program; value-at-stage scrap accounting):')
    for c in LCH:
        r, l, s = system_cost(c, 10000)
        print(f'  {c:8s} ROOT die {r["die_cost"]:6.2f} sub {r["sub"]:6.1f} assy {r["assy"]:5.1f} '
              f'test {r["test_spend"]:6.1f} scrap {r["scrap"]:5.1f} => {r["total"]:7.2f}')
        print(f'  {"":8s} LEAF die {l["die_cost"]:6.2f} sub {l["sub"]:6.1f} assy {l["assy"]:5.1f} '
              f'test {l["test_spend"]:6.1f} scrap {l["scrap"]:5.1f} => {l["total"]:7.2f}')
        print(f'  {"":8s} SYSTEM (1 root + 9 leaves) = {s:8.2f} USD')

    print('\nE. SYSTEM SPLIT, central @10k systems:')
    r, l, s = system_cost('central', 10000)
    sil = r['die_cost'] + 9 * l['die_cost']
    sub = r['sub'] + 9 * l['sub']
    asy = r['assy'] + 9 * l['assy']
    tst = r['test_spend'] + 9 * l['test_spend']
    scr = s - sil - sub - asy - tst
    for name, v in [('raw silicon (incl. sort-input & finishing)', sil),
                    ('substrates', sub), ('assembly', asy),
                    ('test+screening spend', tst),
                    ('yield scrap (assy+FT+BI+SLT losses)', scr)]:
        print(f'   {name:42s} {v:8.2f}  ({v/s:5.1%})')
    print(f'   {"TOTAL":42s} {s:8.2f}')

    print('\nF. VOLUME CURVE (central; program-size amortization + wafer quantization):')
    print(f'   {"systems":>8s} {"rootWfr":>7s} {"leafWfr":>7s} {"silicon/sys":>11s} {"root$":>9s} {"leaf$":>8s} {"TOTAL/sys":>10s}')
    for n in [10, 100, 1000, 10000, 50000]:
        n_, rw, lw, sil, rt, lt, tot = volume_row('central', n)
        print(f'   {n_:8d} {rw:7d} {lw:7d} {sil:11.2f} {rt:9.2f} {lt:8.2f} {tot:10.2f}')
    r_inf = unit_cost('central', 'root', 10**9)
    l_inf = unit_cost('central', 'leaf', 10**9)
    print(f'   {"infinity":>8s} {"-":>7s} {"-":>7s} {"":11s} {r_inf["total"]:9.2f} {l_inf["total"]:8.2f} '
          f'{r_inf["total"] + 9*l_inf["total"]:10.2f}   (interface at wear-replacement floor)')

    print('\nG. BEFORE -> AFTER vs v1 (central, at-volume):')
    print('   v1 system $571.98 = silicon 148.59 + packages 388.89 + test 33.00')
    r, l, s = system_cost('central', 10000)
    print(f'   v2 system {s:7.2f} = see split above.')
    print('   Movers: substrate 90->150 root, 20->29 leaf (server/AI ABF class [S12,S27,S28]);')
    print('   test 6->~x15 root (sort+at-speed FT+burn-in+SLT+interface [S15-S26]);')
    print('   + explicit package-stage test-yield scrap (v1 had none beyond assembly yield).')
