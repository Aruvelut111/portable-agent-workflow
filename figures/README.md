# 图示 / Figures

[中文正文](../README.md) · [English article](../README.en.md)

文章里的三张图都放在这里，每张有 SVG、PDF 和 PNG。标签用英文，两种语言的说明见下文。图里画的是工作关系，没有性能数据或真实项目结构。

The article's three figures are available here as SVG, PDF, and PNG. They share English labels, with descriptions in both languages below. They show relationships, without performance data or an actual project's structure.

## 01 · 库和工作环境 / The library and working environments

[SVG](01-portability.svg) · [PDF](01-portability.pdf) · [PNG](01-portability.png)

规则、知识、方法、工具登记和项目进度，按当前任务提供给 Agent。需要细节时还能打开原件。换个工作环境，可以继续使用这些资料，再分别接好规则加载、工具调用、权限、消息和恢复方式。

Rules, knowledge, procedures, tool records, and project progress provide context for the task, with originals available for closer reading. The material can be reused in another environment, which still needs its own setup for loading, tool calls, permissions, messaging, and recovery.

## 02 · 分工和反馈 / Assignments and feedback

[SVG](02-collaboration.svg) · [PDF](02-collaboration.pdf) · [PNG](02-collaboration.png)

用户主要和项目负责人交流。负责人分任务、收结果，最后把东西接到实际使用的地方。蓝色双向箭头表示派活和反馈，虚线表示成员围绕具体问题的沟通。文件和进度留在能找到的位置。共用同一个应用或运行资源时，要另外协调，免得互相影响。图中的成员数量只是示意。

The user mainly talks to the project lead, who assigns work, collects results, and connects them to where they will be used. Blue arrows show assignments and feedback; dashed lines show communication about a specific dependency. Files and progress remain accessible. Shared applications and runtime resources need separate coordination. The team size is illustrative.

## 03 · 一直试到实际使用 / Trying the result in use

[SVG](03-delivery.svg) · [PDF](03-delivery.pdf) · [PNG](03-delivery.png)

拿真实输入，经过处理、传递和加载，看最后用起来是否正确。出问题时，沿途找最早出现的差异，修改相关部分。图里画回处理环节只是一个例子，也可以查回输入、传递或使用端。中断后先看上次实际完成了什么，再继续，避免重复执行已经生效的操作。

Take real input through processing, transfer, and loading, then check the result in use. Follow a problem back to its first relevant difference and change the affected part. The return to processing is illustrative; investigation can return to the input, handoff, or application. After an interruption, check what actually completed before continuing, to avoid repeating actions that already took effect.

## 下载和重新生成 / Downloads and rendering

SVG 和 PDF 便于放大或放进其他文档，PNG 用于预览。SVG 把字形保存成路径，减少缺字体带来的变化；需要文字说明，可以看正文和本页。

SVG and PDF are useful for scaling or inclusion in documents; PNG is for preview. SVG stores glyphs as paths to reduce font-substitution changes. The article and this page provide text descriptions.

从仓库根目录执行 / Run from the repository root:

```sh
python -m pip install -r requirements-figures.txt
python figures/render.py
```

脚本会覆盖本目录三个具名图示的九个导出文件，不读取项目资料，也不联网。已在 Python 3.13 上运行，直接依赖见 requirements。不同后端和间接依赖可能影响输出字节。

The script overwrites the nine exports for these three figures. It reads no project inputs and makes no network calls. It has been run on Python 3.13; the direct dependency is in requirements. Backends and transitive dependencies can affect output bytes.

制作时参考了 [K-Dense Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) 的相关建议，详见[参考资料 20–21](../docs/references.md#figure-method)。图由本仓库原创 Matplotlib 代码绘制，使用白底、简单配色和线型。脚本会检查文字是否超出画布，箭头含义和阅读效果仍要看成图。

Relevant guidance came from [K-Dense Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md); see [references 20–21](../docs/references.md#figure-method). The figures use original Matplotlib code, white backgrounds, and simple colors and line styles. The script checks whether text extends beyond the canvas. Arrow meanings and readability still need inspection.
