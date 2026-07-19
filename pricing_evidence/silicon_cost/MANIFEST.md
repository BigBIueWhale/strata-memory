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
