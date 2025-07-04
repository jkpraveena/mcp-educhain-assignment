from educhain import Educhain
import json

# Initialize Educhain client
client = Educhain()

# Set your topic
topic = "Python Programming Basics"

# Generate MCQs
mcq = client.qna_engine.generate_questions(
    topic=topic,
    num=3,
    question_type="Multiple Choice"
)

# Generate Lesson Plan
lesson = client.content_engine.generate_lesson_plan(
    topic=topic
)

# Combine and save the result in JSON format
output = {
    "topic": topic,
    "lesson_plan": lesson.model_dump(),  # dictionary format
    "multiple_choice_questions": mcq.model_dump()
}

with open("content.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Content generated and saved to content.json")
