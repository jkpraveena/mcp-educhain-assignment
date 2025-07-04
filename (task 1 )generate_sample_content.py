from educhain import Educhain
import json

# Initialize Educhain client
client = Educhain()

# Set your topic
topic = "Python Programming Basics"

# Generate MCQs
mcqs = client.qna_engine.generate_questions(
    topic=topic,
    num=5,
    question_type="Multiple Choice"
)

# Generate Lesson Plan
lesson = client.content_engine.generate_lesson_plan(
    topic=topic
)

# Simulate Flashcards using Short Answer type
short_answers = client.qna_engine.generate_questions(
    topic=topic,
    num=5,
    question_type="Short Answer"
)

# Format flashcards
flashcards = [
    {
        "question": q.question,
        "answer": q.answer
    }
    for q in short_answers.questions
]

# Combine and save the result in JSON format
output = {
    "topic": topic,
    "lesson_plan": lesson.model_dump(),  # dictionary format
    "multiple_choice_questions": mcqs.model_dump(),
    "flashcards": flashcards
}

# Save to JSON
with open("sample_responses.txt", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Content generated and saved to responses/sample_responses.json")
