from XAgent import XAgent
# Initialize the XAgent with the desired configuration
agent = XAgent(config={"model": "gpt-3.5-turbo"})

# Define the query to be sent to the agent
query = "What is 2 + 2?"

try:
    # Get the response from the agent
    response = agent.query(query)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


eval_config = {
    "criteria": ["helpfulness", "conciseness"],
    "input_key": "input",
}

# You can run evaluations or further interactions here if required.
def evaluate_agent(eval_config):
    # Add your evaluation logic here
    pass

# Call the evaluation function
evaluate_agent(eval_config)

# Initialize the XAgent with the desired configuration
agent = XAgent(config={"model": "gpt-3.5-turbo"})

# Define the query to be sent to the agent
query = "What is 2 + 2?"

# Get the response from the agent
response = agent.query(query)

# Print the response
print(response)

# If you want to evaluate the agent's performance, you can add evaluation logic here
# For example, you might want to run evaluations on a dataset or specific criteria.
# This part is optional and can be customized based on your needs.

# Example evaluation configuration (if needed)
# eval_config = {
#     "criteria": ["helpfulness", "conciseness"],
#     "input_key": "input",
# }

# You can run evaluations or further interactions here if required.