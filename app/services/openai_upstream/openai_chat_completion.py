from utils import read_mcp_config


class OpenAIChatCompletion:
    def __init__(self, service):
        self.client = service.client
        self.query_config = service.query_config
        self.model_name = self.query_config.agent.model_name
        self.previous_response_id = getattr(
            getattr(self.query_config.thread, "thread_meta", None),
            "response_id",
            None
        )
        self.tools = []
        self.file_ids = []
        self.meta_content = None
        self.prepare_tool_data()
        self.prepare_files()

    def prepare_files(self):
        context_data = list(self.query_config.context_data)
        for data in context_data:
            if data.get("file_id", None):
                self.file_ids.append(data.get("file_id"))
            if data.get("meta_content", None):
                self.meta_content = data.get("meta_content")

    def prepare_send_msg(self):
        msgs = []
        listing_description = f"""
        \n\n ======The below is the listings data=====
        {self.meta_content}
        \n\n
        """
        msgs.append({"role": "developer", "content": self.query_config.topic.topic_description + listing_description})
        for file_id in self.file_ids:
            msgs.append({
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "file_id": file_id
                    }
                ]
            })
        return msgs


    def prepare_tool_data(self):
        tools_types = getattr(self.query_config.topic, "tools", "")
        tools_types = tools_types.split(",")
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
        msgs = self.prepare_send_msg()
        msgs.append({
            "role": "user",
            "content": str(message)
        })
        response = self.client.responses.create(
            model = self.model_name,
            input = msgs,
            previous_response_id = self.previous_response_id,
            tools = self.tools
        )
        response = self.construct_response(response)
        return response

    def construct_response(self, response):
        result = {
            "message" : response.output_text,
            "role" : "system",
            "thread_meta": {
                "response": response.id
            }
        }
        return result





