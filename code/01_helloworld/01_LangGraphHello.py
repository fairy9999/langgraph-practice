# pip install -U langgraph
# pip install grandalf
from typing import TypedDict, Annotated, List, Dict
from langgraph.graph import StateGraph, START, END
import uuid
from langchain_core.runnables.graph import MermaidDrawMethod


# 1．定义State对象(官网推荐必选，but可选)
class HelloState(TypedDict):
    name: str
    greeting: str

"""
class Order
{
    private int id;
    private String orderName;
}
"""

# 2.定义节点Node(就是干活的函数)
def greet(helloState: HelloState) -> dict:
    name = helloState["name"]
    return {"greeting": f"你好,{name}"}
    #return helloState

"""
public Map greet(HelloState helloState)
{
    helloState.getName();
    return new HashMap();
}
"""

def add_emoji(helloState:HelloState) -> dict:
    greeting = helloState["greeting"]
    return {"greeting": greeting + "  。。。😄"}


# 3.构建图graph
graph = StateGraph(HelloState)

graph.add_node("greeting",greet)
graph.add_node("add_emoji",add_emoji)

graph.add_edge(START, "greeting")
graph.add_edge("greeting","add_emoji")
graph.add_edge("add_emoji",END)


# 4.编译图
app = graph.compile()

# 5.运行
# invoke()方法只接收状态字典作为核心参数
result = app.invoke({"name":"z3"})
print(result)
print()
print(result["greeting"])



#
# #6 打印图的边和节点信息
#6.1 打印图的ascii可视化结构
print(app.get_graph().print_ascii())
print("="*50)
#
#6.2 打印图的Mermaid代码可视化结构并通过https://www.processon.com/mermaid编辑器查看
print(app.get_graph().draw_mermaid())
print("="*50)


#
#6.3 生成 PNG并写入文件 ，一般需要开启科学上网
png_bytes = app.get_graph().draw_mermaid_png(max_retries=2,retry_delay=2.0)
output_path = "langgraph" + str(uuid.uuid4())[:8] + ".png"
with open(output_path, "wb") as f:
    f.write(png_bytes)
print(f"图片已生成：{output_path}")

"""
上面第3种方式，容易bug,时好时坏，域名解析失败，程序无法解析 mermaid.ink 域名，
连不上在线绘图接口，所以导出 Mermaid 图片失败。
ValueError: Failed to reach https://mermaid.ink  
API while trying to render your graph after 1 retries. 
To resolve this issue:
1. Check your internet connection and try again
2. Try with higher retry settings: `draw_mermaid_png(..., max_retries=5, retry_delay=2.0)`
3. Use the Pyppeteer rendering method which will render your graph locally in a browser: 
`draw_mermaid_png(..., draw_method=MermaidDrawMethod.PYPPETEER)`
"""

