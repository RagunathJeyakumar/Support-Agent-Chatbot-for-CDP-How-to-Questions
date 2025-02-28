from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize

# Initialize Flask app
app = Flask(__name__)

# Simulated documentation
docs = {
    'segment': """# Segment Documentation\n## Setting up a Source in Segment:\n1. Navigate to the Sources tab in your Segment workspace.\n2. Click "Add Source" and choose the source type (e.g., Web, Mobile App).\n3. Follow the setup steps, including adding your integration key.""",
    'mparticle': """# mParticle Documentation\n## Setting up User Profiles:\n1. Go to the User Profiles section.\n2. Click "Create User Profile" and add essential details like user ID and attributes.\n3. Link the user profile to events or actions.""",
    'lytics': """# Lytics Documentation\n## Audience Segmentation in Lytics:\n1. Go to the Audiences section of the Lytics platform.\n2. Click "Create Audience" and select segmentation criteria like demographics, actions, or behavior.\n3. Apply filters and save the audience for future use.""",
    'zeotap': """# Zeotap Documentation\n## Integrating Zeotap with Other Platforms:\n1. Go to the Integrations tab.\n2. Select the platform or tool to connect with Zeotap.\n3. Follow the steps to complete the integration and verify successful syncing."""
}

# Function to process query and extract detailed answers
def search_docs(query):
    query_tokens = word_tokenize(query.lower())
    response = ""
    found = False

    # Check for comparison questions
    if "compare" in query.lower() or "comparison" in query.lower():
        platforms = [p for p in docs.keys() if p in query.lower()]
        if len(platforms) >= 2:
            response = f"Comparing {platforms[0]} and {platforms[1]}:\n"
            for platform in platforms:
                response += f"{platform.capitalize()}:\n{docs[platform]}\n"
            return response
        elif len(platforms) == 1:
            response = f"{platforms[0].capitalize()}:\n{docs[platforms[0]]}\n"
            return response
        else:
            return "Please specify two platforms to compare (e.g., 'Segment vs Lytics')."

    # Search for specific how-to steps
    for platform, content in docs.items():
        # Only proceed if the platform name or a specific keyword is in the query
        specific_keywords = ['source', 'profile', 'audience', 'integrate', 'integration', 'set', 'create', 'segmentation']
        if (platform in query.lower()) or (any(token in content.lower() for token in query_tokens if token in specific_keywords)):
            lines = content.split('\n')
            relevant_section = []
            for i, line in enumerate(lines):
                if any(token in line.lower() for token in query_tokens if token in specific_keywords or platform in line.lower()):
                    if line.startswith('#'):
                        relevant_section.append(line)
                    elif line.strip():
                        relevant_section.append(line)
            if relevant_section:
                response += f"{platform.capitalize()}:\n" + "\n".join(relevant_section) + "\n"
                found = True
            break

    if not found:
        response = "Sorry, I couldn’t find relevant information for your query."
    return response

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = search_docs(user_input)
    return response

if __name__ == '__main__':
    nltk.download('punkt')  # Ensure NLTK tokenizer is available
    app.run(debug=True)