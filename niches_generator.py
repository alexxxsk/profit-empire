import json
import random
from typing import List, Dict

class NichesGenerator:
    def __init__(self):
        self.niches = [
            {"name": "AI & Automation", "potential": 9.8, "competition": 8.5},
            {"name": "Cryptocurrency", "potential": 9.5, "competition": 9.0},
            {"name": "Remote Work", "potential": 9.2, "competition": 8.0},
            {"name": "Digital Products", "potential": 9.0, "competition": 7.5},
            {"name": "Passive Income", "potential": 9.5, "competition": 8.8},
            {"name": "E-commerce", "potential": 8.8, "competition": 8.2},
            {"name": "Social Media Marketing", "potential": 8.5, "competition": 7.8},
            {"name": "SEO Mastery", "potential": 9.0, "competition": 8.0},
            {"name": "Freelancing", "potential": 8.2, "competition": 7.0},
            {"name": "Personal Branding", "potential": 8.5, "competition": 7.5},
            {"name": "Content Creation", "potential": 8.8, "competition": 7.2},
            {"name": "Dropshipping", "potential": 8.0, "competition": 8.5},
            {"name": "Affiliate Marketing", "potential": 9.2, "competition": 8.5},
            {"name": "Video Marketing", "potential": 9.0, "competition": 7.8},
            {"name": "Email Marketing", "potential": 8.8, "competition": 7.0},
            {"name": "Coaching & Consulting", "potential": 9.0, "competition": 7.8},
            {"name": "Software as Service", "potential": 9.5, "competition": 8.8},
            {"name": "Mobile App Development", "potential": 9.2, "competition": 8.5},
            {"name": "Online Courses", "potential": 9.0, "competition": 8.0},
            {"name": "Niche Blogging", "potential": 8.5, "competition": 6.5},
        ]
    
    def get_all_niches(self) -> List[Dict]:
        return self.niches
    
    def get_best_niches(self, count: int = 10) -> List[Dict]:
        scored = [(n, n['potential'] - (n['competition'] * 0.3)) for n in self.niches]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [n[0] for n in scored[:count]]
    
    def generate_content_ideas(self, niche: str, count: int = 5) -> List[str]:
        ideas = {
            "AI & Automation": [
                "How AI is changing jobs in 2026",
                "Top 10 AI tools for productivity",
                "Automation business ideas",
                "Future of work with AI",
                "AI for small business owners"
            ],
            "Cryptocurrency": [
                "Bitcoin investment guide 2026",
                "Best crypto wallets",
                "DeFi explained simply",
                "Blockchain for beginners",
                "Crypto trading strategies"
            ],
        }
        return ideas.get(niche, [f"{niche} tip {i}" for i in range(1, count+1)])

if __name__ == "__main__":
    gen = NichesGenerator()
    print("All niches:", len(gen.get_all_niches()))
    print("Best niches:", gen.get_best_niches(5))