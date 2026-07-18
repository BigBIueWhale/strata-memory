# STRATA-2T — primary source PDFs

All files verified as real PDFs (`%PDF` magic). Downloaded 2026-07-18. Backing the design in `../strata_2t_design.html`.

## Fast tier (GDDR7) + compute die
| File | Why |
|---|---|
| `micron-gddr7-product-brief.pdf` | GDDR7 device truth: 266-ball FBGA 12×14×1.1 mm, 0.75 mm pitch, 4×(8+2) channels, ×32, clamshell=Yes, 1.2 V, 28/32/36 Gb/s, 4.5 pJ/bit. MPN decode → `MT68A768M32DF-28-A` (24 Gb). |
| `nvidia-rtx-pro-6000-ws-datasheet.pdf` | The existence proof for the fast tier: 96 GB GDDR7 ECC / 512-bit / 1792 GB/s / 600 W. |
| `nvidia-rtx-blackwell-pro-architecture.pdf` | GB202 memory-subsystem architecture detail. |
| `achronix-gddr6-ug091-si-electrical.pdf` | Best public SI/electrical numbers: R_ON 40/48/60 Ω, ODT 60/120/240 Ω, ZQ, WCK2CK/read/write/CA training, POD (GDDR6, applies closely to GDDR7). |
| `arxiv-2410.12990-pam3-ddr-signal-integrity.pdf` | PAM3 DRAM-bus SI physics — ISI/skin/dielectric loss, PAM3-vs-PAM4 margin; the "why short point-to-point" citation. |

## Bulk tier (DDR5) + registering
| File | Why |
|---|---|
| `unisemicon-ddr5-rdimm-288pin-mechanical.pdf` | 288-pin DDR5 RDIMM datasheet with package/mechanical drawing (133.35 × 31.25 mm). |

*(RCD/DB/MRDIMM part numbers — Renesas RG5R364/RRG50120, Montage M88DR5RCD03 — and the Samsung/Micron 256 GB PNs are cited inline in the design doc; their vendor pages are HTML, not downloadable PDFs. Micron 128 GB RDIMM brief and the module reference guide are additional DDR5 sources noted in the research.)*

## Coherence / tiering / precedent
| File | Why |
|---|---|
| `nvidia-grace-hopper-architecture-whitepaper.pdf` | The precedent: 900 GB/s C2C, cache-coherent two-NUMA-node HBM+LPDDR model = STRATA-2T's GDDR7+DDR5 blueprint. |
| `arxiv-2411.02814-hitchhikers-cxl-c2c-infinity.pdf` | One-methodology measurements of GH200 + MI300A + CXL — the cross-precedent. |
| `arxiv-2407.07850-grace-hopper-measured.pdf` | Measured C2C 375/297 GB/s, access-counter migration, page-size effects. |
| `cxl-3.0-whitepaper.pdf` | CXL coherence/back-invalidation — the rejected bulk-attach alternative (latency rationale). |
| `arxiv-2206.02878-tpp-memory-tiering.pdf` | Meta TPP: memory-tier latency table + 22%→90% hot-page hit rate. |
| `amd-mi300a-datasheet.pdf` | 128 GB unified HBM + LGA-6096 — the ~6,000-contact package existence proof. |

## Workload (Kimi / MoE / MLA KV cache)
| File | Why |
|---|---|
| `arxiv-2507.20534-kimi-k2-technical-report.pdf` | Kimi K2 specs: 1.04T/32.6B active, 61 layers, 384 experts, MLA, 128K. |
| `arxiv-2405.04434-deepseek-v2-mla-kvcache.pdf` | The MLA KV-cache formula (576 elem/token/layer) — the 28× correction vs MHA. |

## Physical / packaging
| File | Why |
|---|---|
| `ocp-oam-design-spec-v1p0.pdf` | OAM module: 102×165 mm, Mirror Mezz, ≤700 W/48 V — the chosen form factor. |
| `pcie-cem-r3.0-card-mechanical.pdf` | PCIe card envelope (111.15 mm height) — proves a 133 mm DIMM can't ride a card. |

## Reference photos (`../images/`)
- `Nvidia-RTX-6000D-*.jpg` — clamshell PCB teardown (front die + back-side memory) confirming 16+16 layout.
