# Project Title

convert the given booking document to desired json format using llm

## Setting Up Your Project

To set up the project, follow these steps:

### 1. Clone the repository

git clone git@github.com:godwin-fk/document_reader.git
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
_ Go to the Groq API dashboard.
_ Click on "Create New Key". \* Copy the generated API key.

### 5. Set up your environment variables

    * Paste it in the main.py where its needed or create a .env file in the root directory.
    * Add the following line: GROQ_API_KEY=your_api_key_here
    * Or you can use my own api_key for this project.(main.py)

### 6. Running the project

Execute:
python main.py
