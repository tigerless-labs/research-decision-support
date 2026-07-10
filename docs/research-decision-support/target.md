# target — output 的验收目标

人对 output 的要求在此登记；output 是对本清单的履行，每条要求可核对。要求变更时
agent 同回合重推 output 受影响部分（与 [output-auto-refresh](ideas/output-auto-refresh.md)
同一纪律：idea 变更与 target 变更都是刷新触发源）。

## 主旨

设计一个**思路理清器 / 决策 board**：把经过历史验证的思维方法做成按场景组织的决策
辅助，核心命题是**决策权在人——AI 铺开选项和证据，帮人快速拍板**（人拍板、agent
跑腿）。主战场是基于调研的决策（evidence-based）：选型、文献综述、尽调、竞品分析
——决策必须站在可溯源的证据上；直觉型、政治型、纯偏好型决策不在射程内。与把思维
模型当 AI 推理透镜的同类项目不同，交付的是有状态的决策协议，产出是人的选择加理由
——版本化、留痕可溯，以决策速度和可追溯性衡量，而非 AI 准确率。

## 当前要求（2026-07-09）

output 必须包含：

- 一张**系统流程图**（泳道分人/agent，纯逻辑不含 UI）与一张**系统架构图**
  （六模块，细节不入图）——**同居一个 markdown、同画在一个页面**；
- **每个模块对应 output/modules/ 下的一份细节 md**；
- **canvas 画板只是可视化层**——基于 markdown 真身的变化而变化，不持有任何事实；
- **skill 的文件结构设计**——skill 包与工作区的完整布局，落到可直接实现的树。

## 履行对照

- 系统流程图 + 系统架构图 → [output/system.md](output/system.md)（HTML 同页呈现）
- 模块细节 → [output/modules/](output/modules/source.md)（source / idea / output /
  canvas / agent / protocol）
- canvas 可视化层约束 → [output/modules/canvas.md](output/modules/canvas.md)
- skill 文件结构 → [output/file-structure.md](output/file-structure.md)
