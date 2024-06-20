from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Kuala Lumpur, Malaysia',
    'salary': 'RM 3,000 - RM 5,000',
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Cyberjaya, Malaysia',
    'salary': 'RM 25,000 - RM 35,000',
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'RM 4,000 - RM 6,000',
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Remote',
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='NCC')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
