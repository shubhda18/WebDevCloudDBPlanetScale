from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)
db_jobs=load_jobs_from_db()
@app.route("/")

def hello_jovian():
  
  return render_template('home.html', 
                           jobs=db_jobs, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(db_jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)