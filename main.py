import os, getpass
from graph.builder import buildGraph


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


def setup():
    _set_env("OPENAI_API_KEY")
    _set_env("LANGSMITH_API_KEY")
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_PROJECT"] = "langchain-academy"


setup()


graph = buildGraph()
