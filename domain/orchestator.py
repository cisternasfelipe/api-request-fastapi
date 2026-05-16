from __future__ import annotations
from agent import Agent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from planner import Planner

class Orchestator(Agent):
    def __init__(self, name, sys_prompt, tools, knowledge, context_summarize, msg):
        super().__init__(name, sys_prompt, tools, knowledge, context_summarize, msg)