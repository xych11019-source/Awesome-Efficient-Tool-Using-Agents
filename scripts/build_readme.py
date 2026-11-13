"""Regenerate README.md from the curated bibliography; Python standard library only."""
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PAPERS=json.loads((ROOT/'data/papers.json').read_text())
GROUPS=json.loads((ROOT/'data/taxonomy.json').read_text())
BY_ID={p['id']:p for p in PAPERS}
SOURCE='https://www.preprints.org/manuscript/202608.0365'
def esc(s):return s.replace('|','\\|').replace('*','\\*').replace('<','&lt;').replace('>','&gt;')
def slug(s):return re.sub(r'[^a-z0-9 -]','',s.lower()).replace(' ','-')
def row(p):
 links=f"[{p['linkType']}]({p['url'] or p['searchUrl']})"
 if p['code']:links+=f" · [Code]({p['code']})"
 return f"| **{esc(p['method'])}** | {esc(p['title'])} | {p['year']} | {esc(p['venue']) or '—'} | {links} |"
def table(ps):return '\n'.join(['| Method | 📄 Paper | 📅 Year | 🏛️ Venue in survey | 🔗 Links |','| :--- | :--- | :---: | :--- | :--- |']+[row(p) for p in ps])
icons={'Context':'🧩','Calling':'🛠️','Reasoning':'🧠','Execution':'⚡'}
subicons={'Tool Set Compression':'🗂️','Tool Description Compression':'✂️','History Compression':'🧹','Eligibility-Aware Calling':'✅','Cost-Aware Calling':'💰','Trajectory Optimization':'🎯','Reasoning Reuse':'♻️','Results Caching':'💾','Parallel Execution':'🔀','Speculative Execution':'🚀'}
stages=['Context','Calling','Reasoning','Execution']
counts={s:sum(p['stage']==s for p in PAPERS) for s in stages}
text=f'''<p align="center">
  <img src="assets/banner.svg" alt="Efficient Tool-Using LLM Agents — a survey and curated reading list" width="100%">
</p>

<h1 align="center">How to Make Tool-Using LLM Agents Efficient?</h1>
<p align="center"><strong>🎉 Accepted at EACL 2026</strong><br>A Survey · A Structured Reading List</p>
<p align="center">
  <a href="{SOURCE}"><img src="assets/badge-survey.svg" alt="Read the survey"></a>
  <img src="assets/badge-references.svg" alt="139 references">
  <img src="assets/badge-stages.svg" alt="4 agent stages">
  <img src="assets/badge-coverage.svg" alt="Literature coverage through July 2026">
</p>

<p align="center">Yunuo Hu · Ziyang Cheng · Wenqi Pei · Miaomiao Li · Boyan Li · Yizhang Zhu<br>Yupeng Xie · Han Chen · Shizheng Hou · Yuyu Luo · Hongyang Du</p>
<p align="center"><a href="{SOURCE}">📄 Paper ↗</a> &nbsp; · &nbsp; <a href="#reading-list">📚 Reading List</a> &nbsp; · &nbsp; <a href="#citation">📝 Cite This Survey</a></p>

<a id="about"></a>

## 📘 About

Tool-using agents spend resources on context, invocation decisions, reasoning trajectories, and execution. This collection follows the survey's four-stage taxonomy to help researchers locate techniques that reduce that overhead while preserving task performance.

The survey tracks four resources: **tokens**, **tool calls**, **latency**, and **monetary cost**. Improvements across studies use different settings and should not be interpreted as a common performance ranking.

> Preprint: [Version 1, posted 6 August 2026]({SOURCE}). Literature coverage ends in July 2026. Source snapshot: 13 November 2026.

<a id="navigation"></a>

## 🧭 Navigation

| Stage | Research question | Entries below |
| :--- | :--- | :---: |
| [🧩 01 · Efficient Tool Context](#efficient-tool-context) | How can an agent carry less context? | {counts['Context']} |
| [🛠️ 02 · Efficient Tool Calling](#efficient-tool-calling) | When is a tool call worth making? | {counts['Calling']} |
| [🧠 03 · Efficient Tool Reasoning](#efficient-tool-reasoning) | How can an agent reason with less repeated work? | {counts['Reasoning']} |
| [⚡ 04 · Efficient Tool Execution](#efficient-tool-execution) | How can tools finish with less waiting? | {counts['Execution']} |
| [🌱 Background & Related Work](#background--related-work) | Foundations, benchmarks, surveys, and further directions | 22 |

The classified list includes **117 references discussed in Section 3**, including two industry articles. The paper states that its taxonomy covers 111 works; this repository also retains the additional Section 3 citations so that no cited references are silently omitted. The tables below include **all 139 source entries**, including background and industry references.

**Link key:** `Paper` links to an arXiv identifier present in the bibliography. `Search` opens a title-based Scholar search when a direct paper URL was not extracted. `Code` retains a repository link supplied by Table A1; links are not a guarantee of implementation quality or availability. Years follow the bibliography; venues follow Table A1. `—` means the comparison table does not supply a venue for that entry.

<a id="reading-list"></a>

## 📚 Reading List

'''
for stage in stages:
 text+=f'<a id="efficient-tool-{stage.lower()}"></a>\n\n## {icons[stage]} Efficient Tool {stage}\n\n'
 for sub in dict.fromkeys(g['subcategory'] for g in GROUPS if g['stage']==stage):
  text+=f'### {subicons[sub]} {sub}\n\n'
  for group in [g for g in GROUPS if g['stage']==stage and g['subcategory']==sub]:
   text+=f"#### {group['approach']}\n\n"+table([BY_ID[i] for i in group['ids']])+'\n\n'
 text+='[↑ Back to navigation](#navigation)\n\n'
