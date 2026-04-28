import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
from niches_generator import NichesGenerator
from agent_replicator import AgentReplicator
from profit_multiplier import ProfitMultiplier

load_dotenv()

class InfiniteProfitEngine:
    def __init__(self):
        self.niches_gen = NichesGenerator()
        self.agent_replicator = AgentReplicator(initial_agents=1)
        self.profit_multiplier = ProfitMultiplier()
        self.cycle_count = 0
        self.running = True
    
    def run_cycle(self):
        """Run one complete profit generation cycle"""
        self.cycle_count += 1
        
        # Get agent count
        agents = self.agent_replicator.get_total_agents()
        niches = len(self.niches_gen.get_all_niches())
        
        # Calculate daily profit
        daily_profit = self.profit_multiplier.calculate_daily_profit(agents, niches)
        
        # Check for agent spawning
        new_agents = self.agent_replicator.spawn_agents(daily_profit)
        
        # Update multiplier
        if self.cycle_count % 10 == 0:
            self.profit_multiplier.apply_multiplier(1.15)
        
        return {
            "cycle": self.cycle_count,
            "agents": self.agent_replicator.get_total_agents(),
            "daily_profit": daily_profit,
            "new_agents_spawned": new_agents,
            "total_profit": self.profit_multiplier.get_total_profit(),
            "timestamp": datetime.now().isoformat()
        }
    
    def start(self):
        """Start the engine"""
        print("🚀 Infinite Profit Empire Engine Started!")
        print(f"Owner: {os.getenv('OWNER', 'Unknown')}")
        print(f"Mode: {os.getenv('MODE', 'production')}")
        
        while self.running:
            try:
                result = self.run_cycle()
                print(f"[Cycle {result['cycle']}] Agents: {result['agents']}, Daily: €{result['daily_profit']:.2f}")
                time.sleep(21600)  # 6 hours
            except KeyboardInterrupt:
                print("\nShutting down...")
                self.running = False
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(60)

if __name__ == "__main__":
    engine = InfiniteProfitEngine()
    engine.start()