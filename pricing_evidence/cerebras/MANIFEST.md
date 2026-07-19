# Cerebras MemoryX / weight-streaming — evidence manifest

Supporting `../../cerebras_memoryx.html`. Compiled 2026-07 from a four-front research
pass (MemoryX hardware & DRAM internals · the weight-streaming execution model ·
the SwarmX fabric & cluster scale · CS-3/latest + inference + independent analysis).

Every load-bearing claim in the write-up is pinned to a document below. Consistent with
the repo policy (see top-level `SOURCES.md`), **large vendor- and IEEE-copyrighted PDFs
are cited by URL, not redistributed** — fetch them from the original hosts. The
freely-distributable Cerebras-authored press/blog HTML and the public SEC filing are
archived here as lightweight snapshots.

## Archived here (freely-distributable Cerebras press/blog HTML)

| File | What it anchors | Date |
|---|---|---|
| `cerebras_2021_brain_scale_pr.html` | "4 TB – 2.4 PB", "up to 120 trillion parameters", MemoryX+SwarmX unveil | 2021-08-24 |
| `cerebras_2021_weight_streaming_announce_blog.html` | weight-streaming definition; "a single MemoryX unit can be used to target any number of CS-2 systems" | 2021-08-24 |
| `cerebras_2024_cs3_launch_pr.html` | CS-3 spec box: "External memory: 1.5TB, 12TB, or 1.2PB", "up to 24 trillion parameters", 2048 systems | 2024-03-13 |
| `cerebras_2024_cs3_launch_blog.html` | true SKU ladder 24/36/120/1,200 TB; retro-states CS-2 units as 1.5/12 TB | 2024-03-13 |
| `cerebras_2024_sandia_55tb_ddr5_pr.html` | **the DDR5 quote** — "55 terabyte MemoryX… commodity DDR5 memory in a 1U server format"; 1→16 CS-3, 15.3× | 2024-12-10 |
| `cerebras_2024_inference_launch_pr.html` | inference launch (SRAM-resident; MemoryX absent from datapath) | 2024-08-27 |
| `cerebras_2024_llama405b_inference_blog.html` | 405B @ 969 t/s, 128K ctx — SRAM-resident serving | 2024-11 |
| `cerebras_2024_condor_galaxy3_pr.html` | CG-3 = 64 CS-3 / 8 EF / Dallas | 2024-03-13 |
| `cerebras_2024_qualcomm_inference_pr.html` | train-on-CS-3 → deploy on Qualcomm AI 100 Ultra (Qualcomm's LPDDR, not MemoryX) | 2024-03-13 |
| `cerebras_2025_qwen3_235b_131k_pr.html` | Qwen3-235B, full 131K context inference | 2025-07-08 |
| `cerebras_2025_six_datacenters_pr.html` | six inference datacenters; "over 40 million Llama 70B tokens per second" | 2025-03-11 |
| `cerebras_2026_openai_750mw_blog.html` | OpenAI 750 MW inference partnership | 2026-01-14 |
| `cerebras_2026_ipo_pricing_pr.html` | IPO priced $185, ~$5.55B gross, Nasdaq: CBRS | 2026-05-13 |

## Cited, not redistributed (fetch from source)

| Document | Anchors | URL |
|---|---|---|
| Weight-streaming whitepaper — Hall/Schreiber/Lie (rev. Mar 2023, 34 pp) | DRAM+flash hybrid; 4TB–2.4PB; 32 bits/param/dir/iter; reuse argument; SwarmX broadcast-reduce; single-copy-to-N | https://8968533.fs1.hubspotusercontent-na1.net/hubfs/8968533/Virtual%20Booth%20Docs/CS%20Weight%20Streaming%20White%20Paper.pdf |
| Hot Chips 33 deck — Sean Lie (2021-08-24) | MemoryX slide ("DRAM and flash hybrid storage"); "complete disaggregation of memory and compute"; latency-hiding timeline | https://hc33.hotchips.org/assets/program/conference/day2/HC2021.Cerebras.SeanLie.v1.pdf |
| Hot Chips 34 deck — Sean Lie (2022) | WSE-2 cluster scale-out; broadcast/reduce | https://hc34.hotchips.org/assets/program/conference/day2/Machine%20Learning/HC2022_Cerebras_Final_v02.pdf |
| IEEE Micro 43(3) "Cerebras Architecture Deep Dive" (2023) | "Weights are stored in DRAM and flash memory in MemoryX and streamed… at 1.2 Tb/s"; per-weight AXPY reuse | https://ieeexplore.ieee.org/abstract/document/10123162 |
| Hot Chips 2024 deck — Sean Lie (2024-08-27, 71 pp) | inference: "weights and KV cache stored locally in the region memory"; "4× WSE-3 = 176 GB SRAM" | https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf |
| Cerebras Wafer-Scale Cluster datasheet (rev. Jun 2024) | rack BOM (3× MemoryX enclosure/CS-3, 42U, 34 kW); "12 to 1,200 TB of off-chip model memory"; 12×100GbE | https://8968533.fs1.hubspotusercontent-na1.net/hubfs/8968533/Cerebras%20Wafer%20Scale%20Cluster%20datasheet%20-%20final.pdf |
| CS-2 datasheet; WSE-3 datasheet; current CS-3 datasheet | 40/44 GB SRAM; 1.2 Tb/s system I/O; inference-era datasheet has no external-memory row | cerebras.ai datasheets (hubspot/sanity CDNs) |
| Cerebras "Scaling Up and Out" eng. blog (2022) | "the model memory has a bandwidth of 4 TB/s"; "8 TB… adequate for GPT-3" | https://www.cerebras.ai/blog/scaling-up-and-out-training-massive-models-on-cerebras-systems-using-weight-streaming |
| Cerebras-GPT (arXiv:2304.03208) | measured weak-scaling "linear within 9%" to 16 CS-2 | https://arxiv.org/abs/2304.03208 |
| SEC Form S-1 (2024-09-30) | MemoryX filed under "training parameter storage"; SwarmX 400G/800G, up to 2048 CS-3; SKUs 30B–24T params; G42 revenue concentration; SOW prices redacted | https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm |
| Condor Galaxy 1 blog + PR (2023-07) | "82 terabytes of memory… unified 82 Terabyte block"; 64 CS-2; 386/388 Tb/s fabric | cerebras.ai (CG-1 blog / G42 PR) |
| Andromeda PR (2022-11-14) | 16 CS-2; 96.8 Tb/s fabric | cerebras.ai |
| The Next Platform — MemoryX/SwarmX (2021), CS-3 hyperscale (2024), OpenAI deal (2026-01), post-IPO (2026-05) | third-party analysis; "compute-to-SRAM ratio wrong for low-latency inference"; WSE-4 "optical links… to shared DRAM memory trays" (speculation); price/perf | nextplatform.com |
| ServeTheHome — Hot Chips 2023 cluster detail; inference launch | MemoryX "up to 1 TB DRAM + 500 TB flash" per node; "theoretical" 2048-system cluster; 4-wafer 70B serving | servethehome.com |
| SemiAnalysis "Groq Inference Tokenomics" (2024-02-21) | transferable SRAM-residency/batch-economics critique of the wafer-SRAM inference class | semianalysis.com |
| IEEE Spectrum "Cerebras CS-3" (2024) | "nothing quite that big is in the works"; core count leveled WSE-2→WSE-3 | spectrum.ieee.org |
| Qualcomm Cloud AI 100 Ultra product page | 128 GB LPDDR4x + 576 MB SRAM (Qualcomm's DRAM, not MemoryX) | qualcomm.com |

**Confidence.** DRAM+flash hybrid (CS-2) and commodity-DDR5 1U (CS-3) are verbatim-primary.
Undisclosed anywhere: MemoryX internal DRAM bandwidth per unit, DRAM:flash split of the
120 TB / 1.2 PB SKUs, per-SKU DRAM generation, and MemoryX standalone power/price (SEC
exhibits redacted). Marketing envelope figures (2.4 PB / 120T; 2048-system / 256-EF
clusters) are flagged as never-shipped in the write-up.
