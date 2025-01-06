from backend.utils.llm import LLM
from backend.agents.base_agent import BaseAgent


class PMAgent(BaseAgent):
    def __init__(self, model_name: str, temperature: float, requirements):
        super().__init__(model_name=model_name, temperature=temperature)
        self.requirements = requirements

    def process(self) -> str:
        """
        Generate a workflow based on the user's requirements.

        Args:
            requirements (str): User's requirements.

        Returns:
            str: The workflow description generated by the LLM.
        """
        prompt = f"Plan a multi-agent workflow for the following requirements:\n\n{self.requirements}"
        return self.llm.generate_response(prompt, max_tokens=300)
