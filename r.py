from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
list=[{"jobid":1234,"job_name":"Python_developer","age":22},
      {"jobid":1237,"job_name":"Java_developer","age":23},
      {"jobid":1274,"job_name":"Web_developer","age":26}]
@app.route('/')
def hello_name():

    return  render_template('r.html',l=list)
app.run(debug=True,port=8000)