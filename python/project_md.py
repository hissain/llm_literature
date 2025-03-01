import os
import autogen
from typing import List, Dict, Any
from dotenv import load_dotenv

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen

load_dotenv()

config_list_file_name = ".config_list"

gemini_config_list = config_list_from_json(config_list_file_name, filter_dict={"tags": ["gemini"]})
gemini_llm_config = {"config_list": gemini_config_list, "timeout": 120}

code_execution_config={
        "last_n_messages": 3,
        "work_dir": "paper_review",
        "use_docker": False,
    }

llm_config = {
    "config_list": gemini_llm_config,
    "temperature": 0.2,
    "seed": 42,
}

# Create the assistant agent
assistant = autogen.AssistantAgent(
    name="Project_Document_Creator_Agent",
    llm_config=gemini_llm_config,
    system_message="""You are an expert on creating readme.md markdown creator.
    Your task is as followings:
    1. Read all the folders and files in the current directory and subdirectories.
    2. You can use `tree` command to know the files.
    3. Read all the files and try to understand the purpose of the project.
    4. Generate a PROJECT.MD markdown file for this project which I can use as Github readme.
    5. Save the file in the current directory.
"""
)

# Create the user proxy agent to execute code
user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "research_workspace",
        "use_docker": False,
    }
)

def generate_technical_review():
    """Initialize the conversation between agents to generate a technical review."""
    
    user_proxy.initiate_chat(
        assistant,
        message=f"""Your task is to get the job of Project_Document_Creator_Agent done."""
    )

# Example usage
if __name__ == "__main__":
    if not os.path.exists("documentation"):
        os.makedirs("documentation")
    generate_technical_review()