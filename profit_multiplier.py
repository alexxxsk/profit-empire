import json
from datetime import datetime
from typing import Dict

class ProfitMultiplier:
    def __init__(self):
        self.base_revenue_streams = {
            "adsense": {"rate": 2.5, "views_needed": 1000},
            "affiliate": {"rate": 15.0, "conversions_needed": 100},
            "products": {"rate": 45.0, "sales_needed": 50},
            "sponsorships": {"rate": 500.0, "deals_needed": 5},
            "email": {"rate": 3.0, "subscribers_needed": 10000}
        }
        self.multiplier = 1.0
        self.total_profit = 0.0
    
    def calculate_daily_profit(self, agents: int, niches: int) -> float:
        base_income = agents * niches * 0.75
        multiplied = base_income * self.multiplier
        self.total_profit += multiplied
        return multiplied
    
    def apply_multiplier(self, factor: float) -> None:
        self.multiplier *= factor
    
    def reinvest_profit(self, profit: float, reinvest_percent: float = 0.1) -> Dict:
        reinvested = profit * (reinvest_percent / 100)
        kept = profit - reinvested
        
        return {
            "total": profit,
            "reinvested": reinvested,
            "to_bank": kept,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_total_profit(self) -> float:
        return self.total_profit

if __name__ == "__main__":
    multiplier = ProfitMultiplier()
    daily = multiplier.calculate_daily_profit(8427, 32)
    print(f"Daily profit: €{daily:.2f}")