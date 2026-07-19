Title: UMI: Extending Chiplet Interconnect Standards To Deal With The Memory Wall

URL Source: https://semiengineering.com/umi-extending-chiplet-interconnect-standards-to-deal-with-the-memory-wall/

Published Time: 2024-10-14T17:56:26+00:00

Markdown Content:
With the Open Compute Project (OCP) Summit upon us, it’s an appropriate time to talk about chiplet interconnect (in fact the 2024 OCP Summit has a whole day dedicated to the multi-die topic, on October 17). Of particular interest is the Bunch of Wires (BoW) interconnect specification that continues to evolve.

At OCP there will be an update and working group looking at version 2.1 of BoW. (That will be at 9:45 a.m. on Thursday, October 17, followed later that day by an overview of a solution called the Universal Memory Interface that can be added to BoW to specifically target the growing memory wall challenge facing multi-die design.) We believe all memory-bound SiP designs can benefit from advantages offered by UMI. Here’s why it’s important:

**The growing memory wall challenge in the AI Era**

 While the improvements in processor performance to enable the incredible compute requirements of applications like Chat-GPT get all the headlines, a not-so-new phenomenon known as the memory wall risks negating those advancements. Indeed, it has been clearly demonstrated that as CPU/GPU performance increases, wait time for memory also increases, preventing full utilization of the processors.

With the number of parameters in the generative AI model ChatGPT-4 reportedly close to 1.4 trillion, artificial intelligence has powered head-on into the memory wall. Other high-performance applications are not far behind. The rate at which GPUs and AI accelerators can consume parameters now exceeds the rate at which hierarchical memory structures, even on multi-die assemblies, can supply them. The result is an increasing number of idle cycles while some of the world’s most expensive silicon waits for memory.

Traditionally there have been three ways to pry open this bottleneck.

The easiest—in the days when Moore’s Law was young—was to make faster DRAM chips with faster interfaces. Today that well is dry.

The second approach has been to create a wider pathway between the memory array—which can produce thousands of bits per cycle in parallel—and the processor die. Arguably this has been taken near its practical limit with the 1 kbit-wide high-bandwidth memory (HBM) interface.

The third alternative is to use parallelism above the chip level. Instead of one stack of HBM dies, use four, or eight, each on its own memory bus. In this way the system architect can expand not just the amount of memory directly connected to a processing die, but also the bandwidth between memory and the compute die.

**Advanced packaging solutions**

 Recent solutions employing advanced packaging such as silicon interposers and silicon bridges have been trying to address these problems. Silicon interposers are the main substrate used today, proven in volume production. Further, interposers offer high Die2Die bandwidth with a single set of masks (easing alignment across the interposer), and with a CTE (coefficient of thermal expansion) that matches the chiplets, minimizing warpage issues.

The trouble is, these approaches are running into two hard limits, both involving real estate. Interposers are limited in size to ~3 reticles, thus limiting the size and performance of SiP devices that can be built. At the SiP level, there is no room left for more memory. We are already filling the largest available silicon interposers. Making room for more memory would mean leaving out some computing dies.

At the die level there is a different issue. Computing dies—whether CPU, GPU, or accelerator—are prime real estate, usually built in the most advanced and expensive process technology available. Designers want all that die area for computing—not for interfaces. They are reluctant to give up any of it, or any of their power budget, for additional memory channels.

More recently, silicon bridges are being utilized to build much larger substrates (4-10 reticles) that enable higher-performance systems. However, the need to achieve micron-level alignment across 100mm substrates is a very difficult task. And, the CTE mismatch between the substrates containing the bridges with the chiplets attached leads to warpage issues.

**Real estate crunches**

 Thus the dilemma. Architects need the added memory bandwidth and capacity that more memory channels can bring. But they are out of area on silicon interposers. And compute designers don’t want to surrender more die area for interfaces.

While silicon interposers and silicon bridges offer the bandwidth potential needed, standard packaging needed to be considered given the above-mentioned challenges. In fact, standard packaging is a preferred option in many scenarios where cost, stability and availability are issues. The dilemma with this option has been in getting the required bandwidth from using this packaging approach.

