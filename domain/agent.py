class Agent():
    def __init__(self, name:str, sys_prompt:dict, tools:dict, knowledge:list, context_summarize:list, msg:str):
        self.name = name
        self.sys_prompt = sys_prompt
        self.tools = tools
        self.knowledge = knowledge
        self.context_summarize = context_summarize
        self.msg = msg
        
    def chat(self, input):
        """method for use agent"""
        return f"""
    your name is: {self.name}.
    your base instructions are: [{self.sys_prompt}].
    your tools are: [{self.tools}].
    your knowledge is a multiple data, the multiple data are: [{self.knowledge}].
    the summarise of conversation is: [{self.context_summarize}].
    user says: {input}"""
    
    def summarise(self, input):
        self.context_summarize = input
        return
    