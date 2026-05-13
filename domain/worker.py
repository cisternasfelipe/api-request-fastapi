from agent import Agent

class Worker(Agent):
    """Slave Agent 哈哈哈哈"""
    def __init__(self, name, sys_prompt, tools, knowledge, context_summarize, msg, objetive:str | None, mcps:dict | None):
        
        super().__init__(name, sys_prompt, tools, knowledge, context_summarize, msg)
        
        self.mcps = mcps
        self.objetive = objetive
        
    def try_goal(self, objetive, mcps:dict | None, tools:dict | None) -> bool:
        """iterate flow to succes goal"""
        pass
    def validate_goal(self) -> bool:
        pass
    def goal_sucess_review(self) -> str:
        pass