import random

def futurePrediction(name1: str) -> str:
    careers = [
        "software engineer", "doctor", 
        "lawyer", "teacher", "artist",
        "entrepreneur", "scientist", 
        "musician", "architect", "chef",
        "engineer", "journalist", 
        "psychologist", "designer", "consultant",
        "nurse", "researcher", "manager", 
        "analyst", "inventor"
    ]
    
    marriage_ages = list(range(25, 40))
    kids_counts = list(range(0, 4))
    success_levels = ["very successful", "successful", 
    "somewhat successful", "moderately successful"]
    
    name = sum(ord(c) for c in name1)
    
    random.seed(name)
    career = random.choice(careers)
    marriage_age = random.choice(marriage_ages)
    kids_count = random.choice(kids_counts)
    success = random.choice(success_levels)
    
    kids_str = "kids" if kids_count != 1 else "kid"
    kids_phrase = f"with {kids_count} {kids_str}" if kids_count > 0 else "with no kids"
    
    return f"{name1} will be a {career} and get married at {marriage_age} {kids_phrase} and you will be {success}"

