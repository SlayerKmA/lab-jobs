from flask import Flask, render_template, jsonify

app = Flask(__name__)

lab_jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Managua, Nicaragua',
        'salary': '$45,000'
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Miami, USA',
        'salary': '$55,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '$49,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Managua, Nicaragua',
        'salary': '$57,000'
    },
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs = lab_jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(lab_jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)