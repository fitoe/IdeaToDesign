# IdeaToDesign

中文为主，English summary included below.

`IdeaToDesign` 是一个面向产品构思与设计推进场景的 Agent Skill。  
它的目标不是替代设计师，也不是生成冗长流程文档，而是把模糊想法逐步整理为清晰的产品结构、分阶段视觉草稿，以及一份可供设计评审和后续开发参考的正式设计文档。

---

## 项目定位

`IdeaToDesign` 适用于以下场景：

- 只有一句模糊想法，希望快速整理为产品方案
- 已有部分页面、流程或参考图，希望继续推进设计
- 希望借助成熟设计模式减少补充细节的负担
- 希望将零散设计过程收敛为正式的设计文档

它强调：

- 先任务流，后页面
- 先结构化规格，后视觉出图
- 先核心页面，后扩展页面
- 让最终交付保持轻量、清晰、可读

---

## 核心目标

`IdeaToDesign` 的默认目标是产出三类核心结果：

1. `Design-Spec.md`
   正式设计文档，作为主要交付物
2. `assets/`
   分阶段设计图资产目录
3. `state.json`
   机器可读状态文件，用于断点续跑与低成本延续

这意味着它不是“只会生图”的技能，也不是“只会写文档”的技能，而是一套从想法到正式设计说明的推进机制。

---

## 工作方式

`IdeaToDesign` 默认使用三种入口模式：

1. `Start from idea`
   从模糊想法开始整理
2. `Continue current design`
   基于现有状态、文档或图稿继续推进
3. `Finalize design doc`
   将已存在的结构与图稿整理为正式设计文档

内部流程分为五个阶段：

1. `Scope`
2. `Structure`
3. `Visual Direction`
4. `Image Iteration`
5. `Finalize`

设计上刻意保持“前台简单、后台有序”：

- 用户不需要一次性补齐所有细节
- 技能会主动给出合理假设和候选结构
- 复杂流程信息尽量隐藏在后台文件中
- 最终对外只暴露轻量交付结果

---

## 设计原则

本技能遵循以下核心原则：

- `task-flow-first`
  先定义核心用户任务流，再展开页面
- `spec-as-source-of-truth`
  结构化规格是事实来源，图片只是表达手段
- `reference-driven-hypothesis`
  当用户输入不完整时，可参考成熟设计模式生成可编辑假设
- `stage-gated-progression`
  通过阶段门禁控制推进，避免跳步失控
- `selective-fidelity-escalation`
  默认只对核心页面提升保真度
- `designer-friendly-output`
  最终输出应让设计师愿意看、开发拿得动

---

## 为什么这样设计

很多“从想法到设计”的流程容易出现两个问题：

- 过度依赖用户逐项补细节，导致推进成本高
- 最终堆出大量文档和过程材料，设计师与开发都不想看

`IdeaToDesign` 的处理方式是：

- 使用成熟产品模式帮助补全结构假设
- 控制默认范围，只深做核心 flow 和核心页面
- 将过程留档与正式交付分开
- 用单一主文档承载最终设计说明，降低阅读成本

---

## 目录结构

当前仓库结构如下：

```text
idea-to-design/
  SKILL.md
  quick-start.md
  templates/
    design-spec-template.md
    state-template.json
  references/
    stage-gates.md
    prompt-patterns.md
    review-checklists.md
```

说明：

- `SKILL.md`
  主技能定义
- `quick-start.md`
  超短上手说明，用于降低高频使用时的 token 开销
- `templates/`
  正式设计文档与状态文件模板
- `references/`
  阶段门禁、出图 prompt 模式与评审清单

---

## 推荐使用方式

如果你希望将本技能用于自己的技能目录，推荐做法：

1. 复制 `idea-to-design/` 整个目录
2. 放入你的 Agent Skill 路径
3. 在实际项目中以 `Start from idea`、`Continue current design` 或 `Finalize design doc` 模式使用

建议先从一个小范围任务开始，例如：

- 一个核心用户流程
- 3 到 5 个关键页面
- 一份轻量正式设计文档

这样最容易验证该技能是否符合你的设计推进习惯。

---

## 输出风格

本项目默认追求以下输出特征：

- 正式但不过度官僚
- 友好但不过度口语
- 清晰、克制、便于交接
- 强调设计决策，而不是堆积过程噪音

---

## English Summary

`IdeaToDesign` is an agent skill for turning vague product ideas into structured design outcomes.

It helps:

- shape rough concepts into flows and pages
- use mature design patterns as editable references
- iterate visuals in controlled stages
- consolidate outputs into a formal `Design-Spec.md`

Default outputs:

- `Design-Spec.md`
- `assets/`
- `state.json`

The goal is not to generate more documentation.  
The goal is to generate a design package that is readable, reviewable, and practical for downstream implementation.

---

## Status

Current version is an initial public release focused on:

- usability
- controlled scope
- token efficiency
- designer-friendly final output

Future refinement may include:

- stronger example outputs
- improved quick-start workflows
- lighter continuation patterns

---

## License / Notes

This repository is currently shared as a public skill project for reference and reuse.  
If you plan to adapt it for your own workflow, it is recommended to adjust:

- tone of output
- final document depth
- image iteration strategy
- archival detail level

to fit your team and project size.
