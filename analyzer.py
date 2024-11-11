import openai  # Import the OpenAI library to interact with OpenAI's API for language model services
from openai import OpenAI  # Import the OpenAI class specifically for creating a client instance with API key authentication
import time  # Import the time module to introduce delays in case of rate limiting, which helps prevent exceeding usage limits

# Initialize the OpenAI client with your API key
# - This API key authenticates your client and allows it to send requests to OpenAI's API
# - Replace 'your-api-key-here' with your actual API key to enable OpenAI access
client = OpenAI(api_key='your-api-key-here')

# Define a function that retries requests to the API if a rate limit error occurs
# This helps manage usage limits by pausing between attempts, giving time for limits to reset
def request_with_retry(question):
    """
    Sends a code snippet to OpenAI and retries if the request is rate-limited.

    Args:
        question (str): The prompt or code snippet to send to OpenAI for analysis.

    Returns:
        str: The response from OpenAI with suggestions or analysis, or a failure message if retries fail.
    """
    max_retries = 3  # Define the maximum number of times to retry the request if rate-limited
    retry_delay = 10  # Set the delay (in seconds) between retries to help prevent rapid requests in succession
    retries = 0  # Initialize a counter to keep track of how many times the request has been retried

    # Retry loop that attempts to send the request up to max_retries times
    while retries < max_retries:  # Continue attempting while the retry count is below the max
        try:
            # Send a request to the OpenAI API using the GPT-4 model
            # - `client.chat.completions.create` is a method to interact with OpenAI models in a chat-like structure
            # - This approach simulates a conversation with a model by specifying roles for messages
            response = client.chat.completions.create(
                model="gpt-4",  # Specify the GPT-4 model to use, as it provides advanced capabilities for analyzing code
                messages=[  # Create a list of message dictionaries representing a conversation history
                    {"role": "user", "content": question},  # The user's message in the "chat" with the model
                    # - "role": "user" indicates that this is a message from the user
                    # - "content": question sends the actual text (e.g., code snippet) that we want analyzed
                ]
            )

            # If the request is successful, return the response from OpenAI
            # - `response.choices[0].message.content` accesses the actual text of the AI’s response
            #   - `choices`: List of response options (usually one response in typical single-prompt usage)
            #   - `choices[0]`: Select the first response in the list of possible completions
            #   - `.message.content`: Access the main text of the assistant's reply, containing analysis or suggestions
            return response.choices[0].message.content  # Return the model's response to the user's question

        # Handle rate limit errors if too many requests have been sent in a short time
        except openai.RateLimitError as e:
            # Inform the user of a rate limit error and the retry delay before the next attempt
            print(f"Rate limit error: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)  # Wait for `retry_delay` seconds to give time for rate limits to reset
            retries += 1  # Increment the retry counter to keep track of retry attempts

        # Handle any other errors that occur, and exit the loop if they happen
        except Exception as e:
            # Print an error message for any non-rate limit errors encountered
            print(f"Error: {e}")
            break  # Exit the retry loop in the case of any unexpected errors

    # Return a failure message if the maximum number of retries is reached without success
    return "Failed to get a response due to rate limits or other errors."

# Define a function that prepares the code for analysis by the OpenAI API
# This function is responsible for constructing a prompt that describes the task to the AI
# and sending it to OpenAI for processing
def analyze_code(code_snippet):
    """
    Sends a code snippet to OpenAI for analysis, including error detection and efficiency suggestions.

    Args:
        code_snippet (str): The user's code to be analyzed by OpenAI.

    Returns:
        str: The analysis or suggestions provided by OpenAI for the given code.
    """
    # Construct a prompt that describes the analysis task to OpenAI
    # - This prompt provides context by instructing the model to identify errors and suggest improvements
    # - `code_snippet` is the user's code, inserted into the prompt for analysis
    prompt = f"Here's some code:\n\n{code_snippet}\n\nPlease identify any errors and suggest improvements for efficiency."

    # Call the request_with_retry function to send the prompt to OpenAI for analysis
    # - Pass `prompt` as an argument, and retrieve the result from OpenAI or a failure message
    return request_with_retry(prompt)  # Return the response from OpenAI, containing analysis or suggestions