text+='<a id="background--related-work"></a>\n\n## 🌱 Background & Related Work\n\n'+table([p for p in PAPERS if p['stage']=='Background'])+'\n\n'
text+='''<a id="source-notes"></a>

## 🔎 Source Notes

- CATP-LLM and GAP have empty inline citations in the source narrative. Their bibliography entries are matched by method title (references 116 and 117).
- The source prose cites “Curtis (2025)” while reference 1 reads “Kurtis, L. K. (2025)”; both forms are preserved in the provenance notes.
- MASH is labeled “Preprint 2025” in Table A1, but its bibliography year is 2026. The list uses 2026.
- The source-provided TokenPilot repository resolves to a differently branded project; verify it before treating it as the official implementation. The AutoTIR repository fetch timed out during preparation; its source-provided URL is retained.
- Several bibliography entries contain incomplete arXiv identifiers (`arXiv:cs`). No replacement identifiers or publication claims have been invented. Titles, years, and venues are transcribed from this survey rather than independently audited for every paper.
- Resources mentioned without numbered references, such as some benchmarks in Appendix F, are not counted among the 139 references. OpenClaw is linked as a [source footnote](https://github.com/openclaw/openclaw).

'''
text+='''<a id="citation"></a>

## 📝 Citation

```bibtex
@misc{hu2026efficienttoolagents,
  title   = {How to Make Tool-Using LLM Agents Efficient? A Survey},
  author  = {Hu, Yunuo and Cheng, Ziyang and Pei, Wenqi and Li, Miaomiao
             and Li, Boyan and Zhu, Yizhang and Xie, Yupeng and Chen, Han
             and Hou, Shizheng and Luo, Yuyu and Du, Hongyang},
  year    = {2026},
  note    = {Preprints.org, Version 1, posted 6 August 2026},
  url     = {https://www.preprints.org/manuscript/202608.0365}
}
```

<a id="contributing"></a>

## 🤝 Contributing

Corrections and additions are welcome. Include the paper title, stable URL, year, relevant taxonomy branch, and an official code link where available. For corrections to the source snapshot, provide the source reference number. Keep newly suggested papers distinct from the Version 1 bibliography.

The structured records live in [`data/papers.json`](data/papers.json), with taxonomy membership in [`data/taxonomy.json`](data/taxonomy.json). Regenerate this page after editing them:

```sh
python3 scripts/build_readme.py
```

<a id="attribution"></a>

## 💛 Attribution

Taxonomy and bibliographic information are adapted from **Hu et al., “How to Make Tool-Using LLM Agents Efficient? A Survey,” Preprints.org, Version 1 (2026)**, available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This repository reorganizes that information and adds navigation, link labels, and provenance notes. Linked papers and code remain subject to their respective licenses.
'''
(ROOT/'README.md').write_text(text)
assert len(PAPERS)==139 and set(BY_ID)==set(range(1,140))
assert len([i for g in GROUPS for i in g['ids']])==len({i for g in GROUPS for i in g['ids']})==117
assert all(p['title'] and not p['title'].startswith('arXiv') for p in PAPERS)
assert len([line for line in text.splitlines() if line.startswith('| **')])==139
assert 'Ref. ' not in text and 'complete-bibliography' not in text
for target in re.findall(r'\]\(#([^)]*)\)',text):
 assert f'id="{target}"' in text or any(slug(h)==target for h in re.findall(r'^#+ (.*)$',text,re.M)),target
print(f'Built README: {len(PAPERS)} references; 117 classified entries; {len(text):,} characters. Anchors and coverage verified.')
