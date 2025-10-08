import requests

url = "http://127.0.0.1:5000"

response = requests.get(url)

service_name = "openai"
model_name = "gpt-4.1"
user_id = "68e553454e05fbc189605af0"
api_key = ""
topic_name = "Sample AI Test"
topic_description = "You are an helpful AI"
tools = "code_interpreter,web_search"

service = requests.post(url + "/api/service", json={"service_name": service_name, "user_id": user_id, "api_key": api_key})
agent = requests.post(url + "/api/agent", json={"service_id": service.json()["id"], "model_name": model_name})
topic = requests.post(url + "/api/topic", json={"agent_id": agent.json()["id"], "topic_name": topic_name, "topic_description": topic_description, "tools": tools})
context = requests.post(url + "/api/context", json={})


thread = requests.post(url + "/api/thread", json={"topic_id": topic.json()["id"], "context_id": context.json()["id"]})
thread_id = thread.json()["id"]


while True:
    query = input("ASK AI: ")
    if query == "":
        break
    response = requests.post(url + "/api/query/" + thread_id, json={"message": query})
    print("AI Response :", response.json())



