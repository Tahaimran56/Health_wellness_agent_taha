from agents.tool import function_tool

@function_tool
def MealPlannerTool(diet: str = "balanced") -> str:
   return f" For a {diet} diet, we suggest meals rich in plant-based protein, leafy greens, seasonal fruits, and lots of water — for all 7 days."
