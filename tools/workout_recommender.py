from agents.tool import function_tool

@function_tool
def WorkoutRecommenderTool(goal: str = "general fitness") -> str:
    return f"To help you achieve your goal of {goal}, we suggest a daily routine with a 30-minute walk and 20 minutes of strength training."
