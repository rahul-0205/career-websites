from flask import  Flask
from flask import render_template
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Delhi,India',
    'salary':'Rs. 11,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Bengaluru, India',
    'salary':'Rs. 7,00,000'
  },
  {
    'id':3,
    'title':'Software Engineer',
    'location':'Chennai,India',
    'salary':'Rs. 12,00,000'
  },
  {
    'id':4,
    'title':'Frontend developer',
    'location':'Remote',
    'salary':'Rs. 1,00,000'
  }
]
@app.route("/")
def hello():
  return render_template('index.html',jobs=JOBS)
if __name__ =='__main__':
  app.run(host='0.0.0.0', debug=True)