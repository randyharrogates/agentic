from typing import Dict, Any
from backend.agents.parent_agents.input_agent import InputAgent
from backend.agents.parent_agents.ba_agent import BAAgent
from backend.agents.parent_agents.ba_evaluator_agent import BAEvaluatorAgent
from backend.config.logger import logger


def run_ba_workflow(inputs: Dict[str, Any]) -> str:
    confirmation = True
    counter = 0
    while confirmation:
        logger.info(f"Running BA Workflow...for iteration: {counter}")
        input_agent = InputAgent(
            model_name="gpt-4",
            temperature=0.7,
            max_tokens=3000,
            inputs=inputs,
        )
        ba_agent = BAAgent(
            model_name="gpt-4",
            temperature=0.7,
            max_tokens=3000,
        )
        ba_evaluator = BAEvaluatorAgent(
            model_name="gpt-4",
            temperature=0.7,
            max_tokens=3000,
        )
        input_agent.process()
        ba_agent.process()
        confirmation, state = ba_evaluator.process()
        counter += 1
    return state.get("BAAgent", "")
