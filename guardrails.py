from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    input_guardrail,
    output_guardrail
)
from context import UserSessionContext


class GoalInputGuardrailOutput(BaseModel):
    is_valid: bool
    reason: str


goalagent = Agent(
    name="Goal checkagent",
    instructions="Check if the input goal is correct",
    output_type=GoalInputGuardrailOutput,
)

@input_guardrail
async def validate_goal_input(
    ctx: RunContextWrapper[UserSessionContext],
    agent: Agent,
    input: str
) -> GuardrailFunctionOutput:
    result = await Runner.run(goalagent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_valid
    )
