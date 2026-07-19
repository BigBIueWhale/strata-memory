> ## Documentation Index
> Fetch the complete documentation index at: https://inference-docs.cerebras.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dedicated Endpoints

> Deploy private, high-performance inference endpoints for enterprise workloads.

A dedicated endpoint is a private, provisioned instance of the Cerebras Inference service reserved exclusively for your organization. Your traffic runs on reserved capacity, ensuring latency and throughput are not affected by other users.

Dedicated endpoints are intended for production workloads that require predictable performance—such as real-time applications, customer-facing products, and high-volume pipelines that need guaranteed capacity. See supported models [here](#supported-models).

**Key Benefits**

<AccordionGroup>
  <Accordion title="Dedicated capacity">
    Your endpoint runs on reserved capacity that is not shared with other customers, so your performance is never impacted by other workloads.
  </Accordion>

  <Accordion title="Consistent latency and throughput">
    Performance is reserved and predictable, even under load.
  </Accordion>

  <Accordion title="Bring your own weights">
    Deploy your custom fine-tuned models alongside standard model variants.
  </Accordion>

  <Accordion title="Performance customization">
    Tailor your endpoint to match the performance and scale requirements of your workload through bespoke draft models, model configurations, and quantization strategies.
  </Accordion>

  <Accordion title="Exclusive access to advanced features">
    All capabilities available on shared endpoints are available on dedicated endpoints. In addition, dedicated customers get access to advanced features including fine-tuning, weight management, and enhanced service tier controls.
  </Accordion>
</AccordionGroup>

To get started with a dedicated endpoint, [contact us](https://www.cerebras.ai/contact).

## Supported Models

Dedicated endpoints support a broad range of model families, including multiple versions, parameter sizes, and weight variations (e.g., `-instruct` and `-thinking`) as well as your own custom weights. We can also work with you to tune your endpoint configuration to meet your specific performance goals.

<AccordionGroup>
  <Accordion title="Alibaba Qwen — Qwen3, Qwen3-Coder" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/qwen.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=5f17b5e6222779e638a8c283f8e511a8" width="16" height="16" data-path="images/icons/qwen.svg">
    **Qwen3-235B-A22B**

    * [Qwen/Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)
    * [Qwen/Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)

    **Qwen3-32B**

    * [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)

    **Qwen3-30B-A3B**

    * [Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
    * [Qwen/Qwen3-30B-A3B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507)

    **Small & Tiny Variants**

    * [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)
    * [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)
    * [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B)
    * [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)

    **Qwen3-Coder**

    * [Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)
    * [Qwen/Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
  </Accordion>

  <Accordion title="OpenAI (OSS) — GPT-OSS" icon="openai">
    * [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b)
    * [openai/gpt-oss-safeguard-120b](https://huggingface.co/openai/gpt-oss-safeguard-120b)
    * [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)
  </Accordion>

  <Accordion title="MiniMax — MiniMax M2.X" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/minimax.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=bb972b9e03b7f218e5d2776a141c29cb" width="24" height="24" data-path="images/icons/minimax.svg">
    * [MiniMaxAI/MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)
    * [MiniMaxAI/MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)
  </Accordion>

  <Accordion title="Google — Gemma 4" icon="google">
    * [google/gemma-4-31b-it](https://huggingface.co/google/gemma-4-31b-it)
  </Accordion>

  <Accordion title="Meta — Llama 3, Llama 4" icon="meta">
    * [meta-llama/Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) (402B total)
    * [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) (109B total)
    * [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)
  </Accordion>

  <Accordion title="Mistral — Mistral Small, Mistral Large 3, Devstral 2, Mixtral" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/mistralai.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=5e1e79f16460060e9825edacec580636" width="24" height="24" data-path="images/icons/mistralai.svg">
    * [mistralai/Mistral-Large-3-675B-Instruct-2512](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512)
    * [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)
    * [mistralai/Devstral-Small-2-24B-Instruct-2512](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)
    * [mistralai/Mathstral-7B-v0.1](https://huggingface.co/mistralai/Mathstral-7B-v0.1)
    * [mistralai/Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1)
  </Accordion>

  <Accordion title="Z.AI — GLM 4.X, GLM 5.X" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/zai.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=06535f5280d8d19ba786406c66be6cf4" width="24" height="24" data-path="images/icons/zai.svg">
    * [zai-org/GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)
    * [zai-org/GLM-5](https://huggingface.co/zai-org/GLM-5)
    * [zai-org/GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)
    * [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)
    * [zai-org/GLM-4.6](https://huggingface.co/zai-org/GLM-4.6)
    * [zai-org/GLM-4.5](https://huggingface.co/zai-org/GLM-4.5)
    * [zai-org/GLM-4.5-air](https://huggingface.co/zai-org/GLM-4.5-air)
  </Accordion>

  <Accordion title="Moonshot AI — Kimi K2.X" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/moonshot.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=580edaa8ea7ace796f411c7244dddb25" width="24" height="24" data-path="images/icons/moonshot.svg">
    * [moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)
    * [moonshotai/Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)
    * [moonshotai/Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct)
    * [moonshotai/Kimi-K2-Thinking](https://huggingface.co/moonshotai/Kimi-K2-Thinking)
  </Accordion>

  <Accordion title="DeepSeek — DeepSeek V3.X" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/deepseek.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=538f34c14c52d24010db84d0332cce36" width="16" height="16" data-path="images/icons/deepseek.svg">
    * [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2)
    * [deepseek-ai/DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1)
    * [deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3)
  </Accordion>

  <Accordion title="StepFun — Step 3.X Flash" icon="https://mintcdn.com/cerebras-inference/5JGSuJfumLWIlNYj/images/icons/stepfun.svg?fit=max&auto=format&n=5JGSuJfumLWIlNYj&q=85&s=37cf81dd7ac6789eb7017fc053d0e816" width="84" height="84" data-path="images/icons/stepfun.svg">
    * [stepfun-ai/Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash)
    * [stepfun-ai/Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)
  </Accordion>

  <Accordion title="ByteDance — OSS Seed" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/bytedance.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=d90cbc6eb08537be002ff8bcfe3d0ca6" width="24" height="24" data-path="images/icons/bytedance.svg">
    * [ByteDance-Seed/Seed-OSS-36B-Instruct](https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct)
  </Accordion>

  <Accordion title="ServiceNow — Apriel" icon="https://mintcdn.com/cerebras-inference/k52j3v9j3Q8jlYv7/images/icons/servicenow.svg?fit=max&auto=format&n=k52j3v9j3Q8jlYv7&q=85&s=9b7890d5d3b44e7363d4a70ca3b6b7b1" width="24" height="24" data-path="images/icons/servicenow.svg">
    * [ServiceNow-AI/Apriel-1.6-15b-Thinker](https://huggingface.co/ServiceNow-AI/Apriel-1.6-15b-Thinker)
  </Accordion>

  <Accordion title="Coming soon: multimodal" icon="photo-film">
    * Qwen3-VL
    * Kimi K2.6
    * Pixtral Large
  </Accordion>
</AccordionGroup>

## Features

Dedicated endpoints include all shared endpoints capabilities, plus:

* **Fine-tuning** — Deploy custom model weights on your dedicated endpoint.
* **[Management API](/dedicated/management-api)** — Programmatically manage models, capacity, and endpoints.
* **[Batch API](/capabilities/batch)** — Run large-scale asynchronous workloads against your reserved capacity.
* **[Service tiers](/capabilities/service-tiers)** — Configure request prioritization to match your SLA requirements.
* **[Metrics](/capabilities/metrics)** — Monitor your endpoint with Prometheus-compatible metrics for requests, tokens, latency, and health.

## Get Started

Dedicated endpoints are available to enterprise customers. [Contact us](https://www.cerebras.ai/contact) to discuss your requirements.
