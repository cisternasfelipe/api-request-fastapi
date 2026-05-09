import uvicorn
from api.agent_json import agent_json
import api.init_http

if __name__ == "__main__":
    uvicorn.run(agent_json, host="0.0.0.0", port=8000)