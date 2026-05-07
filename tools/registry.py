from agentscope.tool import Toolkit
from tools.get_crypto_price import get_crypto_price
from tools.mongo_query_executor import query_find
def registry_tool(functions:list):
    toolkit = Toolkit()
    for tool in functions:
        toolkit.register_tool_function(tool)
    return toolkit
        
REGISTRY_TOOLS = {
    "get_crypto_price":get_crypto_price,
    "query_find":query_find
}