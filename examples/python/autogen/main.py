import os
from autogen import AssistantAgent, UserProxyAgent

# Warning: You must set OPENAI_API_KEY environment variable or provide a config_list.
# For simplicity, this example assumes OPENAI_API_KEY is available.

config_list = [
    {
        'model': 'gpt-4',
        'api_key': os.environ.get("OPENAI_API_KEY")
    }
]

llm_config = {"config_list": config_list, "seed": 42, "temperature": 0}

# Create an assistant agent named "assistant"
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

# Create a user proxy agent named "user_proxy"
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "coding"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

# the assistant receives a message from the user_proxy, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""What date is today? Compare the year-to-date gain for META and TESLA.""",
)
