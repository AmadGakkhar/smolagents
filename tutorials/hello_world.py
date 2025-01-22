from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
import os
from dotenv import load_dotenv

load_dotenv()

model = HfApiModel(token=os.getenv("HF_API_TOKEN"))

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run(
    "How many seconds would it take for a leopard at full speed to run through Pont des Arts?"
)
