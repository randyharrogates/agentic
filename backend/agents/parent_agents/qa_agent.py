from backend.utils.llm import LLM


class QAAgent:
    def __init__(self):
        self.llm = LLM(model_name="gpt-4")

    def validate_output(self, output: str) -> str:
        """
        Validate the generated output and suggest improvements if needed.

        Args:
            output (str): The generated output to validate.

        Returns:
            str: Validation result or suggestions from the LLM.
        """
        prompt = f"Validate the following output and suggest any necessary improvements:\n\n{output}"
        return self.llm.generate_response(prompt, max_tokens=200)
