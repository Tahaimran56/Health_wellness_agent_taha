from agent import create_health_agent 
from context import UserSessionContext
from agents import Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
from dotenv import load_dotenv
from agents.run import RunConfig
import asyncio, os
from utils.streaming import stream_response
from db.database import init_db, save_user_session, load_user_session
from report.pdf_generator import PDFReportGenerator
from config import model, config

load_dotenv()
set_tracing_disabled(disabled=True)

print("*" * 5 ,"Health and Wellness AI Agent", "*" * 5,"\n")
print("Type 'exit' or 'quit' to Finish.\n")
print("Type 'report' to generate a PDF report of your session.\n")

History_save = []

async def main():
    init_db()
    # Optionally allow user to load previous session
    while True:
        user_id = input("Enter your user ID to resume session (or press Enter to start new): ").strip()
        if not user_id:
            user_context = UserSessionContext(name="khaid", uid=1001)
            break
        try:
            user_id_int = int(user_id)
            user_context = load_user_session(user_id_int)
            if user_context:
                print(f"[Session loaded for user: {user_context.name} (ID: {user_context.uid})]")
            else:
                print("No previous session found. Starting new session.")
                user_context = UserSessionContext(name="Muhammad Ubaid Raza", uid=user_id_int)
            break
        except ValueError:
            print("Please enter a valid numeric user ID or press Enter to start a new session.")

    while True:
        prompt = input("🧑 You : ")
        if prompt.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        if prompt.lower() == 'report':
            # Generate PDF report
            context_dict = user_context.model_dump()
            pdf_gen = PDFReportGenerator(context_dict)
            pdf_gen.generate_report()
            continue

        user_context.messages.append({"role": "user", "content": prompt})
        health_agent = create_health_agent(model)

        try:
            result = Runner.run_streamed(
                health_agent,
                prompt,
                context=user_context,
                run_config=config
            )
            await stream_response(result, user_context)
            user_context.messages.append({"role": "assistant", "content": result.final_output})
            # Save session after each interaction
            save_user_session(user_context)

        except Exception as e:
            if "InputGuardrailTripwireTriggered" in str(e):
                print("🛑 [Guardrail] Input not allowed (off-topic or unsafe).")

                # 🎯 Assistant explains what kind of input is expected
                fallback_response = (
                    "⚠️ Your input does not seem related to health, wellness, fitness, or nutrition. "
                    "I can only assist with those topics.\n"
                    "Please try again with a relevant question (e.g. 'I want to lose 5kg in 2 months')."
                )

                await stream_response(fallback_response, user_context)

            else:
                print(f"❌ [Unhandled Error] {e}")
                await stream_response("⚠️ Sorry, an unexpected error occurred.", user_context)

if __name__ == "__main__":
    asyncio.run(main())
