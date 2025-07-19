from typing import Any, Dict
class Agent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions

#runner logic
class Runner:
    @staticmethod
    async def run(agent: Agent, input_text: str, context: Dict[str, Any]) -> Dict[str, Any]:
        # Basic goal valid check
        if any(unit in input_text.lower() for unit in ['kg', 'pounds', 'lbs']) and \
           any(time in input_text.lower() for time in ['week', 'month', 'year']):
            return {"is_valid": True, "reason": "Valid goal format."}
        else:
            return {"is_valid": False, "reason": "Invalid format. Example: 'lose 5kg in 2 months'"}

# Define agent
goal_check_agent = Agent(
    name="Goal Validator",
    instructions="Check if the input goal is in valid format (e.g. 'lose 5kg in 2 months')"
)

# Guardrail validation 
async def validate_goal_input(ctx: Dict[str, Any], input_text: str) -> Dict[str, Any]:
    result = await Runner.run(goal_check_agent, input_text, context=ctx)
    return {
        "output_info": result,
        "tripwire_triggered": not result["is_valid"]
    }

import asyncio

async def test():
    context = {"user_id": 123}
    input_text = "lose 5kg in 2 months"
    validation_result = await validate_goal_input(context, input_text)
    print(validation_result)

asyncio.run(test())
