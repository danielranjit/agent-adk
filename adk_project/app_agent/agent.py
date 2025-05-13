from google.adk import Agent
from google.adk.artifacts import InMemoryArtifactService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

import os
from dotenv import load_dotenv

# 1. Load environment variables from the agent directory's .env file
load_dotenv()
google_cloud_project = os.getenv("GOOGLE_CLOUD_PROJECT")
google_cloud_location = os.getenv("GOOGLE_CLOUD_LOCATION")
google_genai_use_vertexai = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "1")
model_name = os.getenv("MODEL")

# 2. Define Your Agent
root_agent = Agent(
    model=model_name,
    name="my_agent",
    instruction="Answer questions.",
)

# 3. Create Session and Artifact Services and a Session
session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()
session = session_service.create_session(app_name="my_app", user_id="user1")

# 4. Create a Runner
runner = Runner(agent=root_agent,
                artifact_service=artifact_service,
                session_service=session_service,
                app_name="my_app")

if __name__ == "__main__":

    # 5. Package a query string into content that identifies itself
    # as having come from a user
    query = "What is the capital of France?"
    content = types.Content(role='user',
                            parts=[types.Part(text=query)])

    # 6. Run the query
    events = runner.run(session_id=session.id, user_id="user1", new_message=content)

    # 7. Process each response event, printing only the final response
    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print(final_response)
