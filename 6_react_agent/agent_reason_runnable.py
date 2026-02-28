from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import create_react_agent, tool
from langchain_community.tools import TavilySearchResults
import datetime
from langchain import hub

load_dotenv()

# 1. Initialize LLM
llm = ChatOpenAI(model="gpt-4o")

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

react_prompt = hub.pull("hwchase17/react")


tools = [get_system_time, search_tool]

react_agent_runnable = create_react_agent(tools=tools, llm=llm, prompt=react_prompt)