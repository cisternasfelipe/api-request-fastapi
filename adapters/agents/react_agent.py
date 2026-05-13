from ports.llm_port import LLMPort
from agentscope.agent import ReActAgent, AgentBase
from agentscope.model import OpenAIChatModel
from agentscope.formatter import OpenAIChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
import asyncio
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class react_agent(LLMPort, BaseModel):
    name:str
    sys_prompt:dict
    agent_tools:list
    knowledge:list
    context_summarize:list
    msg:str
    
    def model_post_init(self, context):
        self.agent=ReActAgent(
                name=self.name,
                sys_prompt=str(self.sys_prompt),
                model=OpenAIChatModel(
                api_key = os.environ.get("YOUR_PROVIDER_APIKEY"),
                model_name = "deepseek-chat",
                client_args={
                    "base_url": "https://api.deepseek.com"
                },
                knowledge=str(self.knowledge),
                enable_thinking=True,
                stream=True,
                multimodality=False
                ),
                formatter=OpenAIChatFormatter(),
                memory=InMemoryMemory()
            )
        return super().model_post_init(context)
            
    
    async def chat(self, user_name, input):
            msg=Msg(name=user_name, content=input, role="user")
            response = await self.agent(msg)
            
            return response
            
    def summarise(self,user_name, input):
            msg=Msg(name=user_name, content=str(input))