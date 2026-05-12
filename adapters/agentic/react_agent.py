from ports.llm_port import LLMPort
from agentscope.agent import ReActAgent
from agentscope.model import OpenAIChatModel
from agentscope.formatter import OpenAIChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
import asyncio
from pydantic import BaseModel

class react_agent(LLMPort, BaseModel):
    name:str
    sys_prompt:dict
    agent_tools:list
    knowledge:str
    context_summarize:list
    msg:str
    
    async def chat(self, input):
        msg=Msg(name="User", content=agent.msg, role="user")
        
        agent=ReActAgent(
            name=agent.name,
            sys_prompt=str(self.sys_prompt),
            model=OpenAIChatModel(
            api_key = os.environ.get("YOUR_PROVIDER_APIKEY"),
            model_name = "deepseek-chat",
            client_args={
                "base_url": "https://api.deepseek.com"
            },
            enable_thinking=True,
            stream=True,
            multimodality=False
            ),
            formatter=OpenAIChatFormatter(),
            memory=InMemoryMemory()
        )
        
        response = await chat()
        
    def summarise(self, input):
        