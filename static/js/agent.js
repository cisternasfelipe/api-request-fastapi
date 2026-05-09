// function that return body of agent_json api for endpoint /agents 
function sendAgent() {
    
    const name = document.getElementById("name").value;
    const prompt = document.getElementById("prompt_form").value;
    const tool_get_crypto_price = document.getElementById("tool_get_crypto_price").checked;
    const tool_query_find = document.getElementById("tool_query_find").checked;
    
    const agent_tools = [];
    if (tool_get_crypto_price) {
        agent_tools.push("get_crypto_price");
    };
    if (tool_query_find) {
        agent_tools.push("query_find");
    };
    if (agent_tools.length === 0) {
        alert("Select Any Option to Continue")
        return;
    };
    
    const msg = document.getElementById("msg").value;
    if (msg === "") {
        alert("The Field Cannot be Empty")
        return;
    };

    const body = {
        name: name,
        prompt: prompt,
        agent_tools: agent_tools,
        knowledge: [],
        msg:msg
    };

    fetch("http://127.0.0.1:8000/agents", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").textContent = data.content[0].text;
    })
};



function fetch_chat() {
    document.getElementById("messages").value
};