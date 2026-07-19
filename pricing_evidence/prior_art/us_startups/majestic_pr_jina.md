Title: Majestic Labs Announces Prometheus: The First AI Server Purpose-Built to Break the Memory Wall

URL Source: https://www.01net.it/majestic-labs-announces-prometheus-the-first-ai-server-purpose-built-to-break-the-memory-wall/

Published Time: 2026-04-28T19:17:00+00:00

Markdown Content:
_Majestic’s memory-first AI servers combine efficiency, ease of programming, and a groundbreaking memory system to collapse racks of standard servers into a single Majestic server_

SAN FRANCISCO & TEL AVIV, Israel--(BUSINESS WIRE)--Majestic Labs today unveiled Prometheus, the first AI server designed from the ground up to tackle the memory wall: the most critical obstacle to the advancement and deployment of AI models. Leveraging an innovative architecture and a complete software stack, the server connects orders of magnitude more memory to each processor, at unprecedented bandwidth, achieving performance equivalent to multiple racks in a single ultra-efficient unit. The resulting improvement in power efficiency and total cost of ownership is unprecedented.

[![Image 1](https://mms.businesswire.com/media/20260428206091/en/2787556/22/Majestic_Labs_logo.jpg)](https://mms.businesswire.com/media/20260428206091/en/2787556/5/Majestic_Labs_logo.jpg)

[![Image 2](https://mms.businesswire.com/media/20260428206091/en/2787556/21/Majestic_Labs_logo.jpg)](https://mms.businesswire.com/media/20260428206091/en/2787556/5/Majestic_Labs_logo.jpg)

AI infrastructure has reached an inflection point where the biggest bottleneck for scaling AI workloads is no longer compute—it is memory. The continuing growth of models, datasets, and context windows is driving an unsustainable buildout of data centers. The top five hyperscalers alone spent [$443 billion](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fwww.cnbc.com%2F2025%2F12%2F31%2Fai-data-centers-debt-sam-altman-elon-musk-mark-zuckerberg.html&esheet=54524672&newsitemid=20260428206091&lan=en-US&anchor=%24443+billion&index=1&md5=6e64202069b0d6670ccf24db3b95bbf0) in capital expenditures in 2025, a figure that is expected to climb 36% to $602 billion in 2026. Over 75% of that investment will be directed toward AI infrastructure. Yet global energy infrastructure cannot support this buildout without significant efficiency gains.

The AI industry has spent years in an arms race for more powerful GPUs, with leading chip manufacturers competing on compute performance. But this focus has created a critical blind spot: processors are burning gigawatts of power while heavily underutilized as they wait for data from memory. Furthermore, that memory is fragmented and spread across hierarchies of CPUs, GPUs, switches, servers, and racks, which makes the software incredibly complex and those systems highly inefficient to deploy.

Majestic’s AI server, Prometheus, rebalances this equation and kicks off a new efficiency race focused on memory. Designed by the team that built and shipped hundreds of millions of custom chips at Google and Meta, Prometheus connects 1000x more high-speed, power-efficient memory at ultra-high bandwidth to each processor in the server. Prometheus is configurable with a maximum memory capacity of 128 TB per standard-size server. The entire memory space is uniform, shared and contiguous, connected at full bandwidth to all processing elements.

“_In the early days of AI, the industry ran workloads on machines that were never actually built for AI._” said**Sha Rabii, Co-Founder and President of Majestic Labs**. “_The industry can no longer afford the compromise in efficiency that results from this ill-fitting pairing considering_ _the scale that AI is reaching today. AI is here to stay and it fundamentally requires three critical elements: memory for huge workloads, high-efficiency vector/tensor processors, and tightly coupled high performance CPUs for algorithmic control and pre- and post-processing._”

_"Prometheus represents the first ground-up reimagination of AI infrastructure with memory as a first-class citizen,"_ added **Ofer Shacham, Co-Founder and CEO of Majestic Labs**_. “AI brains become better with larger model and context sizes and when multi-modalities work in tandem. Bigger truly is better in this context. We built Prometheus to remove capacity and bandwidth limits so organizations can deploy sophisticated AI systems that were previously impractical, if not impossible, to run at scale.”_

Inside, Prometheus carries proprietary AI Processing Units (AIUs) named Ignite. Ignite focuses on enabling AI researchers and software developers. Majestic’s fully programmable system supports industry-standard frameworks, including PyTorch, vLLM, and OpenAI’s Triton, allowing developers to deploy their existing code without any changes. “_After over a decade of collaboration with internal developers and researchers working at the intersection of AI algorithms and custom silicon at Google and Meta, we learned that when customers have to choose between performance and productivity, they choose productivity.”_ said**Masumi Reynders, Co-Founder and Chief Operating Officer**. “_The system just has to work, with no switching cost. Part of our North Star has been ‘Day 1 productivity’, and our focus has not wavered._”

Ignite is the first chip multiprocessor of its kind built around a unique memory-first architecture. It is a holistic processor that combines datacenter-class ARM application cores with the most efficient RISC-V vector and tensor cores, all on the same silicon and in the same memory space.

Prometheus is the first commercial system capable of running the most advanced multi-trillion-parameter models in one server, enabling organizations to deploy LLMs with massive context windows of hundreds of millions of tokens, complex mixture-of-experts models, agentic AI systems, graph neural networks and tabular models that cannot run efficiently on conventional GPU-based infrastructure. The architecture is designed to accommodate emerging kernels, networks, and frameworks as AI continues to evolve. With Prometheus, companies will be able to deploy these sophisticated AI workloads at a fraction of the power consumption and TCO.

_"As AI models continue to grow in scale and complexity, memory bandwidth has emerged as a critical bottleneck," said **Jason Bennett, VP and Global Head of Startups and Venture Capital at AWS**. "We are excited that Majestic Labs has chosen AWS to help them reimagine AI infrastructure from the ground up. Their focus on memory-first architecture represents the kind of innovative thinking the industry needs as we work toward more efficient AI systems."_

**The Name Behind the Server**_“We were inspired by Prometheus, the Titan in Greek mythology who brought fire from the gods and gave it to humanity. At Majestic Labs, we have a parallel mission. Our Prometheus server brings the most efficient and advanced AI infrastructure to any organization ready to use it, and we want it to light up the world,”_ said **Reynders**, explaining the origin of the product’s name.

_“To design Prometheus, we couldn't optimize our way around the memory wall with incremental improvements,”_ said **Rabii. _“_**_We had to reimagine the entire architecture from first principles, putting memory first and building everything else around it. The name reflects that ground-up and almost defiant design philosophy.”_

Prometheus is in development for early customers with wide availability expected next year. Organizations interested in learning more can visit [www.majestic-labs.ai](https://cts.businesswire.com/ct/CT?id=smartlink&url=http%3A%2F%2Fwww.majestic-labs.ai&esheet=54524672&newsitemid=20260428206091&lan=en-US&anchor=www.majestic-labs.ai&index=2&md5=2adf1917ad200e4c9d4979562b3c8177).

**About Majestic Labs**Majestic Labs builds power-efficient AI servers for the largest and most advanced AI workloads. The company's flagship server architecture collapses multiple racks of conventional equipment into a single server. Majestic's system features custom accelerator and memory interface chips that connect immense amounts of memory to compute, enabling up to 128 TB of high-speed, power-efficient, high-bandwidth memory per server, and nearly 1000 times more memory to each processor than today's leading GPUs. This memory-first approach allows organizations to run massive AI models while dramatically reducing power consumption, data center footprint, and infrastructure costs. Majestic Labs' mission is to democratize access to the most advanced AI capabilities and reduce the environmental impact of AI infrastructure.

**Contacts**

**Media Contact**

[Majestic@deeptech.agency](mailto:Majestic@deeptech.agency)
