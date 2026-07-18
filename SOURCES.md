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
