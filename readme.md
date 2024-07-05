# Project Title

A brief description of what this project does and who it's for.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python.
- You have a Windows/Linux/Mac machine.

## Setting Up Your Project

To set up the project, follow these steps:

### 1. Clone the repository

git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname

### 2. Create a virtual environment

For Windows:
python -m venv venv
.\venv\Scripts\activate
For Linux/Mac:
python3 -m venv venv
source venv/bin/activate

### 3. Install the required packages

pip install -r requirements.txt

### 4. Create a Groq API Key

To use Groq services, you need to create an API key. Follow these steps:

### 5. Set up your environment variables

Go to the Groq API dashboard.
Navigate to the API Keys section.
Click on "Create New Key".
Copy the generated API key.
Paste it in the main.py where its needed or create a .env file in the root directory and add the following line: GROQ_API_KEY=your_api_key_here or you can use my own api_key for this project.(main.py)

### 6. Running the project

To run the project, execute:
python main.py
