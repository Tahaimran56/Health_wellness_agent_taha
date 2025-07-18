# from agents.tool import function_tool

# @function_tool
# def NutritionExpertAgent(query: str = "daily protein needs") -> str:
#     return f" As a nutritionist, i suggest you consume {query} to maintain a healthy lifestyle."

#now we make special agent 

from agents import Agent

nutrition_agent = Agent(
    name="Nutrition Expert Agent",
    instructions=(
        "You are a nutrition expert. Help users with dietary needs as well as "
        "such as diabetes, food allergies, or medical conditions.much more"
    )
)
