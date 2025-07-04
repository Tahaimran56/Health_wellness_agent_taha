from openai_agents import Runner

async def stream_response(agent, input_text, context):
    async for step in Runner.stream(starting_agent=agent,
                                     input=input_text,
                                       context=context):
        print(step.pretty_output)
