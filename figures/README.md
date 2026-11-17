# 图示与复现 / Figures and reproduction

[中文文章](../README.md) · [English article](../README.en.md)

这些是原创概念示意图，用于解释文章中的关系。图中没有性能数据、真实项目结构或平台兼容性测试结果。英文标签供两种语言正文共用，下面提供完整文字说明。

These original conceptual figures explain relationships in the article. They contain no performance data, actual project topology, or platform-compatibility results. Both editions use the same English labels; full text descriptions follow.

## 01 · 工作材料与执行适配 / Working material and execution adaptation

[SVG](01-portability.svg) · [PDF](01-portability.pdf) · [PNG](01-portability.png)

规则、知识、流程、能力登记和项目状态构成不同职责的工作材料。当前任务只获取相关上下文，并能继续访问证据。不同 harness 分别接入加载、调用、权限、消息和恢复。材料可迁移，并不证明各平台运行能力相同。

Rules, knowledge, procedures, capability records, and project state have distinct responsibilities. A task obtains relevant context while retaining access to evidence. Each harness adapts loading, invocation, permissions, messaging, and recovery. Portable material does not establish equivalent runtime capabilities.

## 02 · 协作与集成责任 / Collaboration and integration ownership

[SVG](02-collaboration.svg) · [PDF](02-collaboration.pdf) · [PNG](02-collaboration.png)

用户主要与集成负责人交流目标和重要选择。负责人安排有边界的任务，需要时安排独立审查，并对实际消费者中的可用结果负责。蓝色双向连接表示任务派发与结果反馈。成员围绕具体依赖直接交流，产物和当前状态可被接续。共享文件和运行环境仍需协调，图中成员数量是示意。

The user primarily discusses goals and important choices with the integration owner. That owner coordinates bounded work and targeted review when warranted, and is responsible for a usable result in the actual consumer. Blue bidirectional connections show task assignment and result feedback. Workers communicate about specific dependencies and leave artifacts and current state for continuation. Shared files and runtime resources still require coordination. The depicted team size is illustrative.

## 03 · 实际交付、诊断与恢复 / Actual delivery, diagnosis, and recovery

[SVG](03-delivery.svg) · [PDF](03-delivery.pdf) · [PNG](03-delivery.png)

真实输入经过处理和交接，由消费者加载使用，形成可观察结果。出现差异时，检查第一处与问题相关的语义分歧，再修改受影响的假设或接口。虚线回到处理环节只是示例，调查也可以回到输入、交接或消费者。中断后，依据当前决定和已提交产物确认下一动作，重试前核对已有副作用。

Real input passes through processing and handoff into a consumer and observable result. Diagnose the earliest relevant semantic divergence, then revise the affected assumption or interface. The dashed return to processing is illustrative: investigation can return to the input, handoff, or consumer. After interruption, current decisions and committed artifacts establish the next action. Check earlier side effects before retrying.

## 制作方式 / Design method

采用白底、克制配色、统一字号和线宽，用标签及实线/虚线共同表达关系。没有装饰图标、渐变或虚构数据。SVG 将字形保存为路径，减少字体缺失造成的变化；正文与本页提供可读文字替代。PDF 保留矢量形状，PNG 供预览。

The figures use white backgrounds, restrained colors, consistent typography and line weights, and redundant labels and line styles. They contain no decorative icons, gradients, or invented data. SVG stores glyphs as paths to reduce font-substitution differences; the article and this page supply readable text alternatives. PDFs retain vector shapes; PNGs provide previews.

图示制作参考了 [K-Dense Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) 的相关原则，来源归属见[研究记录 20–21](../docs/references.md#figure-method)。没有调用外部图像生成服务，绘图代码为本仓库原创。

Relevant guidance came from [K-Dense Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md); see [references 20–21](../docs/references.md#figure-method). No external image-generation service was called. The rendering code is original to this repository.

## 复现 / Reproduce

从仓库根目录执行 / Run from the repository root:

```sh
python -m pip install -r requirements-figures.txt
python figures/render.py
```

脚本只覆盖本目录三个具名图示的 SVG/PDF/PNG，不读取业务输入、不联网。Python 3.13 上实跑；依赖版本见 requirements。不同后端和间接依赖可能影响字节，不承诺逐字节相同。

The script overwrites only the three named SVG/PDF/PNG sets in this directory, reads no business inputs, and makes no network calls. It was run on Python 3.13; the direct dependency is in requirements. Backends and transitive dependencies can change bytes; byte-for-byte replay is not promised.

文字边界检查只检查标签是否超出画布。图的含义、箭头和最终阅读效果仍需查看，自动检查不构成论文规范或可访问性认证。

The text-boundary check only detects labels outside the canvas. Meaning, arrows, and final readability require inspection. The check is not publication or accessibility certification.
