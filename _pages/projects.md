---
layout: page
title: Research & Projects
permalink: /projects/
description: Selected work in agent evaluation, cybersecurity, and simulation.
nav: false
nav_order: 1
---

<div class="research-intro"><p>Selected research and coursework in autonomous-agent evaluation, cybersecurity, and simulation. Each entry identifies my role, collaborators, methods, and source availability.</p></div>

<article class="case-study" id="modelscope">
  <div class="case-study-head"><div><p class="eyebrow">Flagship research</p><h2>ModelScope</h2><p class="case-subtitle">Evaluation platform for autonomous AI agents</p></div><span class="status-pill">In development</span></div>
  <dl class="project-facts"><div><dt>Role</dt><dd>Research fellow and contributor</dd></div><div><dt>Collaborators</dt><dd>Dr. Jaime C. Acosta; Army Research Laboratory (ARL)</dd></div><div><dt>Methods</dt><dd>Agent benchmarking, objective validation, telemetry, simulated environments</dd></div><div><dt>Technologies</dt><dd>Python, modular plugin architecture, Linux</dd></div></dl>
  <h3>Problem</h3><p>ModelScope evaluates whether autonomous agents complete objectives, how efficiently they operate, what resources they consume, and whether they comply with policy.</p>
  <h3>My contribution</h3><p>As an Army HBCU-MI SPARK research fellow, I am helping build ModelScope and designed a modular plugin architecture for configurable agents and objective ground-truth criteria. The platform captures task success, operational speed, resource usage, and policy-compliance metrics for auditable validation.</p>
  <h3>Evidence and status</h3><p>The work is an active 2026 research deliverable connected to a collaboratively developed cyber Capture-the-Flag environment. Dr. Jaime C. Acosta owns and maintains the public repository; this page describes my contribution and does not imply sole authorship.</p>
  <div class="button-row"><a class="button button-secondary" href="https://github.com/raistlinJ/ModelScope">View maintained repository <span class="sr-only">for ModelScope on GitHub</span></a></div>
</article>

<article class="case-study" id="specguard">
  <div class="case-study-head"><div><p class="eyebrow">Research prototype</p><h2>SpecGuard</h2><p class="case-subtitle">AI-assisted vulnerability discovery system</p></div><span class="status-pill">Prototype</span></div>
  <dl class="project-facts"><div><dt>Role</dt><dd>Designer and developer</dd></div><div><dt>Methods</dt><dd>Static analysis, LLM reasoning, RAG, pairwise-correctness evaluation</dd></div><div><dt>Technologies</dt><dd>Python, LangChain, ChromaDB, Ollama</dd></div><div><dt>Evidence</dt><dd>1,999 real-world CVEs used as indexed ground truth</dd></div></dl>
  <h3>Problem</h3><p>Vulnerability discovery tools often trade interpretability and coverage against one another. SpecGuard explores whether deterministic analysis and language-model reasoning can complement each other.</p>
  <h3>Approach and results</h3><p>I built a hybrid framework that retrieves from a ChromaDB knowledge base indexing the <code>hzhu721/vulnerability-specifications</code> dataset. Detection logic covers memory corruption, use-after-free, and integer overflow, while an evaluation pipeline scores output against CVE ground truth at scale.</p>
  <p class="link-note"><strong>Source status:</strong> The repository is not yet public, pending documentation, licensing, reproducibility, and security review.</p>
</article>

<article class="case-study" id="evacuation">
  <div class="case-study-head"><div><p class="eyebrow">Advanced Algorithms coursework</p><h2>Evacuation Optimization Simulator</h2><p class="case-subtitle">Congestion-aware multi-agent routing</p></div><span class="status-pill">Course project</span></div>
  <dl class="project-facts"><div><dt>Role</dt><dd>Developer</dd></div><div><dt>Methods</dt><dd>Graph modeling, simulation, comparative algorithm analysis</dd></div><div><dt>Technologies</dt><dd>Dijkstra and Floyd-Warshall routing</dd></div><div><dt>Outcomes measured</dt><dd>Evacuation rate, time-to-safety, population throughput</dd></div></dl>
  <h3>Approach</h3><p>I modeled edge capacity, congestion, and variable movement speed, then compared routing behavior across realistic constraints. The project connected algorithmic correctness with system-level outcomes rather than treating shortest paths in isolation.</p>
  <p class="link-note"><strong>Source status:</strong> No public repository is available for this course project.</p>
</article>
