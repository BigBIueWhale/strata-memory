# Sources

The primary datasheets, standards, and papers behind these design records. They are
**not** included in this repository (many are vendor-copyrighted); download from the
original hosts below. All URLs verified live in July 2026.

## GDDR7 / fast tier
- Micron GDDR7 product brief — https://www.micron.com/content/dam/micron/global/public/products/product-flyer/gddr7-product-brief.pdf
- NVIDIA RTX PRO 6000 Blackwell Workstation datasheet — https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/rtx-pro-6000-blackwell-workstation-edition/workstation-blackwell-rtx-pro-6000-workstation-edition-nvidia-us-3519208-web.pdf
- NVIDIA RTX Blackwell PRO GPU architecture whitepaper — https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/NVIDIA-RTX-Blackwell-PRO-GPU-Architecture-v1.0.pdf
- Achronix Speedster7t GDDR6 user guide UG091 (SI/electrical reference) — https://www.achronix.com/sites/default/files/docs/Speedster7t_GDDR6_User_Guide_UG091.pdf
- PAM3 DRAM-bus signal-integrity (arXiv 2410.12990) — https://arxiv.org/pdf/2410.12990
- JEDEC GDDR7 standard JESD239 (member-gated) — https://www.jedec.org/standards-documents/docs/jesd239e

## DDR5 / bulk tier
- Micron 128 GB DDR5 RDIMM product brief — https://www.micron.com/content/dam/micron/global/public/documents/products/product-flyer/128gb-ddr5-rdimm-product-brief.pdf
- Micron DDR5/DDR4 module part-numbering guide — https://assets.micron.com/adobe/assets/urn:aaid:aem:4c7ee063-8a72-45c3-90c8-a0254083ccc7/original/as/numsdrammod.pdf
- Micron "DDR5 SDRAM: New Features" whitepaper — https://www.micron.com/content/dam/micron/global/public/products/white-paper/ddr5-new-features-white-paper.pdf
- Micron DRAM module reference guide — https://www.micron.com/content/dam/micron/global/public/products/memory/dram-modules/broad-product/dram-module-reference-guide.pdf
- Montage DDR5 RCD/DB/MRCD/MDB selection guide — https://www.montage-tech.com/sites/default/files/2025-02/MB%20Products%20Selection%20Guide_0.pdf
- 288-pin DDR5 RDIMM datasheet (mechanical) — https://www.unisemicon.com/uploadfile/2023/1228/20231228025734751.pdf
- MRDIMM analysis (arXiv 2605.02371) — https://arxiv.org/pdf/2605.02371
- JEDEC DDR5 device JESD79-5; modules JESD305/JESD308; mechanical MO-329 (member-gated) — https://www.jedec.org

## Coherent tiering / precedent / workload
- NVIDIA Grace Hopper architecture whitepaper — https://storage.ghost.io/c/35/17/35170502-dfe4-4f36-9612-bdc657f28241/content/files/2023/12/NVIDIA_Grace_Hopper_Superchip_Architecture_Overview_Whitepaper.pdf
- "Hitchhiker's Guide" — CXL / NVLink-C2C / Infinity Fabric measurements (arXiv 2411.02814) — https://arxiv.org/pdf/2411.02814
- Grace Hopper measured C2C / migration (arXiv 2407.07850) — https://arxiv.org/pdf/2407.07850
- CXL 3.0 whitepaper — https://computeexpresslink.org/wp-content/uploads/2023/12/CXL_3.0_white-paper_FINAL.pdf
- TPP memory tiering (arXiv 2206.02878) — https://arxiv.org/pdf/2206.02878
- AMD Instinct MI300A datasheet (LGA-6096 existence proof) — https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300a-data-sheet.pdf
- Kimi K2 technical report (arXiv 2507.20534) — https://arxiv.org/pdf/2507.20534
- DeepSeek-V2 (MLA KV-cache formula, arXiv 2405.04434) — https://arxiv.org/pdf/2405.04434

