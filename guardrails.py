from agents.guardrail import input_guardrail, GuardrailFunctionOutput
from agents.run import Runner
from agents import RunContextWrapper, Agent
from pydantic import BaseModel
from agents import TResponseInputItem

import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from agents import set_tracing_disabled



load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Error: GEMINI_API_KEY not found in .env file. Add your Gemini API key to proceed.")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client
)

# Define output type
class HealthInputOutput(BaseModel):
    is_health_related_question: bool
    input: str
    reasoning: str
    answer: str

# Define agent used for input validation
health_guardrail_agent = Agent(
    name="Health Input Guardrail Agent",
    instructions=(
    "You are a smart assistant that checks whether a user's message is related to health or wellness. "
    "Valid topics include health, fitness, diet, workout, exercise, goal setting, progress tracking, meal planning, "
    "nutrition, injuries, wellness, and check-ins. You should also accept greetings like 'hi', 'hello', or 'hey' "
    "as valid input. If the message is clearly unrelated to these topics, mark it as not health-related."
),
    output_type=HealthInputOutput,
    model=model
)

# actual guardrail function
@input_guardrail
async def health_input_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input:str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    try:
        result = await Runner.run(health_guardrail_agent, input, context=ctx.context, run_config=config)
        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=not result.final_output.is_health_related_question
        )
    except Exception as e:
        print(f"[Guardrail Error] Input validation failed: {e}")
        return GuardrailFunctionOutput(
            output_info=None,
            tripwire_triggered=True
        )
