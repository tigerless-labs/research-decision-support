# workspace 发现协议 + .design-harness 指针

## 背景

skill 允许 workspace 放在任意位置，但没有任何机制让新会话找回自定义位置：
用户没把路径写进宿主说明时，agent 会找不到、或在默认路径重复 init 出一个
分叉的空 workspace。裁决（人）：落一个 runtime 中立的指针文件
`.design-harness/config.json`，目录名锁死 `design-harness`，配合按名查找兜底。

## 方案

- **指针**：宿主项目根 `.design-harness/config.json`，唯一字段 `workspace`
  （相对宿主根的路径；仓外用绝对路径）。它是指针不是真相：丢失/损坏/指错
  都由后续发现步骤重建，fail-safe。第一版不存任何偏好。
- **发现顺序**（新模块 `discover_workspace.py`，其余脚本无参时调用）：
  1. config 存在且指向结构合法的 workspace（含 `sources/ ideas/ output/`
     目录 + `logs.md`）→ 用；
  2. 否则查默认 `docs/design-harness/`；
  3. 否则全树按目录名 `design-harness` 扫描（排除 `.git` `node_modules`
     `.claude` 等）；
  4. 恰一个 → 用；多个/零个 → 脚本报明确错误退出，由 agent 问人——
     **绝不默默新建**。
- **写入**：只有 `init_workspace.py` 写 config（含默认路径也写，行为统一）；
  发现函数保持纯读。无参 init 先走发现：已有 workspace → 幂等 no-op 并补写
  config；多个 → 报错；零个 → 在默认路径 init 并写 config。
- **SKILL.md**：Getting started 增加发现顺序与"多候选/零候选必问人、
  绝不默默 init"的行为约定。
- **manifest**：双清单 patch 版本号同步 bump。

## 单元（每单元 tests 先行）

1. output 文档：`file-structure.md` 增 config 指针与新脚本条目；
   `modules/agent.md` 增"操作前先定位 workspace，绝不默默新建"边界；
   `logs.md` 追记；`docs/testing.md` 测试映射更新。
2. `tests/test_discover_workspace.py`：config 命中 / config 指向失效路径回退 /
   默认路径命中 / 按名扫描唯一命中 / 多候选与零候选返回歧义 / 结构校验拒绝
   同名非 workspace 目录 / config 畸形 JSON fail-safe / init 写 config /
   无参 init 发现已有 workspace 时不再新建默认目录。
3. `scripts/discover_workspace.py` 实现 + `init_workspace.py`
   `check_workspace.py` `build_canvas.py` `check_doc_links.py` 无参默认改走发现。
4. 端到端验证：临时宿主目录内自定义位置 init → 无参 check/build 均命中；
   全测试绿 → PR → CI 绿。
