# 图示与复现 / Figures and Reproduction

[中文正文](../README.md) · [English article](../README.en.md)

三张原创图示分别说明库与执行环境、协作关系、交付与恢复路径。每张提供 SVG、PDF 和 PNG，使用共用英文标签及下列双语说明。图示表达设计关系，不包含性能数据，也不对应某个内部项目结构。

Three original figures describe the library and execution environment, collaboration, and delivery and recovery. Each is available as SVG, PDF, and PNG, with shared English labels and bilingual descriptions below. They depict design relationships, not performance data or an internal project structure.

## 01 · 库与执行环境 / Library and execution environment

[SVG](01-portability.svg) · [PDF](01-portability.pdf) · [PNG](01-portability.png)

规则、知识、方法、工具登记与项目状态组成可持续维护的工作信息。会话按任务读取相关内容，并可沿引用检查原件。更换执行环境时，这些内容可以复用；规则加载、工具连接、权限、消息与恢复则需要分别适配。

Rules, knowledge, procedures, tool records, and project state form maintained working information. A conversation selects relevant content and follows references to originals. The material can be reused across environments, while rule loading, tool connections, permissions, messaging, and recovery need their own adaptation.

## 02 · 任务协作与集成 / Task coordination and integration

[SVG](02-collaboration.svg) · [PDF](02-collaboration.pdf) · [PNG](02-collaboration.png)

用户主要与集成负责人沟通，负责人维护目标、关键依赖与整体交付。蓝色双向箭头表示任务和反馈，虚线表示成员围绕依赖的直接沟通。共享产物与当前状态支持接续，但不要求共享全部聊天。工作区之外的共享应用和运行资源仍需协调，图中成员数量为示意。

The user primarily communicates with the integration lead, who maintains goals, important dependencies, and delivery. Blue bidirectional arrows represent assignments and feedback; dashed links represent dependency-specific communication. Shared outputs and current state support continuity without sharing every conversation. Shared applications and runtime resources outside the workspaces still need coordination. Team size is illustrative.

## 03 · 实际交付与中断恢复 / Delivery and recovery

[SVG](03-delivery.svg) · [PDF](03-delivery.pdf) · [PNG](03-delivery.png)

真实输入经过处理和交接，在实际应用或读者处形成结果。发现差异时，沿依赖定位相关环节，修正受影响的输入、假设或实现。图中回到处理环节的箭头仅为示意，诊断可以返回任一相关位置。中断后先确认已提交产物和已生效操作，再决定从何处继续。

Real input passes through processing and handoff to produce a result in an application or for a reader. Differences are traced through dependencies to correct the relevant input, assumption, or implementation. The arrow returning to processing is illustrative; diagnosis can return to any relevant stage. Recovery first establishes committed outputs and effects before choosing where to continue.

## 导出格式与生成方法 / Export formats and rendering

SVG 与 PDF 适合缩放和嵌入文档，PNG 用于预览。SVG 将字形保存为路径，以减少字体替换造成的变化；正文和本页提供对应文字说明。

SVG and PDF support scaling and inclusion in documents; PNG is for preview. SVG stores glyphs as paths to reduce font-substitution changes. The article and this page provide corresponding text descriptions.

从仓库根目录执行 / Run from the repository root:

```sh
python -m pip install -r requirements-figures.txt
python figures/render.py
```

脚本会覆盖本目录三个具名图示的九个导出文件，不读取项目资料，也不联网。已在 Python 3.13 上运行；直接依赖见 requirements。不同后端与间接依赖可能影响输出字节。

The script overwrites the nine exports for these three figures. It reads no project inputs and makes no network calls. It has been run on Python 3.13; direct dependencies are in requirements. Backends and transitive dependencies can affect output bytes.

图示方法参考 [K-Dense Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md)，采用原创 Matplotlib 代码、白底、有限配色与可区分线型，来源说明见[参考资料 20–21](../docs/references.md#figure-method)。脚本检查文字是否超出画布；连接含义与阅读效果需查看成图。

The method draws on [K-Dense Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md), using original Matplotlib code, white backgrounds, restrained colors, and distinguishable line styles. See [references 20–21](../docs/references.md#figure-method) for provenance. The script checks text bounds; connection meaning and readability require inspection of the rendered figures.
