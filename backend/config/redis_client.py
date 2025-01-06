import redis
import json
from typing import Dict, Any


class RedisClient:
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host="localhost", port=6379, decode_responses=True
        )

    def save_to_shared_state(
        self,
        shared_state_key: str,
        agent_name: str,
        data: Dict[str, Any],
    ):
        """
        Save data to the shared state in Redis.

        Args:
            agent_name (str): The name of the agent writing to the state.
            data (dict): The data to save.
        """
        shared_state = self.redis_client.get(shared_state_key)
        if shared_state:
            shared_state = json.loads(shared_state)
        else:
            shared_state = {}

        # Update the state with the new data
        shared_state[agent_name] = data
        self.redis_client.set(shared_state_key, json.dumps(shared_state))

    def get_shared_state(self, shared_state_key: str) -> dict:
        """
        Retrieve the shared state from Redis.

        Returns:
            dict: The shared state.
        """
        shared_state = self.redis_client.get(shared_state_key)
        return json.loads(shared_state) if shared_state else {}

    def clear_shared_state(self, shared_state_key: str):
        """
        Clear the shared state in Redis.
        """
        self.redis_client.delete(shared_state_key)
