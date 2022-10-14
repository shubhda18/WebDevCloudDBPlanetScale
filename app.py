from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db


app = Flask(__name__)

@app.route("/")

def hello_jovian():
  db_jobs=load_jobs_from_db()
  return render_template('home.html', 
                           jobs=db_jobs 
                           )

@app.route("/api/jobs")
def list_jobs():
  db_jobs=load_jobs_from_db()
  return jsonify(db_jobs)

  
@app.route("/jobs/<id>")
def load_job(id):
  job =load_job_from_db(id)
  if not job:
    return "Not Found",404
  return render_template('jobpage.html',display_job=job)
  
if __name__ == '__main__:':
  app.run(host='0.0.0.0', debug=True)