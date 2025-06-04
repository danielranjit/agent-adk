from google.adk import Agent
# from agents.tools.retrieval import VertexAISearchTool
from google.adk.tools import VertexAiSearchTool

# The data_store_id path maps to the datstore parameter in the
# google.genai.types.VertexAISearch type
# https://googleapis.github.io/python-genai/genai.html#genai.types.VertexAISearch

# Create your vertexai_search_tool and update its path below
vertexai_search_tool = VertexAiSearchTool(
   data_store_id="projects/qwiklabs-gcp-01-a80a34502ff4/locations/global/collections/default_collection/dataStores/planet-search_1748916382631"
)


root_agent = Agent(
   # A unique name for the agent.
   name="vertexai_search_agent",
   # The Large Language Model (LLM) that agent will use.
   model="gemini-2.0-flash-001",
   # A short description of the agent's purpose, so other agents
   # in a multi-agent system know when to call it.
   description="Answer questions using your data store access.",
   # Instructions to set the agent's behavior.
   instruction="
   Assume that you are space scientist. As per the data you fetched from datastore
   You analyze new planet discoveries and engage with the scientific community on them.
   Explain those concepts in a simple way as if you are explaining to a kid",
   # Add google_search tool to perform grounding with Google search.
   tools=[vertexai_search_tool]
)
