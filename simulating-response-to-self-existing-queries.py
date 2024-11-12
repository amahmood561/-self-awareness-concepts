# Response to questions about self-awareness
def respond_to_existence_question(question):
    if "are you self-aware" in question.lower():
        return "I am not self-aware. I am a program that responds to inputs based on pre-learned patterns."
    elif "do you exist" in question.lower():
        return "I exist as a program running on a computer, but I have no consciousness or subjective experience."
    else:
        return "I'm here to help you with your questions."

# Test existence questions
questions = ["Are you self-aware?", "Do you exist?", "What are you?"]

for question in questions:
    print(f"Q: {question}")
    print("A:", respond_to_existence_question(question))
