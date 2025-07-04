**READ IN CODE VIEW FOR BETTER FORMAT**


# mcp-educhain-assignment
EduChain MCP Server Integration – This project implements an MCP server using the EduChain library to generate educational content such as multiple-choice questions, lesson plans, and flashcards. The server is fully compatible with Claude Desktop and demonstrates tool/resource integration via the Model Context Protocol (MCP).

📚 EduChain MCP Server Integration with Claude Desktop

This project demonstrates how to build a Model Context Protocol (MCP) server using the EduChain library and integrate it with Claude Desktop. The server provides tools and resources to generate educational content such as MCQs and lesson plans on demand.

🚀 Features
	•	✅ MCP-compliant server using Python
	•	✅ Educational content generation using EduChain
	•	✅ Seamless integration with Claude Desktop via claude_desktop_config.json
	•	✅ Tools:
	•	Generate Multiple-Choice Questions (MCQs) and Flashcards 
	•	✅ Resources:
	•	Generate Lesson Plan
	•	✅ Bonus:
	•	Sample content generator script
	•	Sample responses exported as .txt

🏗️ Project Structure

mcp-educhain-assignment/
├── mcp_server.py                    # Main MCP server
├── .env                             # Environment file with your OPENAI_API_KEY
├── claude_desktop_config.json       # Claude Desktop config (excluded in .gitignore)
├── README.md                        # You're reading it!
├── (task 1)generate_content.py      # Script to generate lesson plan and MCQs
│── (task 1)sample_responses.txt     # Saved responses in plain text
Proofs of final outcome is added in the form screenshots and videos in the directory

⸻

🧪 Setup Instructions

1. Clone the repo

git clone https://https://github.com/jkpraveena/mcp-educhain-assignment.git
cd mcp-educhain-assignment

2. Set up environment

Create a .env file with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

3. Run the MCP server

python mcp_server.py

4. Configure Claude Desktop

Update your claude_desktop_config.json:

{
  "command": "/path/to/python3",
  "args": ["/path/to/mcp_server.py"]
}

💡 For security, this config is excluded from GitHub via .gitignore.
