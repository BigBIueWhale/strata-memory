#!/usr/bin/env python3
"""
Per-unit silicon MANUFACTURING cost model (NRE/masks/design EXCLUDED)
for the 2-die converter ASIC set on TSMC N5:
  ROOT die : 512-lane GDDR7 device-mode PHY (28 Gb/s PAM3) + 9x UCIe-class
             fan-out (~2 TB/s aggregate) + control + small SRAM,
             ~6,000-ball FCBGA (SP5-class body).
  LEAF die : 5x DDR5-5600 full channels (~550 signal pins) + root-facing
             UCIe-class link + scheduling + small SRAM, ~1,500-2,000-ball FCBGA.
  1 system = 1 root + 9 leaves (45 DDR5 channels total).

Every parameter is tagged [S]=sourced (see MANIFEST.md) or [E]=estimate
derived from sourced anchors. Low/central/high (L/C/H) bands throughout.
"""

import math

# ----------------------------------------------------------------------------
# 1. SOURCED ANCHORS (see MANIFEST.md in this directory for files/URLs)
# ----------------------------------------------------------------------------
# [S1] CSET "AI Chips" (2020), appendix table: foundry sale price per 300mm
#      wafer: 5nm $16,988; 7nm $9,346. ATP (assembly/test/pkg) modeled by CSET
#      as 33.48% of foundry price (market average).
# [S2] TrendForce 2024-10-04 (Commercial Times): 2nm wafers "expected to double
#      compared to 4/5nm, may exceed USD 30,000"  -> 4/5nm ~ $15-16k+ in 2024.
# [S3] SemiAnalysis (Sep 2022, free preview): TSMC N5/N4 wafer cost > 2.2x
#      Samsung 8nm.
# [S4] AnandTech 2020-08-25 (TSMC Tech Symposium): N5 D0 ~0.10-0.11 /cm2 at
#      ramp, expected <0.10 next quarter; N7 hit 0.09 three quarters after HVM.
# [S5] NVIDIA RTX Blackwell whitepaper: GB202 = 750 mm2, 92.2B xtors, sixteen
#      32-bit GDDR7 controllers (512-bit), 28 Gbps PAM3, 1.792 TB/s (RTX 5090).
#      AD102 = 608.5 mm2/384-bit (also Locuza/Ryan Smith: 608.44 mm2).
# [S6] Das Sharma et al., arXiv:2510.06513 (UCIe on-package memory):
#      - UCIe-S module: 1.143 mm die-edge x 1.54 mm depth @110um bump pitch,
#        x32 link, doubly-stacked = 2dir x 32 lanes x 32 GT/s = 256 GB/s
#        (=> 128 GB/s per direction per module), 224 GB/s/mm linear,
#        145.44 GB/s/mm2; channel reach 25 mm on std organic package.
#      - LPDDR5 PHY bump map: 5.8 mm (edge) x 1.75 mm (depth) per 128 DQ
#        @ 9.6 GT/s => 26.5 GB/s/mm, 15.1 GB/s/mm2.
#      - HBM4: 8 mm x 2.5 mm per 2048-bit @ 6.4 GT/s.
# [S7] Angstronomics "The Secret of RDNA3": Navi31 MCD = ~37.5 mm2 on N6 =
#      16MB Infinity Cache + 64-bit GDDR6 PHY + InFO_oS fanout (35um pitch).
# [S8] WikiChip (N5): HD SRAM bitcell 0.021 um2 (+~30% assist overhead).
# [S9] Wikipedia Socket SP5: 6,096-contact LGA, package 72 x 75.4 mm
#      (5,428.8 mm2) -- existence/size anchor for a ~6,000-contact package.
# [S10] SemiEngineering "Test Costs Spiking": test historically held to ~2% of
#      total manufacturing cost; rising for complex parts (to several %).
# [S11] SemiEngineering "Can Chiplets Serve Cost-Conscious Apps?" (Fraunhofer
#      Heinig): advanced chiplet-class packages "maybe $10 to $20" today.
# [S12] TrendForce 2023-05-25: ABF substrate market $9.3B (2023) -> $15B
#      (2026); server substrates drive layer count/area/complexity growth.
# [S13] Wikipedia DDR5: 288-pin DIMM, 2 independent subchannels w/ own CA.
# [S14] Wikipedia/JEDEC GDDR7: PAM3, up to 32 Gb/s/pin.

