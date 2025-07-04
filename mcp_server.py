# TASK 2 FROM THE GIVEN ASSIGNMENT


# mcp_server.py

from mcp.server.fastmcp import FastMCP
from educhain import Educhain

from dotenv import load_dotenv
load_dotenv()  # Load from .env file

import os
api_key = os.getenv("OPENAI_API_KEY")

# Initialize EduChain
client = Educhain()

# Create the MCP server
mcp = FastMCP("EduChain MCP Server")


# 🛠️ TOOL: Generate MCQs
@mcp.tool()
def generate_mcqs(topic: str = "Python Programming Basics"):
    """
    Generate multiple-choice questions for the given topic using EduChain.
    """
    mcqs = client.qna_engine.generate_questions(
        topic=topic,
        num=3,
        question_type="Multiple Choice"
    )
    return mcqs.model_dump()
# 🧠 TOOL: Generate Flashcards
@mcp.tool()
def generate_flashcards(topic: str = "Python Programming Basics"):
    """
    Generate flashcards for the given topic using EduChain.
    """
    flashcards = client.qna_engine.generate_flashcards(topic=topic)
    return flashcards.model_dump()

# 📚 RESOURCE: Get lesson plan
@mcp.resource("lesson://{topic}")
def get_lesson_plan(topic: str = "Python Programming Basics"):
    """
    Generate a lesson plan for the given topic using EduChain.
    """
    lesson = client.content_engine.generate_lesson_plan(topic=topic)
    return lesson.model_dump()


# 🚀 Start the server
if __name__ == "__main__":
    print("🚀 MCP server starting...")
    mcp.run()
    print("✅ MCP server shut down.")
