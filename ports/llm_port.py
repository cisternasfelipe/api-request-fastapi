from abc import ABC, abstractmethod

class LLMPort(ABC):
    @abstractmethod
    def chat(self, input):
        pass
    
    @abstractmethod
    def summarise(self, input):
        pass