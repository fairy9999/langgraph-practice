from typing import TypedDict
from langgraph.constants import START, END
from langgraph.graph import StateGraph

# 1. 定义状态机对象Obj，等价于业务实体entity，或者叫当前数据快照
class GraphStateObj(TypedDict):
    process_data: dict


if __name__ == '__main__':
    obj = GraphStateObj()

    # 第一种写法：[key]
    obj["k1"] = "v1"  # set k1 v1
    obj["k2"] = "v2"

    print(obj.keys())
    print(obj.values())


    #写法2：get方法
    print(obj.get("k1"))
    print(obj.get("k3"))

    print(obj["k1"])
    print(obj["k3"])# KeyError: 'k3'











    # 遍历键
    for key in obj:
        print(key)

    # 遍历键+值
    for k, v in obj.items():
        print(f"{k}: {v}")

    #
    #







