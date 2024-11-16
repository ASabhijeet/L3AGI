from XAgent import XAgent, Tool
from typing import Any, Dict

# Define the calculator function with type hints
def calculator_function(expression: str) -> str:
    """Evaluates a mathematical expression and returns the result as a string."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error in calculation: {e}"

# Define the function to get the weather with type hints
def get_weather() -> str:
    """Returns a string with the current weather conditions."""
    # Placeholder for weather retrieval logic
    return "The weather today is sunny with a high of 75°F."

# Create a list of tools for the XAgent
def create_tools() -> Dict[str, Tool]:
    """Creates and returns a dictionary of tools for the XAgent."""
    return {
        "Calculator": Tool(name="Calculator", func=calculator_function),
        "Weather": Tool(name="Weather", func=get_weather),
    }

# Initialize the XAgent with the configured tools
def main() -> None:
    """Main function to initialize the agent and process queries."""
    tools = create_tools()
    agent = XAgent(tools=list(tools.values()))

    # Define the query to get the weather
    response = agent.query("What is the weather today?")
    print(response)

if __name__ == "__main__":
    main()