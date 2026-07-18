# STRATA — custom-silicon designs for scaling GPU memory

A set of linked engineering **decision records and research reports** exploring one question:

> How do you give a GPU **far more memory** (up to multiple TiB) than any single
> memory type can provide on its bus — while keeping the bandwidth and latency
> characteristics of a high-end card like an RTX 5090?

These are **hypothetical, pre-silicon design studies** — analysis, not products, and
not affiliated with or endorsed by any vendor. They reference real, publicly
documented parts and products (GDDR7, DDR5, NVIDIA/AMD accelerators, JEDEC/OCP/CXL
standards) purely as factual anchors and shipping existence-proofs. Every design
assumes freedom to tape out custom silicon; every load-bearing wall is closed with a
real, shipping reference, and estimates are flagged as such.

## The documents

| # | File | What it is |
|---|------|-----------|
| 1 | [`strata_2t_design.html`](strata_2t_design.html) | **STRATA-2T** — a two-tier-memory accelerator: a 96 GiB GDDR7 fast tier (1.79 TB/s, an RTX PRO 6000-class subsystem) fused with a 2 TiB DDR5 bulk tier in one coherent address space. Modeled on the Grace Hopper HBM+LPDDR division of labor. |
| 2 | [`strata_v_design.html`](strata_v_design.html) | **STRATA-V** — a DDR5 *memory-virtualizer*: a converter hierarchy that makes ~600 ordinary DDR5 dies appear to a GPU as **one impossible chip** (2.25 TiB, 1.79 TB/s, fixed-beat protocol). Same pin count and bandwidth as a 5090, ~70× the capacity. |
| 3 | [`rtx5090_strata_v_retrofit_verdict.html`](rtx5090_strata_v_retrofit_verdict.html) | **Retrofit verdict** — why you *cannot* desolder a stock RTX 5090's GDDR7 and bolt STRATA-V on to trick it into 2 TiB. A negative result: a finished GPU's memory is defined by its controller, not its chips. |
| 4 | [`sourcing_report.html`](sourcing_report.html) | **Sourcing report** — can you actually *buy* it? A four-thread hunt for the finished product, the DDR5 parts, the converter silicon, and the CXL path, with real 2026 reseller prices — and a corrected (6–10× higher) DDR5 cost. |
| 5 | [`kimi_k3_1m_full_quality.html`](kimi_k3_1m_full_quality.html) | **Kimi K3 @ 1M, full quality — checked out** — the honest memory build for the *real, announced* Kimi K3 (2.8T params, **MXFP4-native** QAT, 96 layers, KDA+MLA hybrid, native vision, 1M context; weights due 2026-07-27). Native precision **determined from Moonshot's own docs** (not assumed): at MXFP4 full quality + un-quantized FP16 KV + MTP + vision ≈ **1.56 TiB** → 45× 48 GiB DDR5-5600 UDIMM @ 1.79 TB/s ≈ **₪61,500 landed**. The ₪30k question, answered straight: **NO** (2× over, estimate-proof — ₪30k runs the previous-gen K2.7, not K3). Evidence in `pricing_evidence/`. |
| 6 | [`kimi_k3_serving_economics.html`](kimi_k3_serving_economics.html) | **Serving economics** — how many users a machine serves K3 to at a 1M-token context (a fixed **~1.45 TiB** model + **~28 GiB/user** KV), the NVIDIA B200 / GB200 options priced for Israel (16× B200 ≈ **₪2.6–3.35M** → ~42 users; GB200 **NVL36** ≈ ₪6.5M → ~165; **NVL72** → ~380), and why cost-per-user *falls* as the shared pool grows (₪80k → ₪39k → ₪28k) — the market case for the cheap-capacity converter. Evidence in `pricing_evidence/b200_gb200_serving/`. |

## The through-line (what the three docs establish)

- **Pins buy bandwidth; capacity is depth.** They're independent axes — `bandwidth ≈ pins × per-pin rate`, capacity is how much DRAM sits behind the pins. So once bandwidth fixes the channel count (and the converter with it), **capacity is a free dial** set by DIMM density alone — the same converter is the cheapest build at *every* capacity, with a hard floor of `channels × smallest DIMM` (360 GiB for the DDR5-5600 UDIMM build; the chosen 48 GiB is the density where that dial lands exactly on Kimi K3).
- **1.79 TB/s is a *low* bandwidth.** It's ~18 MRDIMM channels or ~35 DDR5-6400 channels — reachable with cheap, deep commodity DRAM, no GDDR7 required.
- **At multi-TiB scale, bandwidth is nearly free.** 2 TiB of commodity DDR5 already contains multiple TB/s of latent parallelism; a converter just exposes the slice you want.
- **A converter can front cheap-and-deep DDR5 as a fast, huge virtual device** — the catch is a fixed ~5–10% latency tax and a hard requirement that the backing stay *deterministic* (a fixed-beat memory protocol has no "please wait").
- **You can't retrofit this onto a shipped GPU** — GDDR7 has no capacity-expansion signaling, the timing is training-frozen, and 28 Gb/s PAM3 can't leave the board. Integration is *design-in*, not *bolt-on*.
- **It provably serves on time — because you *author* the deadline, not race it.** `CL`, `tRCD`, and the refresh interval are parameters you program into the controller you design; set them to what the backing can meet and no legal command stream — peak streaming, row-miss floods, prefetch — can be served late. Correctness reduces to two paper checks: an *encodable* read latency and a *schedulable* refresh budget. (First-principles derivation: `strata_v_design.html` Part II.)
- **Functionally it's a strict superset** of the memory it replaces (every operation + 64× the capacity). The one inherent cost is a ~10–30% latency premium that bites *only* latency-bound, low-parallelism (CPU-style) access — which GPUs, and MoE inference, structurally don't run.
- **Serving a frontier model is a memory-*capacity* economy.** The model is a fixed cost paid once; each concurrent 1M-token user adds only ~28 GiB of KV cache. So cost-per-user *falls* as the shared memory pool grows — and capacity is the one axis where HBM/GDDR7 are worst and DDR5 is best. That is the whole market case for the converter, now quantified against NVIDIA's own B200 / GB200 serving hardware (doc 6).

## Sources

The datasheets, standards, and papers these studies rest on are **not redistributed
here** (many are vendor-copyrighted). Their source URLs are listed in
[`SOURCES.md`](SOURCES.md) — download from the original hosts.

## Provenance

Authored collaboratively with Claude (Anthropic) as an engineering thought-experiment.
No hardware was built; all figures are computed or cited, and open questions are
flagged in each document. No license is asserted — treat as all-rights-reserved unless
a `LICENSE` is added.
