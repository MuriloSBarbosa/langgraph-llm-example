import asyncio
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langchain_mcp_adapters.client import MultiServerMCPClient
from graph.tools import book_tool


with open("mcp_servers.json", "r", encoding="utf-8") as f:
    servers = json.load(f)

mcp_client = MultiServerMCPClient(servers)

tools_from_mcp = asyncio.run(mcp_client.get_tools())
tools = [book_tool.find_all_books, book_tool.insert_book] + tools_from_mcp


llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)


def assistant_node(state: MessagesState) -> MessagesState:
    with open("prompts/system.txt", "r", encoding="utf-8") as f:
        content = f.read()
        system = SystemMessage(content)
        result = llm_with_tools.invoke([system] + state["messages"])
        return new_message(result)


def new_message(message) -> MessagesState:
    return {"messages": [message]}


def tools_node(state: MessagesState):
    return ToolNode(tools)
