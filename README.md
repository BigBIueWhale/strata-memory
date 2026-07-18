# STRATA — custom-silicon designs for scaling GPU memory

Three linked engineering **decision records** exploring one question:

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

## The through-line (what the three docs establish)

- **Pins buy bandwidth; capacity is depth.** They're independent axes — `bandwidth ≈ pins × per-pin rate`, capacity is how much DRAM sits behind the pins.
- **1.79 TB/s is a *low* bandwidth.** It's ~18 MRDIMM channels or ~35 DDR5-6400 channels — reachable with cheap, deep commodity DRAM, no GDDR7 required.
- **At multi-TiB scale, bandwidth is nearly free.** 2 TiB of commodity DDR5 already contains multiple TB/s of latent parallelism; a converter just exposes the slice you want.
- **A converter can front cheap-and-deep DDR5 as a fast, huge virtual device** — the catch is a fixed ~5–10% latency tax and a hard requirement that the backing stay *deterministic* (a fixed-beat memory protocol has no "please wait").
- **You can't retrofit this onto a shipped GPU** — GDDR7 has no capacity-expansion signaling, the timing is training-frozen, and 28 Gb/s PAM3 can't leave the board. Integration is *design-in*, not *bolt-on*.
- **It provably serves on time — because you *author* the deadline, not race it.** `CL`, `tRCD`, and the refresh interval are parameters you program into the controller you design; set them to what the backing can meet and no legal command stream — peak streaming, row-miss floods, prefetch — can be served late. Correctness reduces to two paper checks: an *encodable* read latency and a *schedulable* refresh budget. (First-principles derivation: `strata_v_design.html` Part II.)
- **Functionally it's a strict superset** of the memory it replaces (every operation + 64× the capacity). The one inherent cost is a ~10–30% latency premium that bites *only* latency-bound, low-parallelism (CPU-style) access — which GPUs, and MoE inference, structurally don't run.

## Sources

The datasheets, standards, and papers these studies rest on are **not redistributed
here** (many are vendor-copyrighted). Their source URLs are listed in
[`SOURCES.md`](SOURCES.md) — download from the original hosts.

## Provenance

Authored collaboratively with Claude (Anthropic) as an engineering thought-experiment.
No hardware was built; all figures are computed or cited, and open questions are
flagged in each document. No license is asserted — treat as all-rights-reserved unless
a `LICENSE` is added.
