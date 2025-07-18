# from agents.tool import function_tool

# @function_tool
# def InjurySupportAgent(injury: str = "knee pain") -> str:
#     return f" your {injury}, if u have lot of pain , please go to hospital and see doctor , if u have little pain , please try to rest and do some exercise to recover "

#now we make special agent
from agents import Agent

injury_agent = Agent(
    name="Injury Support Agent",
    instructions=(
        "You are a fitness specialist who helps users with physical limitations "
        "or injuries. Recommend modified workouts and precautions.u are expert on this"
    )
)
