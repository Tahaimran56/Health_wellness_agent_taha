from agents.tool import function_tool

@function_tool
def NutritionExpertAgent(query: str = "daily protein needs") -> str:
    return f" As a nutritionist, i suggest you consume {query} to maintain a healthy lifestyle."

