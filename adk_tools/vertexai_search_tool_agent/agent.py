from google.adk import Agent
# from agents.tools.retrieval import VertexAISearchTool
from google.adk.tools import VertexAiSearchTool

# The data_store_id path maps to the datstore parameter in the
# google.genai.types.VertexAISearch type
# https://googleapis.github.io/python-genai/genai.html#genai.types.VertexAISearch

# Create your vertexai_search_tool and update its path below
vertexai_search_tool = VertexAiSearchTool(
   data_store_id="projects/YOUR_PROJECT_ID/locations/global/collections/default_collection/dataStores/YOUR_DATA_STORE_ID"
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
   instruction="You analyze new planet discoveries and engage with the scientific community on them.",
   # Add google_search tool to perform grounding with Google search.
   tools=[vertexai_search_tool]
)