LCH = ['low', 'central', 'high']

WAFER_PRICE = dict(low=15000.0, central=16500.0, high=18000.0)   # [S1][S2][S3]
D0_PER_CM2 = dict(low=0.05, central=0.07, high=0.10)             # [S4]+[E] mature-N5
PARAMETRIC_YIELD = dict(low=0.98, central=0.97, high=0.95)       # [E] systematic/edge/test escapes

WAFER_DIAM_MM = 300.0
EDGE_EXCLUSION_MM = 3.0                                          # [E] standard 3mm EE
SCRIBE_MM = 0.1                                                  # [E] scribe+seal per die edge

# ----------------------------------------------------------------------------
# 2. DIE AREA DERIVATION  (PHY/pad/shoreline-limited by construction)
# ----------------------------------------------------------------------------
# GDDR7 512-lane DEVICE-mode PHY [E, anchored S5/S6/S7]:
#   - lower bound: LPDDR5 bump-map density (45.3 um/DQ @9.6G [S6]) degraded
#     1.5-2x for 28G PAM3 -> ~0.11-0.15 mm2/DQ  => 55-77 mm2 for 512 DQ.
#   - upper bound: GPU-die strip observation: MCD 64-bit G6 PHY ~ one 6.4mm
#     edge x ~1.7mm [S7] (~0.17 mm2/DQ) and GB202 512-bit on 750mm2 [S5]
#     => 87-100 mm2.
GDDR7_PHY = dict(low=55.0, central=75.0, high=100.0)             # mm2
# UCIe-S fan-out on root: worst-case per-leaf 224 GB/s/dir (5ch x 44.8 GB/s)
#   => 2 x32 modules/leaf (2x128=256 GB/s/dir) x 9 leaves = 18 modules
#   x 1.143x1.54 mm = 1.760 mm2 each  [S6]
UCIE_MODULE_MM2 = 1.143 * 1.54
ROOT_UCIE = dict(low=18 * UCIE_MODULE_MM2, central=18 * UCIE_MODULE_MM2,
                 high=27 * UCIE_MODULE_MM2)                      # high adds 50% margin modules
LEAF_UCIE = dict(low=2 * UCIE_MODULE_MM2, central=2 * UCIE_MODULE_MM2,
                 high=3 * UCIE_MODULE_MM2)
# DDR5-5600 PHY per full 72-bit DIMM channel (~110-118 signals) [E, anchored
#   S6 LPDDR5 map (slower pins, but DIMM reach + dual-subchannel CA) and
#   Genoa-IOD-style edge strips]:
DDR5_PHY_PER_CH = dict(low=5.0, central=6.5, high=8.5)           # mm2
# Control logic + NoC + a few MB distributed SRAM (trivial at N5: 1 MiB HD
#   SRAM ~ 8.389e6 b x 0.021 um2 x ~2x macro overhead ~ 0.35-0.5 mm2/MiB [S8])
ROOT_LOGIC = dict(low=8.0, central=10.0, high=15.0)
LEAF_LOGIC = dict(low=3.0, central=4.0, high=5.0)
# pad ring / seal / DFT / PLL overhead multiplier [E]
OVH = dict(low=1.05, central=1.07, high=1.08)

# Bump-field floor: die bump count x pitch^2 (full-area array) [task premise;
#   pitch: UCIe-S std package = 110um [S6]; task band 130-150um; InFO 35um [S7]]
BUMP_PITCH_MM = dict(low=0.130, central=0.140, high=0.150)
ROOT_BUMPS = dict(low=4300, central=5000, high=6000)   # [E] ~2.2k signal + pwr/gnd
LEAF_BUMPS = dict(low=1400, central=1700, high=2000)   # [E] ~750 signal + pwr/gnd

