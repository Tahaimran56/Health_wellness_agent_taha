from agents.tool import function_tool

@function_tool
def ProgressTrackerTool(metric: str = "steps") -> str:
    return f"Progress on {metric} has been logged. Stay focused on your daily target."
