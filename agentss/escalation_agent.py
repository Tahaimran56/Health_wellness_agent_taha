from agents.tool import function_tool

@function_tool
def EscalationAgent(issue: str = "emergency") -> str:
    return f" your have  '{issue}' kindly contact to doctor.i cannot help more on this "
