from agent import Agent
from worker import Worker
from planner import Planner

class Boss(Agent):
    def __init__(self, name, sys_prompt, tools, knowledge, context_summarize, msg, mcps:dict | None, objetive:str | None, employees: dict | Worker, planner: Planner | None):
        
        super().__init__(name, sys_prompt, tools, knowledge, context_summarize, msg)

        self.objetive = objetive
        self.mcps = mcps
        self.employees = employees
        self.planner = planner
        
    def delegate_task(self, employees: dict | Worker) -> str:
        pass
    
    def review_progress(self, validate_goal: bool, employees: dict | Worker) -> bool:
        pass
    
    def retry_flow(self, validate_goal: bool, employees: dict | Worker) -> bool:
        pass
    
    def escalate_to_planner(self, planner: Planner, review_progress: bool, goal_sucess_review):
        pass