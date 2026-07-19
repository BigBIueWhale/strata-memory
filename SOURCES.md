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
