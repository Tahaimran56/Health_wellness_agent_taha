from agents import Agent
from guardrails import health_input_guardrail
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool
from agentss.nutrition_expert_agent import nutrition_agent
from agentss.injury_support_agent import injury_agent
from agentss.escalation_agent import escalation_agent

health_agent = Agent(
    name="MainHealthPlanner",
    instructions="You're a caring assistant helping users reach health goals. if user has a goal, you should help them achieve it.",
    tools=[
        GoalAnalyzerTool,
        MealPlannerTool,
        WorkoutRecommenderTool,
        CheckinSchedulerTool,
        ProgressTrackerTool,
    ],
    handoffs=[
        escalation_agent,
        nutrition_agent,
        injury_agent,
    ],
guardrails=[health_input_guardrail]
)
