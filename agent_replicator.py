import json
import random
from datetime import datetime
from typing import Dict, List

class AgentReplicator:
    def __init__(self, initial_agents: int = 1):
        self.agents = initial_agents
        self.agent_history = []
        self.profit_threshold = 500  # €500 to spawn new agent
        self.multiplication_factor = 2.0
    
    def spawn_agents(self, current_profit: float) -> int:
        """Spawn new agents based on profit threshold"""
        new_agents = 0
        while current_profit >= self.profit_threshold:
            new_agents += 1
            current_profit -= self.profit_threshold
            self.agents += 1
            
        return new_agents
    
    def replicate(self, agent_id: int) -> Dict:
        """Replicate an agent"""
        new_agent = {
            "id": self.agents,
            "parent_id": agent_id,
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "efficiency": random.uniform(0.9, 1.1)
        }
        self.agents += 1
        self.agent_history.append(new_agent)
        return new_agent
    
    def get_total_agents(self) -> int:
        return self.agents
    
    def get_agent_productivity(self) -> float:
        base_productivity = 1.0
        return base_productivity * (1 + (self.agents / 100) * 0.05)

if __name__ == "__main__":
    replicator = AgentReplicator()
    print(f"Starting agents: {replicator.get_total_agents()}")
    new = replicator.spawn_agents(5000)
    print(f"After profit €5000: {replicator.get_total_agents()} agents (spawned {new})")