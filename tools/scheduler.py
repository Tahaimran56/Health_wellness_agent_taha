from agents.tool import function_tool

@function_tool
def CheckinSchedulerTool(day: str = "Sunday") -> str:
 return f" Let’s stay on track! Your progress check is scheduled for every {day} morning"
