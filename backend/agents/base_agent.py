from backend.interface.agent_interface import AgentInterface
from utils.llm import LLM


class BaseAgent(AgentInterface):
    """
    Base class for all agents. Implements shared functionality.
    """

    def __init__(
        self,
        model_name: str,
        temperature: float,
        dev_msg: str,
        user_msg: str,
        max_tokens: int,
    ):
        """
        Initialize the BaseAgent with an LLM instance.

        Args:
            model_name (str): The name of the LLM model.
            temperature (float): The temperature for LLM responses.
        """
        self.llm = LLM(
            model_name=model_name,
            temperature=temperature,
            dev_msg=dev_msg,
            user_msg=user_msg,
            max_tokens=max_tokens,
        )

    def process(self) -> str:
        """
        Default implementation of the process method.

        Args:
            input_data (str): The input data to process.

        Returns:
            str: The response generated by the LLM.
        """
        raise NotImplementedError("Each agent must implement the `process` method.")