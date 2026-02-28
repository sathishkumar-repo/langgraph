from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults
import datetime

load_dotenv()

# 1. Initialize LLM
llm = ChatOpenAI(model="gpt-4o")

search_tool = TavilySearchResults(search_depth="basic")

tools = [search_tool]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

agent.invoke("Current time in Tamilnadu")