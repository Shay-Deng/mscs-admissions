# MSCS Admissions

[简体中文](README.md) | English

A skill for applicants to computer science and related master's programs in North America. It helps you assess program fit, verify program information, and develop ideas for your application essays.

## School Selection

Assess your competitiveness in the context of your undergraduate institution, GPA on its original grading scale, major, and application cycle, using traceable admission cases. Distinguish admissions selectivity from program value and consider each applicant's outcomes across multiple programs. An admission to a safety choice should not define an applicant's ceiling, and a single exceptional admission should not inflate expectations for everyone with a similar profile.

GPA is a central factor. Research, internships, and projects are evaluated against each program's specific expectations. Assessments stay consistent whether you express confidence or anxiety.

## Official Website Research and Essay Planning

Research official program websites, application requirements, curricula, and faculty research interests. Connect these findings to your actual experiences to identify relevant examples, questions to explore, and ways to organize your ideas. Distinguish explicit requirements from analytical suggestions, helping you explain why a program fits your interests and what you hope to gain from it.

## Usage

The repository root is the skill directory, with [SKILL.md](SKILL.md) as its entry point. Download or clone the repository, then place the entire directory in your tool's skills directory under the name `mscs-admissions`.

```text
mscs-admissions/
├── SKILL.md
├── agents/
├── references/
└── scripts/
```

Example prompts:

> Use $mscs-admissions to assess suitable programs based on my undergraduate background, GPA, and target application cycle. Support your assessment with evidence.

> Use $mscs-admissions to research my target program's official website and help me develop essay ideas from my existing experiences.

Official website research uses the web search and browsing tools available in your environment. Local reference search requires Python 3.9 or later; data updates also require curl.

## Sources

Thanks to the authors and contributors of [Open CS Application](https://opencs.app/) and [CS Grad](https://csgrad.com/). Reference materials retain their source and version information and should be checked against official information for the target application cycle.

This project is licensed under [CC BY-NC-SA 4.0](LICENSE).