def die_areas(case):
    root_ip = (GDDR7_PHY[case] + ROOT_UCIE[case] + ROOT_LOGIC[case]) * OVH[case]
    leaf_ip = (5 * DDR5_PHY_PER_CH[case] + LEAF_UCIE[case] + LEAF_LOGIC[case]) * OVH[case]
    root_bump = ROOT_BUMPS[case] * BUMP_PITCH_MM[case] ** 2
    leaf_bump = LEAF_BUMPS[case] * BUMP_PITCH_MM[case] ** 2
    root = max(root_ip, root_bump)
    leaf = max(leaf_ip, leaf_bump)
    # high case: root also absorbs strict single-row shoreline closure
    if case == 'high':
        root = max(root, 180.0)
    return root, leaf, root_ip, root_bump, leaf_ip, leaf_bump

# ----------------------------------------------------------------------------
# 3. DIES/WAFER, YIELD, $/GOOD DIE
# ----------------------------------------------------------------------------
def gross_dpw(area_mm2, aspect=1.35):
    """Rectangle die, standard die-per-wafer formula with edge exclusion."""
    w = math.sqrt(area_mm2 * aspect); h = area_mm2 / w
    w += SCRIBE_MM; h += SCRIBE_MM
    eff = w * h
    d = WAFER_DIAM_MM - 2 * EDGE_EXCLUSION_MM
    usable = math.pi * (d / 2) ** 2
    return int(usable / eff - math.pi * d / math.sqrt(2 * eff))

def murphy_yield(area_mm2, d0_cm2):
    ad = (area_mm2 / 100.0) * d0_cm2
    if ad == 0: return 1.0
    return ((1 - math.exp(-ad)) / ad) ** 2

def die_cost(case, area):
    g = gross_dpw(area)
    y = murphy_yield(area, D0_PER_CM2[case]) * PARAMETRIC_YIELD[case]
    good = g * y
    return g, y, good, WAFER_PRICE[case] / good

# ----------------------------------------------------------------------------
# 4. PACKAGE + TEST  ($/unit, recurring only; MODELED [E], anchored S9-S12,
#    and CSET's market-avg ATP=33.48% of silicon as a structural cross-check)
# ----------------------------------------------------------------------------
# Root: ~6,000-ball FCBGA, SP5-class body (72x75mm, ~18-22 build-up layers).
ROOT_SUBSTRATE = dict(low=60.0, central=90.0, high=140.0)
ROOT_ASSEMBLY  = dict(low=15.0, central=25.0, high=40.0)   # FC attach, underfill, lid, balls
# Leaf: ~1,500-2,000-ball FCBGA (~40-50mm body, 10-14 layers).
LEAF_SUBSTRATE = dict(low=12.0, central=20.0, high=32.0)
LEAF_ASSEMBLY  = dict(low=6.0,  central=10.0, high=16.0)
ASSY_YIELD = dict(low=0.995, central=0.99, high=0.98)      # loss applied to die+substrate value

# Test (wafer sort + final test, DFT/loopback for 28G PAM3 + DDR5 BIST) [S10]
ROOT_TEST = dict(low=3.0, central=6.0, high=12.0)
LEAF_TEST = dict(low=1.5, central=3.0, high=5.0)

