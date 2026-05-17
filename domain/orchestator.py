from __future__ import annotations
from agent import Agent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from planner import Planner

class Orchestator(Agent):
    def __init__(self, name, sys_prompt, tools, knowledge, context_summarize, msg, planner_reference:Planner, department_bosses:list | dict, active_workflow : dict, execution_state: dict):
        super().__init__(name, sys_prompt, tools, knowledge, context_summarize, msg)

        self.planner_reference = planner_reference
        self.department_bosses = department_bosses
        self.active_workflow = active_workflow
        self.execution_state = execution_state

    # Methods
    def analyze_proposed_plan(self, *args, **kwargs):
        pass

    def segment_requirements(self, *args, **kwargs):
        pass

    def dispatch_to_bosses(self, *args, **kwargs):
        pass

    def synchronize_workflow(self, *args, **kwargs):
        pass

    def compile_final_delivery(self, *args, **kwargs):
        pass