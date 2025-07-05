
🧠 Health & Wellness Planner Agent
An AI-powered assistant built with the OpenAI Agents SDK that helps users:

Plan personalized meals 🍽️

Track fitness progress 📊

Stay consistent with their health goals ✅

Everything is tailored to the user’s preferences and lifestyle.

🚀 How It Works
The digital wellness agent chats naturally with users, understands their goals (like "lose 5 kg in 1 month"), and then offers customized support using different tools:

Meal plans

Workout recommendations

Progress tracking

Goal analysis

Injury support

Emergency escalation

🔧 Key Agents (with examples)
1. Escalation Agent
Handles emergency issues.

python
Copy
Edit
EscalationAgent("severe bleeding")
# → "your have 'severe bleeding' kindly contact to doctor. i cannot help more on this"
2. Injury Support Agent
Gives first-aid advice for common injuries.

python
Copy
Edit
InjurySupportAgent("shoulder pain")
# → "your shoulder pain... please go to hospital or rest based on pain level"
3. Nutrition Expert Agent
Gives diet tips based on user query.

python
Copy
Edit
NutritionExpertAgent("foods rich in Vitamin C")
# → "I suggest you consume foods rich in Vitamin C to maintain a healthy lifestyle."
🧰 Core Tools (tools/ folder)
Tool File	What It Does
goal_analyzer.py	Understands and structures health goals.
meal_planner.py	Suggests weekly meal plans.
scheduler.py	Schedules check-ins and tasks.
tracker.py	Tracks progress (like steps or calories).
workout_recommender.py	Recommends workouts based on user level.

📦 Data Models (Guardrails)
✅ GoalInput
Defines goal structure: type, quantity, unit, and duration.

✅ MealPlanOutput
List of meals like: ["Oats", "Grilled chicken"].

✅ WorkoutPlanOutput
Weekly plan like: {"Monday": "Jog", "Tuesday": "Pushups"}.

🧠 User Session Context
Stores user-specific data to personalize experience:

Name, ID

Goals

Diet preference

Meal/workout plans

Injury notes

Logs of agent actions (handoffs, progress, etc.)

🪝 Hooks System
Custom logging for agent/tool actions. Example:

csharp
Copy
Edit
[2025-07-05 20:30] (started): NutritionExpertAgent
[2025-07-05 20:31] Handoff from InjurySupportAgent to EscalationAgent
Also logs to session context to retain memory.

✅ Features
🎯 Goal Analyzer

🍲 7-Day Meal Planner

🏋️ Workout Recommender

📈 Progress Tracker

📅 Weekly Check-In Scheduler

🩺 Injury and Emergency Response

⚙️ Installation
Make sure Python is installed, then:

bash
Copy
Edit
# 1. Clone the repo
git clone <your-repo-url>
cd health-wellness-agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# 3. Install required libraries
pip install -r requirements.txt
# Or install manually:
pip install openai-agents litellm python-dotenv

# 4. Run the agent
python main.py
🛠 Tech Stack
Python 🐍

openai-agents SDK

LiteLLM

Python Dotenv

Let me k
