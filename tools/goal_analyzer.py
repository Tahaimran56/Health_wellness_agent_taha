from agents.tool import function_tool

@function_tool
def GoalAnalyzerTool(goal: str) -> str:
    return f" Love it! '{goal}' is a strong, inspiring goal — we’ll turn it into an actionable plan."
