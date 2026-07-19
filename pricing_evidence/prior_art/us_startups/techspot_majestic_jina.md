Title: Former Google and Meta engineers build memory-first AI server to challenge Nvidia's GPU dominance

URL Source: https://www.techspot.com/news/112235-former-google-meta-engineers-build-memory-first-ai.html

Published Time: 2026-04-29T14:33:00-05:00

Markdown Content:
Serving tech enthusiasts for over 25 years. 

 TechSpot means tech analysis and advice [you can trust](https://www.techspot.com/ethics.html).

**First look:** A new generation of artificial intelligence systems is exposing a limitation that raw computing power alone cannot solve. As models scale into the trillions of parameters, memory – its size, speed, and proximity to compute – has become the primary constraint. A startup founded by former Google and Meta engineers is betting that rethinking this balance from the ground up will make very large models cheaper and easier to run.

[Majestic Labs AI](https://majestic-labs.ai/), founded by Ofer Shacham, Masumi Reynders, and Sha Rabii, has [developed](https://www.wsj.com/tech/chip-startup-aims-to-shatter-ais-dreaded-memory-wall-b5f4c563) a server architecture built around what it describes as a memory-first design. The company, which raised $100 million in November from investors including Bow Wave Capital, Lux Capital, and Grove, is targeting one of the most persistent bottlenecks in modern AI systems: the so-called "memory wall."

That bottleneck emerges when high-performance processors sit idle while waiting for data to move between chips. As models grow larger, these delays add up and blunt the gains from faster hardware. Rabii told The Wall Street Journal that at extreme scales, "the best-quality models are becoming increasingly commercially not viable using existing infrastructure."

Majestic's answer is a new server system called Prometheus, built around a proprietary chip it calls an AIU, or artificial intelligence processing unit. Rather than prioritizing raw compute density, the system is designed to pair processors with significantly larger pools of memory.

According to the company, its architecture delivers up to 1,000 times the memory capacity of competitors' GPU-based systems, such as Nvidia's.

Each Prometheus server can be configured with up to 128 terabytes of high-speed memory. That capacity, Majestic says, is sufficient to run models with 5 to 10 trillion parameters without the sharding and memory wait times that slow today's systems. The exact configuration can be adjusted depending on customer requirements.

"This is the first time that a processor for AI is actually designed around memory first, with these amounts of memory that are required to handle the biggest models," Shacham said.

![Image 1](https://www.techspot.com/images2/news/bigimage/2026/04/2026-04-29-image-34.jpg)

The company's approach comes as demand for inference continues to surge. The rise of agentic AI systems, which autonomously execute tasks such as writing code or coordinating workflows, has intensified pressure on compute infrastructure. That demand has pushed up rental prices for advanced chips and in some cases, led to service slowdowns or usage caps.

Large incumbents and well-funded startups alike are racing to address the same problem. AMD has positioned its latest chips for inference workloads, while Nvidia has doubled down on the segment, including a $20 billion deal tied to Groq's inference technology and the hiring of members of its leadership team.

Google Cloud recently introduced a new generation of TPUs that separates training and inference functions while emphasizing high-bandwidth memory. Cerebras, another player focused on inference-scale hardware, has expanded its footprint through a deal with Amazon Web Services and filed to go public earlier this month.

Majestic's founders argue that these approaches still fall short in terms of memory capacity, forcing customers into inefficient trade-offs. Buyers often need to purchase excess compute just to access sufficient memory. "The analogy is, I need a new garage, and you tell me I have to buy a new house," Rabii said.

[![Image 2](https://www.techspot.com/images2/news/bigimage/2026/04/2026-04-29-image-20.jpg)](https://www.techspot.com/images2/news/bigimage/2026/04/2026-04-29-image-20.jpg)

Instead of relying on high-bandwidth memory, which is more complex and supply-constrained due to its three-dimensional stacking process, Majestic uses commodity DRAM. The company pairs that choice with proprietary interconnect technology designed to move data at speeds that, it claims, exceed HBM while consuming less power. That combination is intended to sidestep ongoing supply constraints that manufacturers expect to persist into next year and beyond.

Despite those constraints, Majestic says it has already secured multiple customers, with projected deals totaling hundreds of millions of dollars in revenue beginning in 2027. The company has not disclosed the identities of those customers, citing confidentiality.

Operating out of a modest office in Los Altos, the team is attempting to reshape a core assumption in AI hardware design: that compute should come first. If the design holds up in production, AI infrastructure could begin to be defined more by memory capacity than by raw compute.
