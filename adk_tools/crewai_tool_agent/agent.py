import os
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.tools.crewai_tool import CrewaiTool

from crewai_tools import FileWriterTool


# 1. Load environment variables from the agent directory's .env file
load_dotenv()
model_name = os.getenv("MODEL")

root_agent = Agent(
    name="crewai_tool_agent",
    model=model_name,
    description="Agent to write files.",
    instruction="I can write a file if you ask me to keep a note.",
    # Add the CrewAI FileWriterTool below



)