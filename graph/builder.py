from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import tools_condition
from langchain.messages import ToolMessage
from graph.nodes import assistant_node, tools_node
from typing import Literal


def after_tool_condition(state: MessagesState) -> Literal["assistant", END]:
    last = state["messages"][-1]

    if isinstance(last, ToolMessage) and last.name == "find_all_books":
        return END

    return "assistant"


def buildGraph():
    builder = StateGraph(MessagesState)

    builder.add_node("assistant", assistant_node)
    builder.add_node("tools", tools_node)

    builder.add_edge(START, "assistant")

    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_conditional_edges("tools", after_tool_condition)

    return builder.compile()
