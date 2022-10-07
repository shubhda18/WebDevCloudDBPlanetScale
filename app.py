from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db


app = Flask(__name__)

@app.route("/")

def hello_jovian():
  db_jobs=load_jobs_from_db()
  return render_template('home.html', 
                           jobs=db_jobs, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  db_jobs=load_jobs_from_db()
  return jsonify(db_jobs)

  
@app.route("/jobs/<id>")
def load_job(id):
  job =load_job_from_db(id)
  return jsonify(job)
  
if __name__ == '__main__:':
  app.run(host='0.0.0.0', debug=False)