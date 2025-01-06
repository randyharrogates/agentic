from typing import Dict, Any
from backend.agents.base_agent import BaseAgent
from backend.config.logger import logger


class BAEvaluatorAgent(BaseAgent):
    """
    BA Validator Agent responsible for comparing Input Agent's outputs with
    BA Agent's outputs using an LLM.
    """

    def __init__(
        self,
        model_name: str,
        temperature: float,
        max_tokens: int,
    ):
        """
        Initialize the BA Validator Agent.

        Args:
            model_name (str): LLM model to use.
            temperature (float): LLM temperature setting.
            max_tokens (int): Maximum tokens for the LLM response.
            input_agent_output (str): The output from the Input Agent.
            ba_agent_output (str): The output from the BA Agent.
        """
        self.shared_state_key = "ba_workflow"
        self.agent_name = "BAEvaluatorAgent"
        self.state = self.redis_client.get_shared_state(self.shared_state_key)
        input_agent_output = self.state.get("InputAgent", "")
        ba_agent_output = self.state.get("BAAgent", "")
        dev_msg = """
        You are an evaluation agent tasked to evaluate if user inputs
        matches the requirements output.
        """
        user_msg = f"""
        The following are the outputs to compare:\n
        
        **Input Agent Output**:\n
        {input_agent_output}

        **BA Agent Output**:\n
        {ba_agent_output}

        Your task is to evaluate if the BA Agent's output adequately aligns 
        with the Input Agent's output.\n 
        If the alignment is insufficient, provide reasons for the misalignment.
        Else if the alignment is sufficient, return a single word 'confirmation'.
        """
        super().__init__(
            model_name=model_name,
            temperature=temperature,
            dev_msg=dev_msg,
            user_msg=user_msg,
            max_tokens=max_tokens,
        )
        self.agent_name = "BAEvaluatorAgent"

    def process(self) -> Dict[str, Any]:
        """
        Validate the alignment between Input Agent and BA Agent outputs.

        Returns:
            dict: Validation result indicating success or failure, with feedback.
        """
        logger.info("Validating alignment between Input Agent and BA Agent outputs...")
        response = self.llm.generate_response()
        logger.info(f"Response for {self.agent_name}: {response}")
        # Simulating LLM interpretation of response
        self.redis_client.save_to_shared_state(
            agent_name=self.agent_name,
            shared_state_key=self.shared_state_key,
            data=response,
        )
        if response.lower().strip() == "confirmation":
            logger.info("Validation successful: Input and BA outputs are aligned.")
            return True, self.state
        logger.warning("Validation failed: Misalignment detected.")
        return False, self.state
