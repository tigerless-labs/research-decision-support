# 计划：skill 三维优化（实用性 / 泛用性 / 易用性）

## 诊断

- 实用性：SKILL.md 引用的 `check_workspace.py` 不存在（承诺落空）；无 bootstrap，冷启动
  靠 agent 手搓目录。
- 泛用性：正文与模板全中文、词汇锁死"论文"，与英文 README/分发定位错位；工作区路径
  硬编码单一默认。
- 易用性：五层方法一次性压给新用户；无渐进采用路径；idea 状态枚举单语，站点徽章
  只识别部分词。

## 决定

- SKILL.md 与 templates/references 改英文正文（分发面统一英文），description 保留中英
  双语触发词；示例工作区保持中文原貌（真实性即卖点）。
- 状态枚举双语等价（候选/candidate、采纳/adopted、存疑/doubtful），校验器与站点徽章
  两套都认。
- 新增 `init_workspace.py`（幂等骨架初始化）与 `check_workspace.py`（frontmatter 校验）。
- SKILL.md 增加渐进采用节：sources+ideas 两层起步，其余层按信号激活。

## 单元（docs → tests → code → verify → commit）

1. 本计划 + `docs/design/workbench.md` 增补校验器/初始化器职责。
2. tests：init 幂等与骨架完整；check 必填字段、双语枚举、sources 豁免、坏卡报错。
3. scripts 实现；site_template 徽章正则补双语。
4. SKILL.md / templates / note-types 英文重写（结构不变）。
5. 全量验证、demo 重建、安装副本同步、push。

## 验收

- 空目录一条命令得到五层骨架；重复跑不覆盖已有内容。
- 坏 frontmatter（缺字段/越界枚举）被校验器点名；示例工作区通过校验。
- SKILL.md 英文、双语触发、无"论文"锁死措辞；模板英文且枚举双语标注。
