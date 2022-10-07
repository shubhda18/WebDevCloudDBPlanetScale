
from sqlalchemy import create_engine,text
import os
db_conn_string = os.environ['DB_CONN_STR']

engine = create_engine(db_conn_string,connect_args ={
  'ssl':{"ssl_ca": "/etc/ssl/cert.pem"}}    )      

def load_jobs_from_db():
  with engine.connect() as conn:
    result= conn.execute(text('SELECT * from jobs'))
    jobs=[]
    for row in result.all():
      jobs.append(dict(row))
  return jobs

  
def load_job_from_db(id):
  with engine.connect() as conn:
    
    result = conn.execute(text("SELECT * FROM jobs where id =:val"),val=id)
    row=result.all()
    if len(row)==0:
      return None
    else:
      return dict(row[0])

 