Fortunately, there is a solution, especially when it comes to the periphery chiplets, such as memory chiplets.

**A novel inter-die interface**

 Rather remarkably, one new proposal employing proven technology can relieve both the substrate-level and the die-level real-estate issues. And this, in turn, can push open the memory bottleneck. That technology is the Universal Memory Interface, or UMI. UMI™ is a high-speed, packetized data lane-based interface similar to UCIe or the Open Compute Project’s Bunch of Wires (BoW) standard. In fact, as UMI’s developer we know that UMI is a straightforward extension to BoW.

There are key differences between UMI and these earlier technologies, though. These differences make possible interposer-level speeds across standard organic substrates, a significant reduction in the compute die area given over to memory interfaces, and large potential improvements in both interconnect speed and power.

**The NuLink PHY**

 NuLink PHY, an Eliyan IP product, was the original PHY that BoW was based on. Being an extension of BoW, UMI gains its unique advantages from an improved version of NuLink PHY.

While most PHY IP used for inter-die communication is optimized for advanced packaging substrates like silicon interposers, the NuLink PHY is designed to not only operate over advanced packaging but also deliver full data rate across the very different and more challenging electrical environment of standard organic substrates — over distances up to several centimeters. This has important implications for memory-bound systems.

First, the ability to use organic substrates, at least for connectivity to the periphery chiplets with lower bandwidth requirements, opens up space. The largest silicon interposer currently in production measures ~2,700mm². Standard organic substrates can be up to four times that size. This allows designers to put more HBM stacks in the SiP, increasing memory capacity and parallelism. There may be room for more big computing dies as well.

Those two or three centimeters of range also has a vital benefit. Typically, memory stacks will be placed abutting the compute dies they serve, in order to get the best possible data rates through existing interfaces. But not only does this restrict layouts rather severely, it also creates strong thermal coupling between the notoriously hot compute die and the notoriously heat-sensitive HBM dies, introducing a serious failure mode for the entire system.

Greater range relaxes layout constraints for both die and substrate. And it allows separation between compute dies and HBM stacks, allowing compute circuitry to run at its maximum speed without overheating the delicate memory.

**Reversable data lanes**

 Just as significant for interfacing to memory is another function of the NuLink PHY leveraged UMI: dynamically reversable data lanes. Common memory interfaces such as DDR DRAM and HBM use reversable data channels, switching back and forth between read and write modes. But today’s inter-die interface specifications transferring data packets define only unidirectional lanes.

This means that today’s interfaces must devote two lanes to each memory channel: one for read, and a second for write. And that means significantly more precious substrate interconnect capacity must go to memory interfaces. UMI, in contrast, assigns one reversable lane to each reversable memory lane—a savings of a factor of two for data lanes. In addition, unlike the existing Die2Die standards with fixed data lanes (e.g. 16, 32, 64), UMI allocates proper necessary number of lanes for control and address signals for a given number of data lanes, thus maximizing the efficient lane usage. As a result, UMI achieves more than 2x efficiency compared to the other standard Die2Die interfaces.

**Speed and power**

 In addition to these points, the NuLink PHY gives UMI the benefits of its advanced architecture and circuit designs. Roughly, in the same environment and process technology NuLink can operate at twice the bandwidth and the power efficiency of alternative solutions. It is not necessary to elaborate on the significance of those figures to system designers.

Finally, it should be pointed out that, despite the name, nothing in the UMI specification limits it to use between compute dies and memory dies. UMI lanes can be configured to support fixed transmit and receive functions and therefore used as general-purpose inter-die interconnect.

Exploiting the NuLink PHY, UMI brings a host of advantages to designers of multi-die SiPs that are facing the memory wall. These include multicentimeter range at full speed over organic substrates, freeing designers from the high cost, size limits, and crowding of silicon interposers; switched bidirectional data lanes to slash the size of most memory interfaces; and inherent high speed at low power compared to the alternatives.
