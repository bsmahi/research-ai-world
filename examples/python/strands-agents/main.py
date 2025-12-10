from strands_agents import Agent, Tool
from strands_agents_tools import python_tool

# Example tool definition
@python_tool
def get_weather(location: str):
    """Returns the weather for a given location."""
    return f"The weather in {location} is sunny."

# Create an agent
agent = Agent(
    name="WeatherBot",
    model="claude-3-sonnet", # Example model reference
    tools=[get_weather],
    instructions="You are a helpful assistant that can check the weather."
)

# Run the agent (conceptual usage)
print("Agent initialized. Running task...")
# response = agent.run("What is the weather in San Francisco?")
# print(response)

print("Strands Agent Setup Complete.")