## Packaging / mechanical
- OCP OAM (Open Accelerator Module) design spec v1.0 — https://ocp-all.groups.io/g/OCP-OAI/attachment/5/0/ocp%20accelerator%20module%20design%20specification_v1p0_Candidate0725.pdf
- PCIe CEM r3.0 (card mechanical envelope) — from PCI-SIG

## Reference photos (not redistributed)
- RTX 6000D clamshell teardown (front die + back-side memory) — Club386, https://www.club386.com/nvidia-rtx-6000d-teardown-shows-84gb-vram-using-3gb-memory-chips/

## Model capacity: MTP + vision pass (July 2026)
- DeepSeek-V3 technical report (MTP architecture, D=1, spec-decode reuse; arXiv 2412.19437) — https://arxiv.org/pdf/2412.19437
- DeepSeek-V3 HF model card ("685B = 671B main + 14B MTP module") + config + API — https://huggingface.co/deepseek-ai/DeepSeek-V3
- Kimi-VL technical report (MoonViT 400M, MLP projector, 3.2MP native-res; arXiv 2504.07491) — https://arxiv.org/pdf/2504.07491
- Kimi-VL-A3B-Thinking-2506 config/API — https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking-2506
- Kimi K2.5 / K2.7-Code model cards (MoonViT 400M vision encoder, 256K context, native INT4) — https://huggingface.co/moonshotai/Kimi-K2.5 , https://huggingface.co/moonshotai/Kimi-K2.7-Code
- vLLM engine args (gpu-memory-utilization default 0.92 = 8% reserve) — https://docs.vllm.ai/en/latest/configuration/engine_args.html

## Kimi K3 launch + native-precision pass (2026-07-18)
- Kimi K3 announcement, "Kimi K3: Open Frontier Intelligence" (2.8T params; KDA + AttnRes + Gated MLA; 16-of-896 experts, Stable LatentMoE; native vision; 1M context; QAT from SFT onward, MXFP4 weights + MXFP8 activations; weights due 2026-07-27) — https://www.kimi.com/blog/kimi-k3
- Kimi API platform pricing, Kimi K3 (model id kimi-k3; context 1,048,576; $0.30 cache-hit / $3.00 cache-miss / $15.00 output per MTok) — https://platform.kimi.ai/docs/pricing/chat-k3 (index: /docs/pricing/chat)
- Kimi-Linear-48B-A3B-Instruct config.json (KDA:MLA 3:1 layer ratio precedent — 20 kda_layers vs 7 full_attn_layers of 27; KDA head_dim 128; MLA kv_lora_rank 512 + qk_rope 64) — https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct
- Kimi K2 technical report p.7 (Sparsity Scaling Law; sparsity 48 = 8-of-384 adopted for K2; abstract: 1.04T total / 32B activated; BF16 training, FP8-E4M3 storage of insensitive activations only) — https://arxiv.org/pdf/2507.20534
- Kimi K2.5 technical report (arXiv 2602.02276, "Visual Agentic Intelligence") — https://arxiv.org/abs/2602.02276
- Crucial DDR5-5600 UDIMM MSRPs via Wayback: CT16G56C46U5 $144.99, CP24G56C46U5 $195.99, CP32G56C46U5 $292.99, CP48G56C46U5 $380.99 (snap 2026-04-16, flagged EOL), CP64G56C46U5 $555.99 (snap 2026-04-14) — https://web.archive.org/web/2026*/https://www.crucial.com/memory/ddr5/
- Crucial Pro **CP48G56C46U5** product page — the chosen 48 GiB DDR5-5600 UDIMM (CL46, Pro series, **EOL** badge, and the 8/16/24/32/48/64 GB density ladder visible) — crucial.com; screenshot in `pricing_evidence/crucial_CP48G56C46U5_product_page.png` (+ archived HTML `pricing_evidence/wayback_crucial_CP48G56C46U5*.html`)

