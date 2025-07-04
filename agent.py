from agents import Agent
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool
from agentss.nutrition_expert_agent import NutritionExpertAgent
from agentss.injury_support_agent import InjurySupportAgent
from agentss.escalation_agent import EscalationAgent

health_agent = Agent(
    name="MainHealthPlanner",
    instructions="You're a caring assistant helping users reach health goals.",
    tools=[
        GoalAnalyzerTool,
        MealPlannerTool,
        WorkoutRecommenderTool,
        CheckinSchedulerTool,
        ProgressTrackerTool,
        NutritionExpertAgent,
        InjurySupportAgent,
        EscalationAgent
    ]
)
