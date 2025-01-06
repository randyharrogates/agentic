import openai
from backend.config.logger import logger

class LLM:

    def __init__(
        self,
        model_name: str = "gpt-4",
        temperature: float = 0.7,
        dev_msg: str = "You are a developer.",
        user_msg: str = "You are a user.",
        max_tokens: int = 150,
    ):
        """
        Initialize the LLM class with model name and temperature.

        Args:
            model_name (str): The model to use (e.g., "gpt-4").
            temperature (float): Sampling temperature for diversity in outputs.
        """
        self.model_name = model_name
        self.temperature = temperature
        self.dev_msg = dev_msg
        self.user_msg = user_msg
        self.max_tokens = max_tokens

    def generate_response(self) -> str:
        """
        Generate a response from the LLM based on the given prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            max_tokens (int): Maximum number of tokens in the output.

        Returns:
            str: The generated response from the LLM.
        """
        try:
            response = openai.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "developer",
                        "content": [{"type": "text", "text": self.dev_msg}],
                    },
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": self.user_msg}],
                    },
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            logger.error(f"Error interacting with LLM: {e}")
            return "An error occurred while generating a response."