## NVIDIA B200 / GB200 scale-out + serving economics (2026-07-18/19)
- NVIDIA DGX B200 page + user guide (180 GB/GPU shipping = 1,440 GB/node; 14.4 TB/s all-to-all NVLink; 8× ConnectX-7 400 Gb/s IB scale-out) — https://www.nvidia.com/en-us/data-center/dgx-b200/ , https://docs.nvidia.com/dgx/dgxb200-user-guide/introduction-to-dgxb200.html
- NVIDIA HGX platform (B200 8-GPU, 1.4 TB total memory) — https://www.nvidia.com/en-us/data-center/hgx/
- NVIDIA Blackwell architecture technical brief (5th-gen NVLink 1.8 TB/s/GPU = 18×100 GB/s; per-GPU memory; HGX B300 NVL16) — https://resources.nvidia.com/en-us-blackwell-architecture
- NVIDIA GB200 NVL72 (72-GPU single NVLink domain, 130 TB/s aggregate, 13.4 TB HBM3e ≈ 186 GB/GPU) + dev blog (NVL36 = 36 GPUs, 9 dual-GB200 nodes) — https://www.nvidia.com/en-us/data-center/gb200-nvl72/ , https://developer.nvidia.com/blog/nvidia-gb200-nvl72-delivers-trillion-parameter-llm-training-and-real-time-inference/
- NVIDIA NVLink / NVSwitch (5th-gen; official NVLink domain sizes **8 | 72** — no NVL16 for B200) — https://www.nvidia.com/en-us/data-center/nvlink/
- NVIDIA DGX SuperPOD B200 reference architecture (scale-out between 8-GPU nodes is Quantum-2 NDR 400G InfiniBand, not NVLink) — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/
- 8× B200 reseller prices (Exxact $338k, IT Creations/Supermicro $449k, GPTshop from $350k, Thinkmate $506k, ViperaTech DGX $580k, Wiredzone HGX baseboard $325k) — captures in `pricing_evidence/b200_gb200_serving/`
- GB200 NVL36 / NVL72 price estimates (Morgan Stanley / TrendForce ~$1.8M / ~$2–3M per rack) — `pricing_evidence/b200_gb200_serving/`
- Bank of Israel USD/ILS reference rate (3.05, 2026-07-17), cross-checked vs ECB/Frankfurter — https://www.boi.org.il
- Israel VAT 18% (from 2025-01-01; Israel Tax Authority Directive 01/2025; PwC Tax Summaries) — https://taxsummaries.pwc.com/israel/corporate/other-taxes
- 0% customs duty on servers (HS 8471) — WTO Information Technology Agreement (Israel participant) + US–Israel FTA — https://www.wto.org/english/tratop_e/inftec_e/itapart_e.htm
- Archived research evidence (NVIDIA datasheets, FX JSONs, VAT/customs pages, reseller captures): `pricing_evidence/b200_gb200_serving/` (124 files)

