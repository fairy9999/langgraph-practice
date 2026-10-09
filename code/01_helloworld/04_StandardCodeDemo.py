from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. 定义状态
class State(TypedDict):
    content: str

# 2. 初始化图
graph_builder = StateGraph(State)

# 3. 添加节点
def node_a(state: State) -> State:
    return {"content": "处理完成"}

graph_builder.add_node("A", node_a)

# 4. 连边
graph_builder.add_edge("A", END)

# 5. 设置入口（必选）
graph_builder.set_entry_point("A")

# 6. 出口这里用 END 全局常量，无需额外 set_finish_point

# 7. 编译
graph = graph_builder.compile()

# 8. 执行
res = graph.invoke({"content": "start"})
print(res)