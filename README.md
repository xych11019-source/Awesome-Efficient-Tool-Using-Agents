# 🤖 Efficient Tool-Using LLM Agents: Research Collection

<div align="center">

![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)
[![Papers](https://img.shields.io/badge/Papers-103-blue)](#-statistics--trends)
[![Years](https://img.shields.io/badge/Years-2021--2026-success)](#-statistics--trends)
[![Focus](https://img.shields.io/badge/Focus-Efficient%20Tool--Using%20Agents-purple)](#-overview)
[![PR](https://img.shields.io/badge/PRs-Welcome-red)](#-contributing)

</div>

## 🌟 Overview

<p align="center">   <img src="./figs/meta.png" width="90%" alt="Survey overview figure"> </p>

This repository contains a **curated collection** of papers on **efficient tool-using LLM agents**. 
The current bibliography focuses on the emerging shift from _capability-first_ agent design to _efficiency-aware_ agent design, covering:

- **tool learning and retrieval**
- **tool selection and decision policies**
- **planning and reasoning for tool use**
- **context compression and memory management**
- **parallel execution, speculative calls, and orchestration**
- **caching, serving, and systems optimization**
- **benchmarks and evaluation for agentic tool use**

## 📊 Statistics & Trends

- **Total papers:** 103
- **Time span:** 2021–2026
- **Peak publication year:** 2025 (50 papers)
- **Recent wave:** 2024–2026 contributes 92 papers

| Year | Count |
|------|------:|
| 2021 | 1 |
| 2022 | 2 |
| 2023 | 6 |
| 2024 | 21 |
| 2025 | 50 |
| 2026 | 21 |
| Unknown | 2 |

## 📑 Table of Contents

- [🌟 Overview](#-overview)
- [📊 Statistics & Trends](#-statistics--trends)
- [🧭 Paper-Aligned Taxonomy](#-paper-aligned-taxonomy)
  - [Efficient Tool Context](#-efficient-tool-context)
    - [Tool Set Compression](#-tool-set-compression)
    - [Tool Description Compression](#-tool-description-compression)
    - [History Compression](#-history-compression)
  - [Efficient Tool Calling](#-efficient-tool-calling)
    - [Eligibility-Aware Calling](#-eligibility-aware-calling)
    - [Cost-Aware Calling](#-cost-aware-calling)
  - [Efficient Tool Reasoning](#-efficient-tool-reasoning)
    - [Trajectory Optimization](#-trajectory-optimization)
    - [Reasoning Reuse](#-reasoning-reuse)
  - [Efficient Tool Execution](#-efficient-tool-execution)
    - [Results Caching](#-results-caching)
    - [Parallel Execution](#-parallel-execution)
    - [Speculative Execution](#-speculative-execution)
- [📚 Resource List](#-resource-list)
  - [Related Surveys & Foundations](#-related-surveys--foundations)
  - [Taxonomy-Aligned Reading Map](#-taxonomy-aligned-reading-map)
  - [Applications & Agent Systems](#-applications--agent-systems)
- [🤝 Contributing](#-contributing)

## 🧭 Paper-Aligned Taxonomy

This README is reorganized to match the **actual Overleaf source structure** of the paper rather than the noisy PDF extraction. The paper defines efficient tool-using LLM agents through four stages of the agent loop: **Efficient Tool Context**, **Efficient Tool Calling**, **Efficient Tool Reasoning**, and **Efficient Tool Execution**.

### 🔹 Efficient Tool Context
This stage minimizes the working context by optimizing the visible tool subset, tool schema representation, and interaction history.

#### Tool Set Compression
Focuses on reducing the visible tool subset so the model does not carry an unnecessarily large tool library into context.

#### Tool Description Compression
Focuses on compressing or deferring tool schemas while preserving invocation-critical fields such as tool names and parameters.

#### History Compression
Focuses on curating, summarizing, or extracting state from prior interaction history so long trajectories do not overwhelm the context window.

### 🔹 Efficient Tool Calling
This stage optimizes whether and when a tool should be invoked, primarily targeting unnecessary tool calls.

#### Eligibility-Aware Calling
Determines whether a tool call is actually warranted and feasible under the current request and context.

#### Cost-Aware Calling
Treats tool use as a utility-cost trade-off under explicit rewards, penalties, or budgets.

### 🔹 Efficient Tool Reasoning
This stage improves how the agent constructs trajectories, reducing redundant reasoning and repeated planning.

#### Trajectory Optimization
Uses structured search, planning, feedback, or policy refinement to build shorter and better reasoning trajectories.

#### Reasoning Reuse
Reuses prior procedural knowledge through plan caching or distills strong reasoning patterns into cheaper agents.

### 🔹 Efficient Tool Execution
This stage focuses on runtime efficiency after a tool action is decided, mainly targeting end-to-end latency.

#### Results Caching
Reuses previous tool outputs or execution state to avoid redundant execution.

#### Parallel Execution
Exposes concurrency across decoding and independent tool calls to reduce serialized waiting time.

#### Speculative Execution
Pre-executes likely future interactions and only keeps them if later reasoning validates those actions.

## 📚 Resource List

> Notes
> - arXiv links are added automatically when an arXiv identifier is present in the bibliography.
> - Entries without an explicit URL in the `.bib` are listed as plain titles.
> - The short focus lines below are lightweight title-based tags for quick browsing.

### 🧭 Related Surveys & Foundations

> Surveys, overviews, and seminal foundations for tool-using and agentic LLM systems.

- **[A survey on the optimization of large language model-based agents]（https://arxiv.org/abs/2503.12434**） (*2026*) `ACM Computing Surveys`
  
  > Focus: survey.
  
- **[Agent skills for large language models: Architecture, acquisition, security, and the path forward](https://arxiv.org/abs/2602.12430)** (*2026*) `arXiv`
  
  > Focus: foundations, agent systems.
  
- **[Toward Efficient Agents: Memory, Tool learning, and Planning](https://arxiv.org/abs/2601.14192)** (*2026*) `arXiv`
  
  > Focus: foundations, tool use, planning.
  
- **[Large language model agent: A survey on methodology, applications and challenges](https://arxiv.org/abs/2503.21460)** (*2025*) `arXiv`
  
  > Focus: survey.
  
- **[Survey on evaluation of llm-based agents](https://arxiv.org/abs/2503.16416)** (*2025*) `arXiv`
  
  > Focus: survey.
  
- **[Tool learning with large language models: A survey](https://arxiv.org/abs/2405.17935)** (*2025*) `FCS`
  
  > Focus: tool use, survey.
  
- **[A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?](https://arxiv.org/abs/2503.24235)** (*2025*) `arXiv`
  
  > Focus: survey.
  
- **[A survey on large language model based autonomous agents](https://arxiv.org/abs/2308.11432)** (*2024*) `FCS`
  
  > Focus: survey.
  
- **[Large language model based multi-agents: A survey of progress and challenges](https://arxiv.org/abs/2402.01680)** (*2024*) `arXiv`
  
  > Focus: survey.

## 🧩 Taxonomy-Aligned Reading Map

### 🔹 Efficient Tool Context

#### 🔧 Tool Learning, Retrieval & Selection

> Methods for tool learning, API grounding, tool discovery, retrieval, and selection.

- **[AutoTool: Efficient tool selection for large language model agents](AutoTool: Efficient tool selection for large language model agents)** (*2026*) `AAAI`
  
  > Focus: tool selection.
  
- **[SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?](https://arxiv.org/abs/2603.00718)** (*2026*) `arXiv`
  
  > Focus: tool use.
  
- **[A joint optimization framework for enhancing efficiency of tool utilization in llm agents](https://aclanthology.org/2025.findings-acl.1149/)** (*2025*) `ACL`
  
  > Focus: tool use.
  
- **[Budget-aware tool-use enables effective agent scaling](https://arxiv.org/abs/2511.17006)** (*2025*) `arXiv`
  
  > Focus: tool use.
  
- **[Dynamic react: Scalable tool selection for large-scale mcp environments](https://arxiv.org/abs/2509.20386)** (*2025*) `arXiv`
  
  > Focus: tool selection, MCP.
  
- **[Dynamic Tool Dependency Retrieval for Efficient Function Calling](https://arxiv.org/abs/2512.17052)** (*2025*) `arXiv`
  
  > Focus: tool use, function calling.
  
- **[Easytool: Enhancing llm-based agents with concise tool instruction](https://arxiv.org/abs/2401.06201)** (*2025*) `ACL`
  
  > Focus: tool use.
  
- **[Less is more: Optimizing function calling for llm execution on edge devices](https://arxiv.org/abs/2411.15399)** (*2025*) `DATE`
  
  > Focus: function calling, edge deployment.
  
- **[SMART: Self-aware agent for tool overuse mitigation](https://arxiv.org/abs/2502.11435)** (*2025*) `ACL`
  
  > Focus: tool use.
  
- **[ToolSEE: Agent Tool Search Engine for Efficient and Scalable Tool Discovery Using Retrieval](https://www.researchgate.net/publication/398436916_ToolSEE_Agent_Tool_Search_Engine_for_Efficient_and_Scalable_Tool_Discovery_using_Retrieval#read)** (*2025*) `Preprint`
  
  > Focus: tool discovery.
  
- **[Advancing tool-augmented large language models: Integrating insights from errors in inference trees](https://arxiv.org/abs/2406.07115)** (*2024*) `NeurIPS`
  
  > Focus: tool use.
  
- **[Anytool: Self-reflective, hierarchical agents for large-scale api calls](https://arxiv.org/abs/2402.04253)** (*2024*) `arXiv`
  > Focus: tool use, API use.

- **[Automatic Tool Selection to Reduce Large Language Model Latency](https://www.tdcommons.org/cgi/viewcontent.cgi?params=/context/dpubs_series/article/8702/&path_info=Automatic_Tool_Selection_to_Reduce_Large_Language_Model_Latency.pdf)** (*2024*) `Manuscript`
  
  > Focus: tool selection.
  
- **[Code Execution with MCP: 98.7% Token Reduction Through Efficient Agent Architecture](https://www.anthropic.com/engineering/code-execution-with-mcp)** (*2024*) `Anthropic`
  > Focus: MCP.

- **[Gear: Augmenting language models with generalizable and efficient tool resolution](https://arxiv.org/abs/2307.08775)** (*2024*) `ACL`
  
  > Focus: tool resolution.
  
- **[Geckopt: Llm system efficiency via intent-based tool selection](https://arxiv.org/abs/2404.15804)** (*2024*) `GLSVLSI`
  
  > Focus: tool selection.
  
- **[Gorilla: Large language model connected with massive apis](https://arxiv.org/abs/2305.15334)** (*2024*) `NeurIPS`
  
  > Focus: API use.
  
- **[Tinyagent: Function calling at the edge](https://arxiv.org/abs/2409.00608)** (*2024*) `EMNLP`
  
  > Focus: function calling, edge deployment.
  
- **[Pal: Program-aided language models](https://arxiv.org/abs/2211.10435)** (*2023*) `International conference on machine learning`
  
  > Focus: llm agents.
  
- **[Toolchain*: Efficient action space navigation in large language models with a* search](https://arxiv.org/abs/2310.13227)** (*2023*) `arXiv`
  
  > Focus: tool use.
  
- **[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)** (*2023*) `NeurIPS`
  
  > Focus: tool use.
  
- **[ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789)** (*2023*) `arXiv`
  
  > Focus: tool use, API use.
  
- **[Webgpt: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)** (*2021*) `arXiv`
  > Focus: llm agents.

#### 🗂️ Memory, Context & Long-Horizon Management

> Context compression, memory management, plan reuse, and long-horizon trajectory control.

- **[A Plan Reuse Mechanism for LLM-Driven Agent](https://arxiv.org/abs/2512.21309)** (*2025*) `arXiv`
  > Focus: agent systems.

- **[Acon: Optimizing context compression for long-horizon llm agents](https://arxiv.org/abs/2510.00615)** (*2025*) `arXiv`
  > Focus: context management, long-horizon agents.

- **[AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/abs/2510.24699)** (*2025*) `arXiv`
  > Focus: context management, long-horizon agents, web agents.

- **[Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents](https://arxiv.org/abs/2506.14852)** (*2025*) `arXiv`
  > Focus: memory, caching.

- **[Efficient On-Device Agents via Adaptive Context Management](https://arxiv.org/abs/2511.03728)** (*2025*) `arXiv`
  > Focus: context management, on-device agents.

- **[Memory as action: Autonomous context curation for long-horizon agentic tasks](https://arxiv.org/abs/2510.12635)** (*2025*) `arXiv`
  > Focus: context management, memory, long-horizon agents.

- **[Memtool: Optimizing short-term memory management for dynamic tool calling in llm agent multi-turn conversations](https://arxiv.org/abs/2507.21428)** (*2025*) `arXiv`
  > Focus: tool use, memory, multi-turn interaction.

- **[Concise and precise context compression for tool-using language models](https://arxiv.org/abs/2407.02043)** (*2024*) `ACL`
  
  > Focus: tool use, context management.
  
- **[Smurfs: Leveraging multiple proficiency agents with context-efficiency for tool planning](https://arxiv.org/abs/2405.05955v3/)** (*2024*) `arXiv`
  
  > Focus: tool use, planning, context management.

### 🔹 Efficient Tool Calling

#### 🧠 Planning, Reasoning & Decision Policies

> Reasoning-time decision policies for when, why, and how agents should plan or invoke tools.

- **[Beyond Static Tools: Test-Time Tool Evolution for Scientific Reasoning](https://arxiv.org/abs/2601.07641)** (*2026*) `arXiv`
  > Focus: tool use, reasoning.

- **[Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use](https://arxiv.org/abs/2602.11541)** (*2026*) `arXiv`
  > Focus: tool use, planning.

- **[ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning](https://arxiv.org/abs/2603.12740)** (*2026*) `arXiv`
  > Focus: tool use, planning.

- **[Catp-llm: Empowering large language models for cost-aware tool planning](https://arxiv.org/abs/2411.16313)** (*2025*) `ICCV`
  
  > Focus: tool use, planning.
  
- **[Efficient tool use with chain-of-abstraction reasoning](https://arxiv.org/abs/2401.17464) **(2025) `ACL`
  
  > Focus: tool use, reasoning.
  
- **[When2Call: When (not) to call tools](https://arxiv.org/abs/2504.18851)** (*2025*) `ACL`
  
  > Focus: tool use.
  
- **[Budget-constrained tool learning with planning](https://arxiv.org/abs/2402.15960)** (*2024*) `ACL`
  
  > Focus: tool use, planning.
  
- **[Look before you leap: towards decision-aware and generalizable tool-usage for large language models](https://arxiv.org/abs/2402.16696)** (*2024*) `arXiv`
  
  > Focus: tool use.
  
- **[Toolplanner: A tool augmented llm for multi granularity instructions with path planning and feedback](https://arxiv.org/abs/2409.14826)** (*2024*) `EMNLP`
  
  > Focus: tool use, planning.
  
- **[Tree-planner: Efficient close-loop task planning with large language models](https://arxiv.org/abs/2310.08582)** (*2023*) `arXiv`
  > Focus: planning.

- **[MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning](https://arxiv.org/abs/2205.00445)** (*2022*) `arXiv`
  > Focus: reasoning, edge deployment.

- **[React: Synergizing reasoning and acting in language models](https://arxiv.org/pdf/2210.03629)** (*2022*) `ICLR`
  
  > Focus: reasoning.

#### 🎯 Training, Distillation & Alignment

> Learning-based improvements for efficient tool use, including alignment, distillation, RL, and calibration.

- **[AdaTIR: Adaptive Tool-Integrated Reasoning via Difficulty-Aware Policy Optimization](https://arxiv.org/abs/2601.14696)** (*2026*) `arXiv`
  > Focus: tool use, reasoning.

- **[ET-Agent: Incentivizing Effective Tool-Integrated Reasoning Agent via Behavior Calibration](https://arxiv.org/abs/2601.06860)** (*2026*) `arXiv`
  > Focus: tool use, reasoning, calibration.

- **[Acting less is reasoning more! teaching model to act efficiently](https://arxiv.org/abs/2504.14870)** (*2025*) `arXiv`
  > Focus: reasoning.

- **[Adaptive tool use in large language models with meta-cognition trigger](https://arxiv.org/abs/2502.12961)** (*2025*) `ACL`
  
  > Focus: tool use.
  
- **[Advancing tool-augmented large language models via meta-verification and reflection learning](https://arxiv.org/abs/2506.04625)** (*2025*) `NeurIPS 2024 poster`
  
  > Focus: tool use.
  
- **[Agentdistill: Training-free agent distillation with generalizable mcp boxes](https://arxiv.org/abs/2506.14728)** (*2025*) `arXiv`
  > Focus: distillation, MCP.

- **[Alignment for efficient tool calling of large language models](https://arxiv.org/abs/2503.06708)** (*2025*) `EMNLP`
  
  > Focus: tool use, alignment.
  
- **[Autotir: Autonomous tools integrated reasoning via reinforcement learning](https://arxiv.org/abs/2507.21836)** (*2025*) `arXiv`
  > Focus: tool use, reasoning, reinforcement learning.

- **[Codetool: Enhancing programmatic tool invocation of llms via process supervision](https://arxiv.org/abs/2503.20840)** (*2025*) `arXiv`
  > Focus: tool use.

- **[Distilling llm agent into small models with retrieval and code tools](https://arxiv.org/abs/2505.17612)** (*2025*) `arXiv`
  > Focus: tool use, distillation.

- **[GAP: Graph-Based Agent Planning with Parallel Tool Use and Reinforcement Learning](https://arxiv.org/abs/2510.25320)** (*2025*) `arXiv`
  > Focus: tool use, planning, parallel execution.

- **[ODIA: Oriented Distillation for Inline Acceleration of LLM-based Function Calling](https://arxiv.org/abs/2507.08877)** (*2025*) `arXiv`
  > Focus: function calling, distillation.

- **[Self Knowledge-Tracing for Tool Use (SKT-Tool): Helping LLM Agents Understand Their Capabilities in Tool Use](https://aclanthology.org/2025.insights-1.14/)** (*2025*) `ACL Workshop`
  
  > Focus: tool use, edge deployment.
  
- **[Smartcal: An approach to self-aware tool-use evaluation and calibration](https://arxiv.org/abs/2412.12151)** (*2024*) `EMNLP`
  
  > Focus: tool use, calibration.

### 🔹 Efficient Tool Execution

#### ⚙️ Systems, Parallelism, Caching & Orchestration

> Execution engines, speculative calls, parallelism, serving, caching, and orchestration.

- **[Optimizing FaaS Platforms for MCP-enabled Agentic Workflows](https://arxiv.org/abs/2601.14735)** (*2026*) `arXiv`
  > Focus: MCP.

- **[Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction](https://arxiv.org/abs/2602.18968)** (*2026*) `arXiv`
  > Focus: tool use, orchestration.

- **[SemanticALLI: Caching Reasoning, Not Just Responses, in Agentic Systems](https://arxiv.org/abs/2601.16286)** (*2026*) `arXiv`
  > Focus: reasoning, caching.

- **[Sutradhara: An Intelligent Orchestrator-Engine Co-design for Tool-based Agentic Inference](https://arxiv.org/abs/2601.12967)** (*2026*) `arXiv`
  > Focus: tool use.

- **[ToolCaching: Towards Efficient Caching for LLM Tool-calling](https://arxiv.org/abs/2601.15335)** (*2026*) `arXiv`
  > Focus: tool use, caching.

- **[TVCACHE: A Stateful Tool-Value Cache for Post-Training LLM Agents](https://arxiv.org/abs/2602.10986)** (*2026*) `arXiv`
  > Focus: tool use, caching.

- **[Why Parallel Tool Calling Matters for LLM Agents](https://www.codeant.ai/blogs/parallel-tool-calling)** (*2026*) `Blog`
  > Focus: tool use, parallel execution.

- **[Asteria: Semantic-Aware Cross-Region Caching for Agentic LLM Tool Access](https://arxiv.org/html/2509.17360v1)** (*2025*) `arXiv`
  
  > Focus: tool use, caching.
  
- **[Break chatbot speed limits with speculative tool calls](https://incident.io/building-with-ai/speculative-tool-calling)** (*2025*) `Blog`
  > Focus: tool use, speculative execution.

- **[Divide-then-aggregate: An efficient tool learning method via parallel tool invocation](https://arxiv.org/abs/2501.12432)** (*2025*) `ACL`
  
  > Focus: tool use, parallel execution.
  
- **[Efficient Function Orchestration for Large Language Models](https://arxiv.org/abs/2504.14872)** (*2025*) `IEEE Transactions on Software Engineering`
  
  > Focus: orchestration.
  
- **[Flash-searcher: Fast and effective web agents via dag-based parallel execution](https://arxiv.org/abs/2509.25301)** (*2025*) `arXiv`
  
  > Focus: parallel execution, web agents.
  
- **[GhostShell: Streaming LLM Function Calls for Concurrent Embodied Programming](https://arxiv.org/abs/2508.05298)** (*2025*) `arXiv`
  > Focus: streaming.

- **[Knowledge Base-Aware Orchestration: A Dynamic, Privacy-Preserving Method for Multi-Agent Systems](https://arxiv.org/abs/2509.19599)** (*2025*) `arXiv`
  > Focus: edge deployment, orchestration.

- **[Optimizing Agentic Language Model Inference via Speculative Tool Calls](https://arxiv.org/abs/2512.15834)** (*2025*) `arXiv`
  > Focus: tool use, speculative execution.

- **[Reducing Latency of LLM Search Agent via Speculation-based Algorithm-System Co-Design](https://arxiv.org/abs/2511.20048)** (*2025*) `arXiv`
  > Focus: agent systems.

- **[Speculative Tool Calling: How to Build Sub-Second Voice Agents](https://getstream.io/blog/speculative-tool-calling-voice/)** (*2025*) `Blog`
  > Focus: tool use, speculative execution, voice agents.

- **[Stream rag: Instant and accurate spoken dialogue systems with streaming tool usage](https://arxiv.org/abs/2510.02044)** (*2025*) `arXiv`
  > Focus: tool use, streaming.

- **[An llm compiler for parallel function calling](https://arxiv.org/abs/2312.04511)** (*2024*) `Forty-first International Conference on Machine Learning`
  
  > Focus: function calling, parallel execution.
  
- **[Asynchronous llm function calling](https://arxiv.org/abs/2412.07017)** (*2024*) `arXiv`
  > Focus: function calling, asynchronous execution.

- **[Asynchronous tool usage for real-time agents](https://arxiv.org/abs/2410.21620)** (*2024*) `arXiv`
  > Focus: tool use, asynchronous execution.

- **[Conveyor: Efficient tool-aware llm serving with tool partial execution](https://arxiv.org/abs/2406.00059)** (*2024*) `arXiv`
  > Focus: tool use.

- **[Llm-dcache: improving tool-augmented llms with gpt-driven localized data caching](https://arxiv.org/abs/2406.06799)** (*2024*) `arXiv`
  > Focus: tool use, caching.

- **[Gptcache: An open-source semantic cache for llm applications enabling faster answers and cost savings](https://aclanthology.org/2023.nlposs-1.24/)** (*2023*) `ACL`
  
  > Focus: caching.
  
- **[Speculative Actions: A Lossless Framework for Faster AI Agents](https://arxiv.org/html/2510.04371v1)** (*2025*) `ICLR`
  
  > Focus: speculative execution.
  
- **[Tool Cache Agent: Accelerating LLM Agent Through Intelligent Tool Call Caching](https://openreview.net/forum?id=tX3YcbNa5w)** (*2025*) `Manuscript`
  
  > Focus: tool use, caching.

#### 📏 Benchmarks, Evaluation & Analysis

> Benchmarks, leaderboards, diagnostic analyses, and efficiency evaluation studies.

- **[When Do Tools and Planning Help LLMs Think? A Cost-and Latency-Aware Benchmark](https://arxiv.org/abs/2601.02663)** (*2026*) `arXiv`
  > Focus: tool use, planning, benchmarking.

- **[Mcpverse: An expansive, real-world benchmark for agentic tool use](https://arxiv.org/abs/2508.16260)** (*2025*) `arXiv`
  > Focus: tool use, benchmarking, MCP.

- **[Pay-per-search models are abstention models](https://arxiv.org/abs/2510.01152)** (*2025*) `arXiv`
  
  > Focus: benchmarking, llm agents.
  
- **[Rethinking Stateful Tool Use in Multi-Turn Dialogues: Benchmarks and Challenges](https://arxiv.org/abs/2505.13328)** (*2025*) `ACL`
  
  > Focus: tool use, benchmarking, multi-turn interaction.
  
- **[The berkeley function calling leaderboard (bfcl): From tool use to agentic evaluation of large language models](https://openreview.net/pdf?id=2GmDdhBdDk)** (*2025*) `ICML`
  
  > Focus: tool use, function calling, benchmarking.
  
- **[Toolsandbox: A stateful, conversational, interactive evaluation benchmark for llm tool use capabilities](https://arxiv.org/abs/2408.04682)** (*2025*) `ACL`
  
  > Focus: tool use, benchmarking.
  
- **[What Limits Agentic Systems Efficiency?](https://arxiv.org/abs/2510.16276)** (*2025*) `arXiv`
  
  > Focus: benchmarking, agent systems.

### 🚀 Applications & Agent Systems

> End-to-end systems and application-facing agent platforms built around efficient tool use.

- **[Hyperagents](https://arxiv.org/abs/2603.19461)** (*2026*) `Manuscript`
  
  > Focus: agent systems.
  
- **[OpenClaw: Open-source Personal AI Assistant ](https://github.com/openclaw/openclaw)**(*2026*) `github`
  
  > Focus: assistant systems.

## 🤝 Contributing

Contributions are welcome. You can:

- open an issue to suggest additional papers
- submit a pull request to refine categories or metadata
- add links, code repositories, figures, or annotations for individual papers

---

<p align="center">
  <i>Maintained as a curated reading list for efficient, scalable, and practical tool-using LLM agents.</i>
</p>