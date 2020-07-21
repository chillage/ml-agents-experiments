import mlagents
from mlagents_envs.registry import default_registry

env_id = 'FoodCollector'
env = default_registry[env_id].make()
env.reset()