# ----------------------------------------------------------------------------
# 5. PER-DIE / PER-SYSTEM STEADY-STATE
# ----------------------------------------------------------------------------
def steady_state(case):
    root_a, leaf_a, *_ = die_areas(case)
    rg, ry, rgood, rdie = die_cost(case, root_a)
    lg, ly, lgood, ldie = die_cost(case, leaf_a)
    ay = ASSY_YIELD[case]
    root_pkg = ROOT_SUBSTRATE[case] + ROOT_ASSEMBLY[case]
    leaf_pkg = LEAF_SUBSTRATE[case] + LEAF_ASSEMBLY[case]
    root_unit = (rdie + root_pkg) / ay + ROOT_TEST[case]
    leaf_unit = (ldie + leaf_pkg) / ay + LEAF_TEST[case]
    system = root_unit + 9 * leaf_unit
    return dict(case=case, root_area=root_a, leaf_area=leaf_a,
                root_gross=rg, root_yield=ry, root_good=rgood, root_die=rdie,
                leaf_gross=lg, leaf_yield=ly, leaf_good=lgood, leaf_die=ldie,
                root_pkg=root_pkg, leaf_pkg=leaf_pkg,
                root_test=ROOT_TEST[case], leaf_test=LEAF_TEST[case],
                root_unit=root_unit, leaf_unit=leaf_unit, system=system)

# ----------------------------------------------------------------------------
# 6. VOLUME CURVE (wafer quantization + packaging/test small-lot multipliers)
# ----------------------------------------------------------------------------
PKG_MULT  = {10: 2.5, 100: 1.5, 1000: 1.15, 10000: 1.0}   # [E] small-lot OSAT/substrate unit premium
TEST_MULT = {10: 1.5, 100: 1.2, 1000: 1.05, 10000: 1.0}

def volume_curve(case, lot_min=1):
    s = steady_state(case)
    rows = []
    for n in [10, 100, 1000, 10000]:
        roots_needed, leaves_needed = n, 9 * n
        rw = max(lot_min, math.ceil(roots_needed / s['root_good']))
        lw = max(lot_min, math.ceil(leaves_needed / s['leaf_good']))
        silicon = (rw + lw) * WAFER_PRICE[case] / n
        pkg = (s['root_pkg'] + 9 * s['leaf_pkg']) * PKG_MULT[n] / ASSY_YIELD[case]
        test = (s['root_test'] + 9 * s['leaf_test']) * TEST_MULT[n]
        rows.append((n, rw, lw, silicon, pkg, test, silicon + pkg + test))
    return s, rows

def combined_reticle(case):
    """1 root + 9 leaves per 26x33mm reticle field: matched sets, 1 mask set."""
    s = steady_state(case)
    field = 26.0 * 33.0
    g = gross_dpw(field, aspect=33.0 / 26.0)
    good_roots = g * murphy_yield(s['root_area'], D0_PER_CM2[case]) * PARAMETRIC_YIELD[case]
    good_leaves = 9 * g * murphy_yield(s['leaf_area'], D0_PER_CM2[case]) * PARAMETRIC_YIELD[case]
    systems = min(good_roots, good_leaves / 9)
    return g, systems, WAFER_PRICE[case] / systems

