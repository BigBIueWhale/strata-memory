Title: OpenAI Patent Reveals Custom AI Chip With 20 HBM Stacks, Using Intel EMIB-Style Bridges to Smash Current Limits

URL Source: https://wccftech.com/openai-patent-custom-ai-chip-hbm-memory-stacks-using-intel-emib-like-bridges/

Published Time: 2026-04-22T09:50:10+00:00

Markdown Content:
OpenAI has published a new patent in which it discloses an [AI chip](https://wccftech.com/openai-broadcom-ai-chips-partnership/) housing several compute chiplets, surrounded by a large number of HBM memory stacks.

## One Compute Chiplet, Several HBM Memory Stacks: This Could Be OpenAI's Future AI Chip Plans

In a new patent titled "[Non-Adjacent Connection of High-Bandwidth Memory Chiplets, I/O Chiplets, And Compute Chiplets Through Embedded Logic Bridges](https://patentscope.wipo.int/search/en/WO2026075822)", OpenAI shares plans for an AI chip solution that is going to house several HBM chiplets and compute chiplets, all connected using Embedded Logic Bridges.

The research proposes the idea of leveraging these embedded logic bridges for high-speed interconnects between longer distances, enabling more chiplets to connect together to support high-performance computing and AI workloads which require access to large amounts of memory for efficient operation.

Current packaging solutions have certain limitations regarding HBM integration as [HBM memory](https://wccftech.com/sk-hynix-answers-hbm-shortage-with-a-32-soccer-field-mega-fab-pt7-dedicated-to-hbm/) communicates with other chiplets on the package using metal wires on the base layer. The current JEDEC standard requires HBM memory to be placed adjacent to the compute chiplet, and there are physical limitation with this approach since the metal wires are required to be less than 6mm in length from the PHY controller on the main chiplet itself.

[![Image 1: A technical drawing labeled 'Fig. 2A' shows an interconnected array of components numbered 210, 214, and 216 with an identifier 'WO 2026/075822' at the top.](https://cdn.wccftech.com/wp-content/uploads/2026/04/OpenAI-AI-Chips-HBM-Memory-Intel-EMIB-_2.jpg)](https://cdn.wccftech.com/wp-content/uploads/2026/04/OpenAI-AI-Chips-HBM-Memory-Intel-EMIB-_2.jpg)[![Image 2: A diagram labeled 'FIG. 2B' shows a semiconductor design with components marked as 'HBM 204,' 'HBM 208,' and 'SUBSTRATE 218' connected by various pathways with identifiers like '216,' '210,' and '214.'](https://cdn.wccftech.com/wp-content/uploads/2026/04/OpenAI-AI-Chips-HBM-Memory-Intel-EMIB-_1.jpg)](https://cdn.wccftech.com/wp-content/uploads/2026/04/OpenAI-AI-Chips-HBM-Memory-Intel-EMIB-_1.jpg)

To overcome this limitation, the OpenAI patent proposes the use of embedded logic bridges, which can extend the distance of 6mm to 16mm. These bridges have two advantages: they not just enable longer communication distances, but they can also provide functionality of a controller for the HBM stack, or provide the functionality of a high-speed PHY for communicating between the chiplets within a package. This D2D (Die-to-Die) interface complies with the UCIe (Universal Chiplet Interconnect Express) standard.

In an example, OpenAI showcases a compute chiplet with 20 HBM memory stacks using the Embedded Logic Bridges. With traditional approaches, you are limited to four, six, or eight stacks. This scales up the memory capacity significantly, leading to chips that are potent for larger AI models.

[![Image 3](https://cdn.wccftech.com/wp-content/uploads/2026/04/Gaijin-april-2026.jpg)](https://bit.ly/4vqf38A)

[![Image 4](https://cdn.wccftech.com/wp-content/uploads/2026/04/gaijin-april.jpg)](https://bit.ly/41WmRSJ)

[![Image 5: A schematic diagram labeled 'WO 2026/075822' and 'PCT/US2025/047003' shows an arrangement of 'MEMORY STACKS 104' centered around a 'COMPUTE CHIPLET 102'.](https://cdn.wccftech.com/wp-content/uploads/2026/04/OpenAI-AI-Chips-HBM-Memory-Intel-EMIB-_3.jpg)](https://cdn.wccftech.com/wp-content/uploads/2026/04/OpenAI-AI-Chips-HBM-Memory-Intel-EMIB-_3.jpg)
But this research also goes hand in hand with a technology that someone is already working on. That's [Intel's EMIB or Embedded Multi-Interconnect Bridge solution](https://wccftech.com/intel-says-emib-is-better-than-2-5d-chips-cost-savings-simple-to-design-more-flexible/). EMIB is an advanced packaging solution that acts like a bridge.

It is designed to tackle the 2.5D packaging tech, leveraging tiny bridges to expand the capabilities and designs of high-performance chips. EMIB and its successor, EMIB-T, have various advantages, they are simple, they are small, they expand beyond the reticle limits of current interposers, and the are cost effective solutions.

[![Image 6: An Intel presentation slide titled 'A True Packaging Breakthrough' compares the 'Industry Standard' and 'EMIB' configurations, highlighting improved die placement flexibility with 'EMIB.'](https://cdn.wccftech.com/wp-content/uploads/2026/01/Intel-EMIB-vs-2.5D-Advanced-Packaging-Solutions-_1-scaled.png)](https://cdn.wccftech.com/wp-content/uploads/2026/01/Intel-EMIB-vs-2.5D-Advanced-Packaging-Solutions-_1-scaled.png)
Can we see a future where [Intel's EMIB technology](https://wccftech.com/intel-emib-challenges-tsmcs-cowos-as-america-answer-to-the-ai-packaging-bottleneck/) gets used by OpenAI for the creation of its custom AI chips with many chiplets and large amounts of HBM memory? Well, this patent seems be pointing towards that.

News Source: [SETI Park](https://x.com/seti_park/status/2046798010559217780)

[![Image 7: Hassan Mujtaba Photo](https://cdn.wccftech.com/wp-content/uploads/2016/09/Hassan.jpg)](https://wccftech.com/author/hms/)

**About the [author](https://wccftech.com/author/hms/):** A Software Engineer by training and a PC enthusiast by passion, Hassan Mujtaba serves as Wccftech's Senior Editor for [hardware](https://wccftech.com/topic/hardware/) section. With years of experience in the industry, he specializes in deep-dive technical analysis of next-generation CPU and GPU architectures, motherboards, and cooling solutions. His work involves not only breaking news on upcoming technologies but also extensive hands-on reviews and benchmarking.

Follow [Wccftech on Google](https://profile.google.com/cp/Cg0vZy8xMWM3NDB2MmIyGgA) to get more of our news coverage in your feeds.
