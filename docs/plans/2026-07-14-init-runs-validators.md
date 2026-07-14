# init 自带校验 — 一条命令完成引导+校验

## 动机

skill 规定 init 后必须跑两个校验器，agent 要发三条 shell 命令（三次模型往返，秒级各一次）。
init 本身幂等且毫秒级，慢的全是往返。把校验合进 init：一条命令，一次往返。

## 变更单元（顺序固定：docs → tests → code）

1. **docs**：`docs/design-harness/output/file-structure.md` 里 init_workspace.py 的描述
   补一句"引导后自跑两个校验器"；SKILL.md 的 Getting started 从三条命令改为一条
   （"每次写入后跑两个校验器"的规则保留，只对 init 场景免除）。
2. **tests**（先失败）：`tests/test_workspace_tools.py`
   - 干净目录跑 `init_workspace.main` → 返回 0，输出含 init 与两个校验器的 ok 行，
     无 INVALID/DANGLING 行。
   - 预置坏卡（idea 缺 id/type）再跑 main → 返回 1，输出点名坏卡。
   - 预置死链卡再跑 main → 返回 1，输出 DANGLING。
   - 测试内 monkeypatch.chdir 到 tmp_path（main 会在 cwd 写指针文件）。
3. **code**：`init_workspace.py` 的 `main` 在 init+record 后依次调用
   `check_workspace.main` 与 `check_doc_links.main`（复用其打印与退出码，DRY），
   任一非零则整体返回 1。
4. **版本**：两份 plugin.json 同步 bump 0.8.0 → 0.8.1。
5. **验证**：对全新临时目录与含坏卡目录各跑一次真实命令，确认退出码与输出。

## 验收

- 单测/系统测全绿；`init_workspace.py <ws>` 单命令即完成引导+全部校验。
- 校验失败时退出码非零（fail-safe：坏 workspace 不会静默通过）。
