# Silicon manufacturing-cost evidence manifest

Scope: per-unit recurring silicon manufacturing cost (NRE/masks/design excluded) for the
converter ASIC set — 1 root die (512-lane GDDR7 device-mode front + 9-way UCIe-class fan-out)
+ 9 leaf dies (5x DDR5-5600 channels each) per system, TSMC N5.
All files fetched 2026-07-19 (curl, browser UA). Full working archive (including
non-load-bearing fetches) at /tmp/strata_silicon_cost/evidence/.
Model: `cost_model.py` (all parameters tagged [S]=sourced / [E]=estimate); output:
`cost_model_output.txt`.

| File | Load-bearing claim (exact figure) | Source URL |
|---|---|---|
| cset_ai_chips_2020_wafer_prices.pdf | Foundry sale price per 300mm wafer: 5nm = $16,988, 7nm = $9,346 (2020 model, appendix table rows "Foundry sale price per wafer"); ATP (assembly+test+packaging) modeled at 33.48% of foundry price (market average) | https://cset.georgetown.edu/wp-content/uploads/AI-Chips%E2%80%94What-They-Are-and-Why-They-Matter-1.pdf |
| trendforce_2024_tsmc_2nm_wafer_30k_double_of_4_5nm.html | "price of 2nm wafers is expected to double compared to 4/5nm, which may exceed USD 30,000 per wafer" (Commercial Times via TrendForce, 2024-10-04) -> 4/5nm ~ $15-16k+ | https://www.trendforce.com/news/2024/10/04/news-tsmcs-2nm-wafers-reportedly-set-to-double-in-price-benefitting-ip-material-companies |
| trendforce_2024_tsmc_blended_wafer_asp_6611usd.html | TSMC blended 12-inch-equivalent wafer ASP = $6,611 in 4Q23 (+22% YoY) — context that leading-edge sells far above blended ASP | https://www.trendforce.com/news/2024/01/24/news-tsmcs-2023-wafer-average-selling-price-rises-by-22-driven-by-n3-process-success |
| semianalysis_ada_n5_wafer_2p2x_samsung_8nm.html | "wafer cost of TSMC N5/N4 is more than 2.2x that of Samsung 8nm" (SemiAnalysis, Sep 2022, free preview) | https://semianalysis.substack.com/p/ada-lovelace-gpus-shows-how-desperate |
| anandtech_2020_tsmc_n5_defect_density_wayback.html | TSMC N5 D0 "around 0.10 to 0.11 defects per square centimeter" in Aug 2020 (ramp), "expects to go below 0.10" next quarter; N7 hit 0.09 three quarters post-HVM (Wayback capture of AnandTech #16028) | https://www.anandtech.com/show/16028/better-yield-on-5nm-than-7nm-tsmc-update-on-defect-rates-for-n5 |
| nvidia_rtx_blackwell_whitepaper_gb202_750mm2.pdf | GB202: die size 750 mm², 92.2B transistors, sixteen 32-bit GDDR7 controllers (512-bit), 28 Gbps GDDR7 PAM3, 1.792 TB/s (RTX 5090); AD102 = 608.5 mm²/384-bit (comparison table) | https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf |
| locuza_ad102_608p44mm2_confirmed.html | AD102 die size 608.44 mm², 76.3B transistors (official, via Ryan Smith/AnandTech tweet quoted by Locuza) — GDDR6X host-die anchor | https://locuza.substack.com/p/nvidias-ad102-officially-revealed |
| angstronomics_rdna3_mcd_37p5mm2_n6.html | Navi31 MCD = ~37.5 mm² on TSMC N6 containing 16MB Infinity Cache + 64-bit GDDR6 PHY; InFO_oS fanout at 35 µm bump pitch; GCD ~308 mm² N5 | https://www.angstronomics.com/p/amds-rdna-3-graphics |
| arxiv_2510p06513_ucie_onpackage_memory_das_sharma.pdf | UCIe-S module: 1.143 mm die-edge x 1.54 mm depth @ 110 µm bump pitch, x32 link, 2dir x 32 lanes x 32 GT/s = 256 GB/s (224 GB/s/mm, 145.44 GB/s/mm²), 25 mm reach; LPDDR5 PHY bump map 5.8 mm x 1.75 mm per 128 DQ @ 9.6 GT/s (26.5 GB/s/mm, 15.1 GB/s/mm²); HBM4 8 mm x 2.5 mm per 2048b | https://arxiv.org/abs/2510.06513 |
| wikichip_n5_hd_sram_0p021um2_wayback.html | TSMC N5 HD SRAM bitcell 0.021 µm² (+~30% assist overhead noted) — shows on-die SRAM (few MB) is area-trivial | https://en.wikichip.org/wiki/5_nm_lithography_process |
| wikipedia_socket_sp5_6096_contacts_72x75mm.html | Socket SP5: 6,096 contacts, processor package 72 x 75.4 mm (5,428.8 mm²) — existence/size anchor for the ~6,000-ball root FCBGA class | https://en.wikipedia.org/wiki/Socket_SP5 |
| wikipedia_gddr7_pam3_32gbps_per_pin.html | GDDR7: PAM3 signaling, up to 32 Gb/s/pin (Samsung announcement; JEDEC JESD239 context) | https://en.wikipedia.org/wiki/GDDR7_SDRAM |
| wikipedia_ddr5_dual_subchannel_288pin.html | DDR5 DIMM: 288 pins, two independent subchannels each with own CA bus — basis for ~110-115 signals per full channel (~550 per 5-channel leaf) | https://en.wikipedia.org/wiki/DDR5_SDRAM |
| trendforce_2023_abf_substrate_market_9p3b_to_15b.html | ABF substrate market $9.3B (2023) -> $15B (2026E), 17% CAGR; server substrates drive layer count/area/complexity | https://www.trendforce.com/news/2023/05/25/server-specification-upgrade-a-bountiful-blue-ocean-for-abf-substrates |
| semiengineering_chiplet_package_cost_10_20_usd.html | Advanced chiplet-class packages cost "maybe $10 to $20" (A. Heinig, Fraunhofer IIS/EAS, quoted by SemiEngineering) — mid-size FCBGA anchor | https://semiengineering.com/can-chiplets-serve-cost-conscious-apps/ |
| semiengineering_test_costs_spiking_2pct_rule.html | "For decades, test was limited to a flat 2% of total manufacturing cost", now rising for complex parts — test-cost share anchor | https://semiengineering.com/test-costs-spiking/ |
| anysilicon_semiconductor_mfg_cost_breakdown.html | Recurring-unit-cost structure (wafer, sort, dicing, package, final test, logistics) + cost-per-good-die formula; NRE vs unit-cost split | https://anysilicon.com/semiconductor-manufacturing-cost-breakdown/ |
| cost_model.py / cost_model_output.txt | The computation itself: die areas, dies/wafer, Murphy yield, $/good die, package+test, per-system, volume curve | (this repo) |

Estimate-only inputs (no per-piece public price exists; flagged [E] in cost_model.py):
FCBGA substrate+assembly $ per package (anchored to Heinig $10-20 for mid-size, ABF-market
structure, and CSET's 33.48% ATP share), per-die test seconds/$ (anchored to the 2%-of-cost
rule), D0 for mature-2026 N5 (anchored to the 2020 ramp measurement 0.10-0.11 and TSMC's
trajectory), GDDR7-device/DDR5 PHY mm² (anchored to the LPDDR5 bump map, MCD 37.5 mm², and
GB202/AD102 die facts), bump counts per die (from ball counts given in the design spec).

---

# v2 refinement (2026-07-19): test/screening + server-class substrate

Scope unchanged (recurring per-unit manufacturing only; NRE/masks/design excluded).
v2 model: `cost_model_v2.py` / `cost_model_v2_output.txt`. v1 files retained above.
v2 working archive: /tmp/strata_silicon_cost_v2/evidence/. All v2 files fetched
2026-07-19 (curl w/ browser UA; teradyne + two roadmap PDFs via Wayback Machine
because the live hosts block scripted fetches).

What v2 changes vs v1 (central, at 10k-system volume):
system $571.98 -> $906.11. Movers: substrate $270->$412/sys (root $90->$150,
leaf $20->$29 -- server/AI ABF class), test+screening $33->$164/sys (explicit
sort / at-speed FT / burn-in / SLT / interface-hardware amortization),
+ $36/sys explicit package-stage test-yield scrap, assembly $115->$143/sys,
silicon +$2.3/sys (wafer finishing). Steady-state floor $813/sys; low $539;
high $1,685.

| # | File | Load-bearing claim (exact figure) | Source URL |
|---|---|---|---|
| S15 | HIR_2023_ch17_test.pdf | IEEE Heterogeneous Integration Roadmap 2023, Ch.17 Test: cost of test now <2-3% of IC revenue; tester depreciation "typically 5 or 6 years", useful life 15-20 yr, depreciation < half of complete test-cell operating cost; since 2015 consumables (probe cards, sockets, SLT device-specific hardware) are the leading test capex for large SOC; SOC tested 2-16 sites, memory >1,000; multi-die drives more SLT ("mission mode") + more exhaustive wafer probe; sockets ">20 GHz" for high-ball-count devices at engineering limit; "KGD does not mean that 100% of the bare dies will pass" | https://eps.ieee.org/images/files/HIR_2023/ch17_test.pdf (via web.archive.org/web/20240507035517) |
| S16 | itrs_2001_test.pdf | ITRS 2001 Test chapter, Table 21 ATE cost: high-performance ASIC/MPU tester = base $250-400k + $2,700-6,000 per pin at 512 pins (=> $1.6M-$3.5M class); "test may account for more than 70% of the total manufacturing cost" in some segments | http://public.itrs.net/Files/2001ITRS/Test.pdf (via web.archive.org/web/20060509104611) |
| S17 | se_screening_silent_data_errors.html | SemiEngineering "Screening For Silent Data Errors" (Meixner): server-market microprocessors get longer test patterns at wafer probe AND package test; "every part receives a system-level function test, often requiring between 40 minutes to an hour"; Meta 6-month/15-day fleet screens; SDEs escape all screens (100% containment not economically feasible) | https://semiengineering.com/screening-for-silent-data-errors/ |
| S18 | se_mission_critical_slt_expansion.html | SemiEngineering (Advantest Reichart): "SLT requires longer test times -- on the order of minutes to more than an hour, versus tens of seconds for ATE"; SLT cost-of-test-per-device driven by site count/floor area | https://semiengineering.com/mission-critical-devices-drive-system-level-test-expansion/ |
| S19 | se_adaptive_test_hpc_ai.html | SemiEngineering (Advantest's Davette Berry, 2025): "Most commercial products have gotten away from doing burn-in, but most of these high-performance compute devices are having to put it back in to the product test flow, because having it fail six hours after it's been installed in the data center is much worse" | https://semiengineering.com/adaptive-test-gaining-ground-for-hpc-and-ai-chips/ |
| S20 | se_package_level_burn_in.html | SemiEngineering: production burn-in on assembled packages "typically 24 to 48 hours (potentially longer depending on quality target)"; automotive HTOL qual 125C/1,000h context | https://semiengineering.com/easing-the-stress-for-package-level-burn-in/ |
| S21 | se_hbm_test_left.html | SemiEngineering "HBM Shifts Testing Left": advanced probe cards up to "$500,000"; DRAM tested 64-128 sites in parallel; DRAM flows include wafer-level burn-in + hot/cold insertions; KGD before stacking; DFT can save up to 80% of probe-card cost | https://semiengineering.com/hbm-shifts-testing-left-to-preserve-ai-chip-yield/ |
| S22 | advantest_t5801_gddr7.html | Advantest T5801 memory tester: "up to 36Gbps PAM3 and 18Gbps NRZ" for GDDR7/LPDDR6/DDR6 -- the production instrument class for exactly the root's device-mode 28G PAM3 interface exists | https://www.advantest.com/en/products/semiconductor-test-system/memory/t5801/ |
| S23 | teradyne_ultraflexplus_wayback.html | Teradyne UltraFLEXplus: UltraPHY 224G "test data rates up to 112 Gb/s NRZ and 224 Gb/s (112 Gbaud) PAM4"; UltraPHY 112G 64G NRZ/112G PAM4; targets high-speed SERDES; PACE/Broadside architecture | https://www.teradyne.com/products/ultraflexplus/ (via web.archive.org/web/20260514141046) |
| S24 | advantest_v93000_exa_scale.html | Advantest V93000 EXA Scale: "Pin Scale Multilevel Serial" = fully-integrated HSIO ATE with multilevel (PAM) capability; Pin Scale 5000 digital; platform targets HPC & AI | https://www.advantest.com/en/products/semiconductor-test-system/soc/v93000/ |
| S25 | advantest_b6700_burnin.html | Advantest B6700 memory burn-in system: "as many as 48 burn-in boards in parallel", test-while-burn-in | https://www.advantest.com/en/products/semiconductor-test-system/memory/b6700/ |
| S26 | aehr_10k_fy2025.htm | Aehr Test Systems 10-K (FY2025): burn-in times "minutes to hours or even days" by application; FOX-XP for wafer/die/module test+burn-in measured in hours-to-days; NAND enterprise mission-critical = 100% test and burn-in | https://www.sec.gov/Archives/edgar/data/1040470/000165495425008553/aehr_10k.htm |
| S27 | trendforce_2023_chiplet_substrates.html | TrendForce 2023-04-26: server platforms drive "higher-layer-count and larger-area ABF substrates"; 2020-22 ABF prices rose with record margins; growth = layer count + area | https://www.trendforce.com/news/2023/04/26/chiplet-design-a-real-game-changer-for-substrates/ |
| S28 | trendforce_2025_bt_fiberglass_20pct.html | TrendForce 2025-07-22 (Commercial Times): BT/T-glass substrate prices +up-to-20%; high-end fiberglass +20%; ABF shipments surging, "medium- to long-term price increases" expected for high-end ABF as sizes expand; T-glass tight until 2H26 capacity | https://www.trendforce.com/news/2025/07/22/news-bt-substrate-fiberglass-prices-reportedly-eye-20-hike-amid-ai-boom-and-supply-shortage/ |
| S29 | se_kgd_singulated_die_screening.html | SemiEngineering: singulated-die screening insertion for KGD (Intel Foundry); active thermal control merges 3 temperature insertions into 1 | https://semiengineering.com/quest-for-kgd-drives-singulated-die-screening/ |
| S30 | se_wafer_probe_multi_die.html | SemiEngineering: wafer probe struggles to deliver at-speed coverage for multi-die assemblies (supports loopback/DFT-based sort + package-level at-speed strategy) | https://semiengineering.com/wafer-probe-struggles-to-adapt-to-multi-die-assemblies/ |
| -- | arxiv_chiplet_actuary.pdf | Feng & Ma, DAC'22 (arXiv:2203.12268): RE-cost structure = raw chips + chip defects + raw packages + package defects + bonding-yield-driven KGD waste (structural cross-check for the staged scrap model) | https://arxiv.org/abs/2203.12268 |
| -- | arxiv_chiplet_cloud.pdf | Chiplet Cloud (arXiv:2307.02666): cost-per-die = (wafer/DPW + cost_test)/yield -- test cost belongs inside per-die cost (structural cross-check) | https://arxiv.org/abs/2307.02666 |

v2 estimate-only inputs (flagged [E] in cost_model_v2.py, all anchored to the
sources above): $/(cm2*layer) band 0.11-0.18 calibrated to S11 low-end +
S12/S27/S28 server-class premium; insertion times (sort 150s root / FT 300s
root central) anchored to S17 "longer patterns" + S15 parallelism limits;
cell-overhead multiplier 2.0-2.5x from S15's "depreciation < half of cell
cost"; interface-set totals ($600k root / $280k leaf central) from S21's
$500k probe-card ceiling + S15 consumables-dominance; burn-in slots/board
from package sizes; package-stage yields (FT 97% / BI 99.3% / SLT 99% root
central) are engineering estimates consistent with S15's KGD caveat and S17's
escape data. WebSearch was quota-exhausted this session; all discovery was
done via curl on site archives/sitemaps, Wayback CDX, Google News RSS, and
WebFetch -- every load-bearing figure above is in a saved file in this folder.
