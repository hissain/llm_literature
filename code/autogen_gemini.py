from dotenv import load_dotenv
import os

load_dotenv()

from autogen_ext.models.openai import OpenAIChatCompletionClient

# Configure the Gemini model client
model_client = OpenAIChatCompletionClient(
    model="gemini-pro",
    api_key=os.getenv("GEMINI_API_KEY"),
    api_type="google",
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "family": "unknown",
    },
)


from autogen_agentchat.agents import AssistantAgent

report_agent_gemini = AssistantAgent(
    name="Report_Agent",
    model_client=model_client,
    description="Generate a report based on a given topic",
    system_message=(
        "You are a helpful assistant. Your task is to synthesize data extracted into a high-quality "
        "literature review including CORRECT references. You MUST write a final report that is formatted "
        "as a literature review with CORRECT references. Your response should end with the word 'TERMINATE'."
    ),
)


from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

termination = TextMentionTermination("TERMINATE")
team = RoundRobinGroupChat(
    participants=[report_agent_gemini],
    termination_condition=termination
)


from autogen_agentchat.ui import Console

# await Console(
#     team.run_stream(
#         task="Write a literature review on no-code tools for building multi-agent AI systems",
#     )
# )
