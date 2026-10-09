from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. 定义状态
class State(TypedDict):
    content: str

# 2. 初始化图
graph_builder = StateGraph(State)

# 3. 添加节点
def node_a(state: State) -> State:
    return {"content": "处理完成v2"}

graph_builder.add_node("A", node_a)

# 4. 连边（使用 START / END 常量）
graph_builder.add_edge(START, "A")
graph_builder.add_edge("A", END)

# 5. 无需再调用 set_entry_point，START 边已指定入口
# 6. 指向 END 即为流程终点，无需 set_finish_point

# 7. 编译图
graph = graph_builder.compile()

# 8. 执行工作流，
# invoke()方法只接收状态字典作为核心参数
res = graph.invoke({"content": "start"})
print(res)