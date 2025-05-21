import os
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.tools.langchain_tool import LangchainTool # import

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# 1. Load environment variables from the agent directory's .env file
load_dotenv()
model_name = os.getenv("MODEL")

root_agent = Agent(
    name="lanchgain_tool_agent",
    model=model_name,
    description="Agent to answer questions using Wikipedia.",
    instruction="I can answer your questions by searching Wikipedia! Ask me about a historical figure.",
    # Add the LangChain Wikipedia tool below
        tools = [
        # Use the LangchainTool wrapper...
        LangchainTool(
            # to pass in a LangChain tool.
            # In this case, the WikipediaQueryRun tool,
            # which requires the WikipediaAPIWrapper as
            # part of the tool.
            tool=WikipediaQueryRun(
              api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]
)