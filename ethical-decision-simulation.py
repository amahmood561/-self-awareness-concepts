# Rule-based ethical simulation
def ethical_decision_simulation(action):
    rules = {
        "harm": "Action not allowed: Causes harm",
        "benefit": "Action allowed: Provides benefit",
        "neutral": "Action allowed: No impact",
    }
    decision = rules.get(action, "Unknown action")
    return decision

# Test actions
actions = ["harm", "benefit", "neutral", "help"]

for action in actions:
    print(f"Decision for '{action}': {ethical_decision_simulation(action)}")
