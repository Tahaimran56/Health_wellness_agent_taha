from agents.tool import function_tool

@function_tool
def InjurySupportAgent(injury: str = "knee pain") -> str:
    return f" your {injury}, if u have lot of pain , please go to hospital and see doctor , if u have little pain , please try to rest and do some exercise to recover "

