# Building a Support Agent Chatbot for CDP "How-to" Questions

## Overview
This project is a chatbot designed to assist users with "How-to" questions related to CDP (Customer Data Platform). The chatbot leverages machine learning and NLP (Natural Language Processing) techniques to provide automated responses, reducing the workload on human support agents.

## Features
- NLP-based question-answering
- Machine learning model for understanding queries
- Predefined knowledge base for CDP-related queries
- Easy-to-use interface

### Output
![Image](https://github.com/user-attachments/assets/b6a12598-5549-4733-ba58-88cec3242faf)

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Flask (for the web interface)
- Required Python libraries (listed in `requirements.txt`)
  

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/RagunathJeyakumar/Support-Agent-Chatbot-for-CDP-How-to-Questions.git
   cd Support-Agent-Chatbot-for-CDP-How-to-Questions
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the chatbot server:
   ```sh
   py app.py
   ```
4. Open the application in your browser at `http://localhost:5000`

## Usage
- Ask the chatbot CDP-related "How-to" questions.
- The chatbot processes the question and provides a response.
- If the chatbot cannot answer, it provides suggestions or alternative queries.

## Technologies Used
- **Python**: Backend development
- **Flask**: Web framework
- **NLTK / SpaCy**: Natural Language Processing
- **Machine Learning**: Training models for understanding queries
- **HTML, CSS, JavaScript**: Frontend UI



