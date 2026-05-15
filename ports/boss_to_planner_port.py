from abc import ABC, abstractmethod

class BossToPlanner(ABC):
    @abstractmethod
    def call_planner(self, call: dict | str):
        pass