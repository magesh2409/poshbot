from functools import total_ordering

from utils import read_mcp_config


class OpenAIChatCompletion:
    def __init__(self, service):
        self.client = service.client
        self.query_config = service.query_config
        self.model_name = self.query_config.agent.model_name
        self.previous_response_id = getattr(self.query_config.thread.thread_meta, "response_id", None)
        self.tools = []
        self.prepare_tool_data()

    def prepare_tool_data(self):
        tools_types = self.query_config.topic.tools
        for tool in tools_types:
            if tool == "code_interpreter":
                self.tools.append({
                    "type": "code_interpreter",
                    "container": {
                        "type": "auto"
                    }
                })
            elif tool == "web_search":
                self.tools.append({
                    "type": "web_search"
                })

            elif tool == "mcp":
                mcp_params = read_mcp_config()
                self.tools.append({
                    "type": "mcp",
                    "server_label": mcp_params["name"],
                    "server_url": mcp_params["url"]
                })

    def send_response(self, message):
        response = self.client.responses.create(
            model = self.model_name,
            input = str(message),
            previous_response_id = self.previous_response_id,
            tools = self.tools
        )
        response = self.construct_response(response)
        return response

    def construct_response(self, response):
        result = {
            "output_text" : response.output_text,
            "role" : "system",
            "response" : response.id

        }
        return result





