# from agents.tool import function_tool

# @function_tool
# def EscalationAgent(issue: str = "emergency") -> str:
#     return f" your have  '{issue}' kindly contact to doctor.i cannot help more on this "

#now we use make special agent

from agents import Agent

escalation_agent = Agent(
    name="Escalation Agent",
    instructions="You are a human support assistant. Help the user and prepare to hand them off to a real human if needed."
)
