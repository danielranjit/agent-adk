from google.adk import Agent
from google.adk.tools import google_search  # The Google Search tool

root_agent = Agent(
    # name: A unique name for the agent.
    name="google_search_agent",
    # description: A short description of the agent's purpose, so
    # other agents in a multi-agent system know when to call it.
    description="Answer questions using Google Search.",
    # model: The LLM model that the agent will use:
    model="gemini-2.0-flash-001",
    # instruction: Instructions to set the agent's behavior.
    instruction="You are an expert researcher. You stick to the facts.",
    # tools: built-in or custom functions to enhance the model's
    # capabilities.

    # Add the google_search tool here to allow the agent to
    # search the web and base its responses on the content it finds
    tools=[google_search]
)
