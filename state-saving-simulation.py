# State-tracking class without awareness
class SystemState:
    def __init__(self):
        self.state = {}

    def update_state(self, key, value):
        self.state[key] = value
        print(f"State updated: {key} = {value}")

    def get_state(self, key):
        return self.state.get(key, "Unknown state")

# Test state tracking
system_state = SystemState()
system_state.update_state("mood", "neutral")
system_state.update_state("temperature", 25)
print("Current mood:", system_state.get_state("mood"))
print("Current temperature:", system_state.get_state("temperature"))
