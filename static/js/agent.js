//let para variables mutables
let agentConfig = {
    name: "default",
    prompt: "",
    agent_tools: ["get_crypto_price", "query_find"]
};
let interactions = [];

function handleKey(event) {
    if (event.key === "Enter") {sendAgent()}
    return
};

function renderMessage(role, text) {
    const element = document.createElement("div")
    element.className = "msg-" + role
    element.textContent = text
    document.getElementById("messages").appendChild(element)
};

// function that return body of agent_json api for endpoint /agents 
function sendAgent() {
    let user_prompt = document.getElementById("user_write").value;    

    if (user_prompt === "") {
        alert("You need write a prompt")
        return
    };

    const body = {
        name: agentConfig.name,
        prompt: agentConfig.prompt,
        agent_tools: agentConfig.agent_tools,
        knowledge: [],
        msg:user_prompt
    };

    renderMessage("user", user_prompt)

    const waiting_response = document.createElement("div")
    waiting_response.textContent = "..."
    waiting_response.className = "msg-agent loading"
    document.getElementById("messages").appendChild(waiting_response) 

    fetch("http://127.0.0.1:8000/agents", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("messages").removeChild(waiting_response)
        
        renderMessage("agent", data.content[0].text)
        
        interactions.push({role:"user", text:user_prompt})
        
        interactions.push({role: data.role, text:data.content[0].text})
    })
};

function fetch_chat() {
    document.getElementById("messages").value
};