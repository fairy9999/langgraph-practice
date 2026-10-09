# LangGraph 学习实践

基于 LangGraph 的渐进式学习练习，掌握图（Graph）编排构建有状态 AI 应用。

## 内容目录

| 模块 | 内容 |
|------|------|
| 01_helloworld | LangGraph 入门示例 |
| 02_graph | 图的构建与编译 |
| 03_state | State 定义与状态管理（StateGraph） |
| 04_node | 节点（Node）编写 |
| 05_edge | 边（Edge）与条件路由（Conditional Edges） |
| 06_persistence | 持久化与多轮对话记忆（Checkpointer） |

## 技术栈

- Python 3.x + LangGraph
- uv 依赖管理（`pyproject.toml` / `uv.lock`）

## 运行方式

```bash
# 安装依赖
uv sync

# 运行任意练习脚本
python code/06_persistence/xxx.py
```
