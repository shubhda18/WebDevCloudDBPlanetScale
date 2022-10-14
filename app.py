from flask import Flask, render_template, jsonify,request
from database import load_jobs_from_db, load_job_from_db,add_application_to_db


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
  return render_template('jobpage.html',job=job)

@app.route("/jobs/<id>/apply", methods=['post'])
def load_application(id):
  job= load_job_from_db(id)
  data=request.form
  add_application_to_db(id, data)
  return render_template('application_submission.html', job=job, application=data)
  
                        
  
if __name__ == '__main__:':
  app.run(host='0.0.0.0', debug=True)