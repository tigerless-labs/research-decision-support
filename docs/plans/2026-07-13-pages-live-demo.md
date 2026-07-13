# Pages 活画布 demo

## 目标

README 首图可点，打开一份永远跟 master 同步的活画布。投影不入库：由 GitHub Actions
在每次 push master 时从 `docs/design-harness`（dogfood 工作区）重建并部署到 GitHub
Pages（source 已设为 workflow，站点 `tigerless-labs.github.io/design-harness`）。

## 单元

1. **workflow** `.github/workflows/pages.yml`：build_canvas 一条命令 → 产物改名
   index.html → 官方 upload/deploy-pages 链路。
2. **README**：首图包 Pages 链接 + 一行"点图进活画布"；Usage 的十秒示例从
   examples/autoharness 换成 docs/design-harness（本仓库自身的工作区）。
3. **验证**：合并后盯 Actions 跑绿、curl Pages URL 200、浏览器无头开一次确认可渲染。
