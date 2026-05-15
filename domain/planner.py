from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from orchestator import Orchestator
from agent import Agent

class Planner(Agent):
    def __init__(self, name, sys_prompt, tools, knowledge, context_summarize, msg, orchestator: Orchestator | None):
        
        super().__init__(name, sys_prompt, tools, knowledge, context_summarize, msg)
        
        self.orchestator = orchestator
        
        
    def analize_failure(self):
        pass         
    
    def determine_new_requeriments(self):
        pass
    
    def draft_plan(self):
        pass
    
    def call_orchestator(self): 
        pass
    
    def prepare_report(self):
        pass
    
    def count_request(self):
        """Circuit breaker: Worker 3 reintentos, Boss 1, Planner contador en BD """
        pass