## Prior art / competitive landscape (2026-07)
- OpenAI–Broadcom custom inference chip announcement (memory config undisclosed) — https://openai.com/index/openai-broadcom-jalapeno-inference-chip
- OpenAI HBM-bridge patent WO 2026/075822 (up to 20 HBM stacks via embedded bridges) — patent search + trade coverage
- Credo "Weaver" memory-fanout gearbox (16 TB/s + 6.4 TB LPDDR5X per xPU) — https://www.businesswire.com/news/home/20251103560324/en/
- Majestic Labs "Prometheus" (>100 TB LPDDR pooling; custom memory-interface chiplet) — EE Times, Business Wire, TechSpot
- Celestial AI photonic memory (DDR5 fronted with HBM semantics + write-through cache) — https://www.nextplatform.com/2024/04/04/celestial-ai-wants-to-break-the-memory-wall-fuse-hbm-with-ddr5/
- Qualcomm "High Bandwidth Compute" (compute-under-DRAM; investor day 2026) — https://www.forbes.com/sites/stevemcdowell/2026/06/25/qualcomms-ai-data-center-bet-inside-the-dragonfly-strategy/
- Eliyan converter-chiplet patent US 12,058,874 ("peripheral gearbox chiplet / interface conversion circuitry") — https://www.freepatentsonline.com/12058874.html
- MetaRAM (now Google) impersonation patent US 8,949,519 "Simulating a memory circuit" (freedom-to-operate reference) — https://www.freepatentsonline.com/8949519.html
- Huawei self-developed HBM (HiBL/HiZQ) + CXMT domestic HBM — Wccftech HC2025 roadmap; DigiTimes; SemiAnalysis
- d-Matrix / Positron / SambaNova SN40L / SanDisk–SK hynix HBF / Enfabrica EMFASYS / Skymizer — captures in `pricing_evidence/prior_art/`
- arXiv: "The Economics of AI Decoding Chips" (2607.13068); SambaNova SN40L (2405.07518); MemExplorer (2604.16007)
- Archived research evidence (154 files: vendor/patent/press/arXiv captures across OpenAI+hyperscalers, US startups, China, memory vendors, academic/patents, accelerators): `pricing_evidence/prior_art/`

## Converter silicon per-unit cost (TSMC N5, NRE/masks excluded) (2026-07)
- N5 300 mm wafer ~$16,988 — CSET "AI Chips: What They Are and Why They Matter" (Table 9) — https://cset.georgetown.edu/wp-content/uploads/AI-Chips%E2%80%94What-They-Are-and-Why-They-Matter-1.pdf ; 4/5nm ~$15–16k, 2nm price doubling — TrendForce 2024-10-04
- N5 defect density D0 ~0.10/cm² at ramp (heading below 0.10) — AnandTech, TSMC Symposium 2020
- UCIe-S die-to-die module geometry (1.76 mm²/×32 link; 224 GB/s/mm) + LPDDR5 bump-map density — Das Sharma et al., arXiv:2510.06513
- Die-area anchors: NVIDIA GB202 750 mm² / 512-bit GDDR7 (RTX Blackwell whitepaper); AMD Navi31 MCD 37.5 mm² N6 = 64-bit GDDR6 PHY + 16 MB SRAM (Angstronomics); AD102 608.44 mm² (Locuza)
- N5 SRAM bitcell 0.021 µm² — WikiChip 5nm
- FCBGA package cost anchors (chiplet-class ~$10–20; ABF server-substrate market) — SemiEngineering / TrendForce; test ~2%-of-cost, rising for complex parts — SemiEngineering
- ~6,000-ball package class exists (Socket SP5, 6,096 contacts) — Wikipedia
- Full cost model + evidence + re-runnable `cost_model.py` / `cost_model_v2.py` + `MANIFEST.md`: `pricing_evidence/silicon_cost/`
- v2 test/screening refinement (why per-system is ~$906, not ~$572): Advantest T5801 (36 Gb/s PAM3 GDDR7 test); Teradyne UltraFLEXplus / UltraPHY; ITRS test-cost tables; HIR 2023 ch.17 (consumable interface hardware — probe cards to ~$500k — is the leading test capex); System-Level Test 40–60 min + burn-in 24–48 h for server parts + silent-data-error screening (SemiEngineering); Aehr burn-in (10-K)
- v2 substrate refinement: server/AI-class ABF layer/area pricing + 2025–26 tight-supply increases (TrendForce, BT/T-glass +20%); Socket SP5 6,096-contact body class (Wikipedia)

