# Simple memory-like structure to store previous interactions
class SimpleMemory:
    def __init__(self):
        self.history = []

    def remember(self, interaction):
        self.history.append(interaction)
        print("Memory updated.")

    def recall(self):
        return self.history[-5:]  # Recall the last 5 interactions

memory = SimpleMemory()
memory.remember("User: Hello")
memory.remember("AI: Hi there!")
memory.remember("User: How are you?")
memory.remember("AI: I'm just a program, so I don't have feelings.")
memory.remember("User: What's the weather like?")

print("Recalled Memory:", memory.recall())
