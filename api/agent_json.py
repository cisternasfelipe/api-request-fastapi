from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from agentscope.agent import ReActAgent

class AgentCreator(BaseModel):
    name: str
    prompt: str
    tools: list
    knowledge: list
        
agent_json=FastAPI()
@agent_json.post("/agents")

async def get_agent(agent: AgentCreator):
    # agent setup
    new_agent = ReActAgent(
        name = agent.name,
        prompt = agent.prompt
    )
    return new_agent
    # Start the agent reply as a task
    