from agents import RunHooks
from datetime import datetime

class MyHooks(RunHooks):
    def on_tool_start(self, tool_name, input, context):
        print(f"[{datetime.now()}] (started): {tool_name}  (input): {input}")

    def on_tool_end(self, tool_name, output, context):
        print(f"[{datetime.now()}] (ended): {tool_name}  (output): {output}")

    def on_agent_start(self, agent_name, input, context):
        print(f"[{datetime.now()}]  (started): {agent_name}  (user_input): {input}")

    def on_agent_end(self, agent_name, output, context):
        print(f"[{datetime.now()}]  (finished): {agent_name} (output): {output}")

    def on_handoff(self, from_agent, to_agent, input, context):
        print(f"[{datetime.now()}]  Handoff from the agent  {from_agent} to the  {to_agent} with the  input: {input}")
        if hasattr(context, "handoff_logs"):
            context.handoff_logs.append(f"Handoff  {from_agent} too {to_agent} at {datetime.now()}")
