## Integrate HTML with flask 
## HTTP verb GET and POST


#jinja2 template 
from flask import Flask,redirect,url_for,render_template,request         #importing library

app=Flask(__name__)  #object creation
#WSGI application


#decorator
@app.route('/') #whenever this page is visited
def welcome():
    return render_template('index.html')  #HTML file is run if it exists
@app.route('/members')
def welcome_members():
    return 'Welcome members'


#success case
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score, 'res':res}
    return render_template('result.html',result=exp)

#failure case 
@app.route('/failure/<int:score>')
def failure(score):
    return 'The person has failed and the marks is' +str(score)

#results case
@app.route('/results/<int:marks>')
def results(marks):
    result=" "
    if marks<50:
        result='failure'
    else:
        result='success'
    return redirect(url_for(result,score=marks))
#result checker
@app.route('/submit', methods=['POST', 'GET'])
def submit():
   # pass  # Placeholder to avoid indentation errors. Add functionality here.
    total_score=0
    #getting the requests for each subject
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
    res=""
    if total_score>=50:
        res="success"
    else:
        res="failure"
    return redirect(url_for(res,score=total_score)) #dynamic url generation
    
if __name__ == '__main__':
    app.run(debug=True)

