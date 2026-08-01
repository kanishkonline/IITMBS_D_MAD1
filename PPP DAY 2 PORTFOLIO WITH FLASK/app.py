from flask import Flask, render_template

app = Flask(__name__)

# All your data lives in Python — not in HTML
student = {
    'name': 'Kanishk Singh',
    'tagline': 'IIT Madras BS Data Science · Building with Python and Flask',
    'about': 'I am a Data Science student at IIT Madras, learning full-stack web development with Python and Flask. Also building a YouTube channel and exploring machine learning.',
    'subjects': ['MAD 1', 'MLF', 'MLT', 'DBMS'],
    'skills': ['Python', 'Flask', 'SQL', 'HTML & CSS', 'Machine Learning', 'Data Science'],
    'projects': [
        {
            'name': 'Grade Tracker App',
            'desc': 'A Flask web app to track academic grades — with user auth, REST API, and live deployment.',
            'tags': ['Flask', 'SQLite', 'Python', 'REST API']
        },
        {
            'name': 'Study Planner',
            'desc': 'A tool to generate day-by-day study plans for exam sprints. Built to solve my own problem.',
            'tags': ['Flask', 'Python', 'Jinja2']
        }
    ],
    'email': 'kanishk@example.com',
    'github': 'https://github.com/kanishk'
}

@app.route('/')
def home():
    return render_template('index.html', student=student)

@app.route('/about')
def about():
    return render_template('about.html', student=student)

@app.route('/projects')
def projects():
    return render_template('projects.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)