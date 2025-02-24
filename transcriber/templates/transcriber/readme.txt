# Speech Recognition App

A real-time speech recognition application using Django and Vosk.

## Setup Instructions

1. Clone the repository:
```bash
git clone [your-repository-url]
cd speech_recognition



    Create a README.md file to guide your teammate:

    
# Speech Recognition App

A real-time speech recognition application using Django and Vosk.

## Setup Instructions

1. Clone the repository:
```bash
git clone [your-repository-url]
cd speech_recognition

    

    Create and activate virtual environment:

    
python3 -m venv speech_env
source speech_env/bin/activate  # On Windows: speech_env\Scripts\activate

    

    Install dependencies:

    
pip install -r requirements.txt

    

    Download Vosk model:

    
mkdir vosk_model
cd vosk_model
# Download and extract the model
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip

    

    Run the server:

    
daphne -b 0.0.0.0 -p 8000 speech_recognition.asgi:application

    

    Visit http://localhost:8000 in your browser

Required Software

    Python 3.x
    pip
    Virtual environment

    

3. Create a `.gitignore` file:

    

.gitignore

*.pyc
pycache/
*.pyo
*.pyd
.Python
env/
speech_env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
*.log
.env
.venv
venv/
ENV/
VS Code

.vscode/
PyCharm

.idea/
Vosk model (optional - depending on size)

vosk_model/
Database

db.sqlite3

    

4. Initialize git and push to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin [your-github-repo-url]
git push -u origin main

    

    Your project structure should look like:

    
speech_recognition/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── speech_recognition/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── transcriber/
    ├── __init__.py
    ├── consumers.py
    ├── views.py
    └── templates/
        └── transcriber/
            └── index.html

    

To create all these files:

    Generate requirements.txt:

    
# Make sure you're in your virtual environment
pip freeze > requirements.txt

    

    Create README.md:

    
touch README.md
# Then copy the content above into it

    

    Create .gitignore:

    
touch .gitignore
# Then copy the content above into it

    

    Push to GitHub:

    
# Initialize git if you haven't already
git init

# Add files
git add .

# Commit
git commit -m "Initial commit"

# Link to your GitHub repo
git remote add origin [your-github-repo-url]

# Push
git push -u origin main

    

Your teammate will then:

    Clone the repo
    Create a virtual environment
    Install dependencies from requirements.txt
    Download the Vosk model
    Run the server

Would you like me to explain any of these steps in more detail?
so this thing 