## Cerebras MemoryX / weight streaming — external-DRAM prior art (2026-07)
- Weight-streaming whitepaper (Hall/Schreiber/Lie, rev. Mar 2023): "the MemoryX architecture uses both DRAM and flash storage in a hybrid fashion"; 4TB–2.4PB / up to 120T params; 32 bits/param/direction/iteration; SwarmX broadcast-reduce; "a single MemoryX unit can be used to target any number of CS-2 systems" — https://8968533.fs1.hubspotusercontent-na1.net/hubfs/8968533/Virtual%20Booth%20Docs/CS%20Weight%20Streaming%20White%20Paper.pdf
- Hot Chips 33 (2021) Cerebras deck — MemoryX "DRAM and flash hybrid storage"; "a complete disaggregation of memory and compute" — https://hc33.hotchips.org/assets/program/conference/day2/HC2021.Cerebras.SeanLie.v1.pdf
- Hot Chips 34 (2022) Cerebras deck — WSE-2 cluster scale-out — https://hc34.hotchips.org/assets/program/conference/day2/Machine%20Learning/HC2022_Cerebras_Final_v02.pdf
- IEEE Micro 43(3), 2023 "Cerebras Architecture Deep Dive" — "Weights are stored in DRAM and flash memory in MemoryX and streamed into the CS-2 at its full IO bandwidth of 1.2 Tb/s" — https://ieeexplore.ieee.org/abstract/document/10123162
- Hot Chips 2024 Cerebras deck — inference: "weights and KV cache stored locally in the region memory"; "4× WSE-3 = 176GB of SRAM" — https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf
- Cerebras Wafer-Scale Cluster datasheet (rev. Jun 2024) — rack BOM (3× MemoryX enclosure per CS-3, 42U, 34 kW); "12 to 1,200 TB of off-chip model memory"; 12×100GbE — https://8968533.fs1.hubspotusercontent-na1.net/hubfs/8968533/Cerebras%20Wafer%20Scale%20Cluster%20datasheet%20-%20final.pdf
- WSE-3 datasheet (44 GB on-chip SRAM, 21 PB/s memory bandwidth, 900k cores, 4T transistors, TSMC 5nm) + CS-2 datasheet (1.2 Tb/s system I/O) — cerebras.ai datasheets (hubspot/sanity CDNs)
- Sandia trillion-parameter PR (2024-12-10) — "55 terabyte MemoryX device. By employing commodity DDR5 memory in a 1U server format…"; 1→16 CS-3, 15.3× — https://www.cerebras.ai/press-release/cerebras-demonstrates-trillion-parameter-model-training-on-a-single-cs-3-system
- CS-3 launch PR + blog (2024-03-13) — SKU ladder 24/36/120/1,200 TB; up to 24T params; 2048 systems — https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine ; https://www.cerebras.ai/blog/cerebras-cs3
- 2021 "brain-scale" PR (4TB–2.4PB / 120T) + weight-streaming announce blog — https://www.cerebras.ai/press-release/cerebras-systems-announces-worlds-first-brain-scale-artificial-intelligence-solution ; https://www.cerebras.ai/blog/announcing-the-cerebras-architecture-for-extreme-scale-ai
- "Scaling Up and Out" eng. blog — model memory "bandwidth of 4 TB/s"; "8 TB… adequate for GPT-3" — https://www.cerebras.ai/blog/scaling-up-and-out-training-massive-models-on-cerebras-systems-using-weight-streaming
- Condor Galaxy 1 blog/PR (82 TB / 64 CS-2 / 386–388 Tb/s); Andromeda PR (16 CS-2 / 96.8 Tb/s); Cerebras-GPT arXiv:2304.03208 (weak-scaling to 16 CS-2) — cerebras.ai ; https://arxiv.org/abs/2304.03208
- Cerebras Inference launch (2024-08-27) — SRAM-resident, "eliminating the need for external memory and for the slow lanes linking external memory to compute"; Llama-405B @ 969 t/s (2024-11) — https://www.cerebras.ai/press-release/cerebras-launches-the-worlds-fastest-ai-inference ; https://www.cerebras.ai/blog/llama-405b-inference
- SEC Form S-1 (2024-09-30) — MemoryX filed under "training parameter storage"; SwarmX 400G/800G up to 2048 CS-3; SKUs support 30B–24T params; G42 revenue concentration; SOW prices redacted — https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm
- Third-party analysis: The Next Platform (MemoryX/SwarmX 2021; CS-3 hyperscale 2024; OpenAI deal 2026-01; post-IPO "optical links… to shared DRAM memory trays" speculation 2026-05); ServeTheHome (HC2023 MemoryX "up to 1 TB DRAM + 500 TB flash"/node; 4-wafer 70B inference); SemiAnalysis "Groq Inference Tokenomics" (2024-02, transferable SRAM/batch-economics critique); IEEE Spectrum "Cerebras CS-3" ("nothing quite that big is in the works")
- Qualcomm Cloud AI 100 Ultra — 128 GB LPDDR4x + 576 MB SRAM (Qualcomm's DRAM, not MemoryX) — https://www.qualcomm.com/products/technology/processors/cloud-artificial-intelligence/cloud-ai-100
- Curated freely-distributable press/blog snapshots + full source manifest (redistribution-safe subset; large vendor/IEEE PDFs cited-not-redistributed per policy above): `pricing_evidence/cerebras/`

## Cerebras interconnect + huge-model inference — "NVLink the wafers?" + GLM-5.2 pricing (2026-07)
- Inter-wafer inference mechanism (verbatim): "Transfer only activations between wafers… low-latency RDMA over Ethernet… <5us, 4 hops, <1% impact… 100Gbps required, <10% of available" — HC2024 deck (URL above)
- NVLink-5 / NVL72: 1.8 TB/s per Blackwell GPU (18×100 GB/s); NVL72 = 130 TB/s aggregate, 13.4 TB pooled HBM, "a single, massive GPU"; NVSwitch = one shared physical address space + native atomics — NVIDIA Hot Chips 2024 deck; NVSwitch HC34 deck; nvidia.com GB200/GB300 pages
- Poolability contrast set — Tesla Dojo (flat-address DMA, tile SRAM "private", shared DIP DRAM): Hot Chips 34 Dojo decks + TTPoE HC2024; Dojo disbanded 2025-08 (Reuters) / "Dojo 3" restart 2026-01 (Tom's Hardware); Groq logically-shared distributed SRAM (ISCA 2022, arXiv/Wayback); SambaNova SN40L three-tier SRAM+HBM+DDR (HC2024 + arXiv:2405.07518); Graphcore Bow (docs.graphcore.ai); Tenstorrent Blackhole (HC2024); Lightmatter Passage M1000 114 Tbps (lightmatter.co); Celestial AI → Marvell close 2026-02-02 (Marvell PR, Wayback); UALink 1.0 native memory semantics (ualinkconsortium.org)
- Cerebras + Ranovus $45M DARPA co-packaged-optics (100–150× target) — cerebras.ai / Ranovus PR 2025-04-01
- GLM-5.2 = 753.33B, 256+1 experts/layer (~40B active), MLA rank 512+64, 78 layers, 1,048,576 ctx, BF16 1,506.7 GB — https://huggingface.co/zai-org/GLM-5.2 (config.json + safetensors param API, 2026-07-20); config/README archived in `pricing_evidence/cerebras/`
- Model sizing (HF config.json + safetensors param API, 2026-07-20): Qwen3.5-397B-A17B; Kimi-K2.6 (1.06T, INT4 QAT ≈595 GB); Llama-3.1-405B; Qwen3-235B-A22B-2507; Qwen3-Coder-480B; gpt-oss-120B (MXFP4); Llama-3.3-70B
- Cerebras inference practice: on-chip weights+KV, native-precision storage (16/8/4-bit, dequant on the fly) — inference-docs.cerebras.ai; Kimi-K2.6 "stores the entire model on-chip" at INT4 — https://www.cerebras.ai/blog/cerebras-kimi-k2-Enterprise ; AWS Bedrock disaggregation (Trainium prefill → CS-3 decode) — https://www.cerebras.ai/blog/disaggregated-inference ; GLM-4.7 — https://www.cerebras.ai/blog/glm-4-7 ; dedicated endpoints incl. GLM-5/5.1 — https://inference-docs.cerebras.ai/dedicated/overview.md
- Wafer-count opacity + 405B "12 systems, 350 t/s projected" — The Register 2024-08-27 (https://www.theregister.com/2024/08/27/cerebras_ai_inference/); "first three, then four, then stopped" + WSE-4 optics wish-list — TNP 2026-05-15; CS-3 ASP ~$2.26M derived (G42 $434.5M / ~192 systems) — TNP 2026-04-22 [CS-3 unit price never published — flagged estimate]
- Independent measured inference speeds — Artificial Analysis (artificialanalysis.ai/providers/cerebras)
- Full interconnect + huge-model research notes: /tmp research corpus (`E_`/`F_` prefixes, ~150 artifacts); curated GLM-5.2 config/README + Cerebras blog snapshots in `pricing_evidence/cerebras/`

## Why GPUs don't use DDR5 — bandwidth density + the design-in paradox (2026-07)
- Bandwidth density (GB/s per mm of controller-die shoreline): DDR5-DIMM ~5–11 · GDDR7 ~23 · HBM3e ~190–205 · UCIe-A ~660 — derived from Das Sharma et al. UCIe/BoW shoreline analysis (arXiv:2510.06513) + AD102/GB202 die-shot geometry
- Per-pin rate root cause — soldered point-to-point PAM3 vs socketed multi-drop NRZ: JESD239 (GDDR7 28–32 Gb/s PAM3) vs JESD79-5/5C (DDR5 5.6–8.8 Gb/s NRZ); the DIMM's virtues (socket, multi-drop, ranks) ARE the density cap (EE Stack Exchange; HN silicon-engineer commentary)
- Energy per bit (pJ/b): Micron GDDR7 brief ~4.5; GDDR6 ~7.25 / GDDR6X ~7.5 / GDDR5 ~14; DDR5 subsystem ~12–22; O'Connor "Fine-Grained DRAM" MICRO-50 (GDDR5 14 / HBM2 3.9 pJ/b); Dally HC2023 keynote (DRAM ~20 pJ/b read); DATE'21 HBM-undervolting (~7 vs 25 pJ/b HBM-vs-DDRx); Rambus GDDR6-vs-HBM2E PHY-power WP; NVIDIA Grace ("one-eighth the power per GB/s", 8-ch DDR5 vs LPDDR5X)
- Killer geometry: 1.79 TB/s of DDR5-class PHY ≈ 165–360 mm of die edge = 1.5–3.2× a GB202 perimeter (~111 mm, ~70% already GDDR7); 45 UDIMM channels ≈ 5,500 signal pins / 8–10k balls
- DDR4-vs-GDDR5 natural experiment (−50–55% FPS, same GPU + bus width) — GamersNexus (GT 1030)
- Design-in side-port precedents (why a co-designed host chooses a side-port over impersonation): NVIDIA Grace (LPDDR5X), AMD MI300, SambaNova SN40L (1.5 TB DDR @ ~200 GB/s beside 64 GB HBM @ 2 TB/s), Credo/Celestial/Eliyan host links
- GPU memory system-visible latency (~226–335 ns) is the GPU hierarchy, not the DRAM — a GDDR-attached CPU would see ~133 ns (Chips and Cheese) — i.e. STRATA-V's latency story survives
- Full adversarial report + 37 archived source artifacts (`G_` prefix, incl. O'Connor MICRO-50, Dally HC2023, Micron/Rambus/Samsung/SK hynix memory-power docs, JEDEC GDDR7 PR, AD102 die shot, community captures): /tmp research corpus
