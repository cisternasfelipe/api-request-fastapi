from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from api.agent_json import agent_json

agent_json.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@agent_json.get("/chat")
async def chat(request: Request):
    return templates.TemplateResponse(request=request, name="chatbot.html")