# ----------------------------------------------------------------------------
if __name__ == '__main__':
    print('=' * 100)
    print('A. DIE AREAS (mm2): max(IP sum, bump field); root-high also covers strict shoreline closure')
    for c in LCH:
        ra, la, rip, rb, lip, lb = die_areas(c)
        print(f'  {c:8s} ROOT: IP={rip:6.1f}  bump-floor={rb:6.1f}  -> {ra:6.1f} | '
              f'LEAF: IP={lip:5.1f}  bump-floor={lb:5.1f}  -> {la:5.1f}')
    print()
    print('B. WAFER ECONOMICS PER DIE  (300mm N5, 3mm edge excl., Murphy yield x parametric)')
    hdr = f'  {"case":8s} {"die":5s} {"area":>6s} {"gross/waf":>9s} {"yield":>6s} {"good/waf":>8s} {"$/good die":>10s}'
    print(hdr)
    for c in LCH:
        s = steady_state(c)
        print(f'  {c:8s} ROOT  {s["root_area"]:6.1f} {s["root_gross"]:9d} {s["root_yield"]:6.1%} '
              f'{s["root_good"]:8.0f} {s["root_die"]:10.2f}')
        print(f'  {"":8s} LEAF  {s["leaf_area"]:6.1f} {s["leaf_gross"]:9d} {s["leaf_yield"]:6.1%} '
              f'{s["leaf_good"]:8.0f} {s["leaf_die"]:10.2f}')
    print()
    print('C. STEADY-STATE PER-UNIT (silicon + package + test, assembly-yield adjusted)')
    for c in LCH:
        s = steady_state(c)
        print(f'  {c:8s} ROOT: die {s["root_die"]:6.2f} + pkg {s["root_pkg"]:6.1f} + test {s["root_test"]:5.1f}'
              f'  => {s["root_unit"]:7.2f}   | LEAF: die {s["leaf_die"]:5.2f} + pkg {s["leaf_pkg"]:5.1f}'
              f' + test {s["leaf_test"]:4.1f} => {s["leaf_unit"]:6.2f}')
        print(f'  {"":8s} SYSTEM (1 root + 9 leaves) = {s["system"]:8.2f} USD')
    print()
    print('D. GB202 MODEL VALIDATION: 750mm2 [S5] on same wafer/yield model (central):')
    g = gross_dpw(750.0, aspect=30.9/24.3)
    y = murphy_yield(750, 0.07)
    print(f'   gross/wafer={g}, defect yield={y:.1%}, $/good die={16500/(g*y):,.0f} '
          f'(street estimates ~$300-400 -> model sane)')
    print()
    print('E. VOLUME CURVE (central case). Wafer-quantized; pkg/test small-lot multipliers.')
    s, rows = volume_curve('central', lot_min=1)
    print(f'   systems per ROOT wafer = {s["root_good"]:.0f};  systems per LEAF wafer = {s["leaf_good"]/9:.1f}'
          f'  (leaf wafers per root wafer for balance = {s["root_good"]/(s["leaf_good"]/9):.2f})')
    print(f'   {"systems":>8s} {"rootWfr":>7s} {"leafWfr":>7s} {"silicon/sys":>11s} {"pkg/sys":>8s} {"test/sys":>8s} {"TOTAL/sys":>9s}')
    for n, rw, lw, sil, pkg, tst, tot in rows:
        print(f'   {n:8d} {rw:7d} {lw:7d} {sil:11.2f} {pkg:8.2f} {tst:8.2f} {tot:9.2f}')
    floor = s['system']
    print(f'   {"infinity":>8s} {"-":>7s} {"-":>7s} {s["root_die"]+9*s["leaf_die"]:11.2f} '
          f'{(s["root_pkg"]+9*s["leaf_pkg"])/ASSY_YIELD["central"]:8.2f} '
          f'{s["root_test"]+9*s["leaf_test"]:8.2f} {floor:9.2f}')
    print()
    print('   Same, if foundry enforces a 25-wafer minimum production lot per die type:')
    s25, rows25 = volume_curve('central', lot_min=25)
    for n, rw, lw, sil, pkg, tst, tot in rows25:
        print(f'   {n:8d} {rw:7d} {lw:7d} {sil:11,.2f} {pkg:8.2f} {tst:8.2f} {tot:9,.2f}')
    print()
    g, sys_w, cost = combined_reticle('central')
    print(f'F. COMBINED-RETICLE OPTION (1 root + 9 leaves per 26x33mm field, one mask set/stream):')
    print(f'   fields/wafer={g}, matched systems/wafer={sys_w:.0f}, silicon $/system={cost:,.0f} '
          f'(vs {s["root_die"]+9*s["leaf_die"]:.0f} separate-wafer floor) -> use for <~400-system runs')
    print()
    print('G. L/C/H SYSTEM SUMMARY (steady-state floor):')
    for c in LCH:
        st = steady_state(c)
        sil = st['root_die'] + 9 * st['leaf_die']
        pkg = (st['root_pkg'] + 9 * st['leaf_pkg']) / ASSY_YIELD[c]
        tst = st['root_test'] + 9 * st['leaf_test']
        print(f'   {c:8s} silicon {sil:7.2f} + packages {pkg:7.2f} + test {tst:6.2f} = {st["system"]:8.2f} $/system')
