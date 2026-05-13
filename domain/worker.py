from agent import Agent

class Worker(Agent):
    def __init__(self, name, sys_prompt, tools, knowledge, context_summarize, msg, objetive, mcps:dict):
        super().__init__(name, sys_prompt, tools, knowledge, context_summarize, msg)
        self.mcps = mcps
        self.objetive = objetive
        
    def try_goal(self, objetive, mcps:dict | None, tools:dict | None) -> bool:
        """iterate flow to succes goal"""
    
    def validate_goal(self):
        
    def goal_sucess_review(self):