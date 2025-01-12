from flask import Flask,redirect,url_for         #importing library

app=Flask(__name__)  #object creation
#WSGI application


#decorator
@app.route('/') #whenever this page is visited
def welcome():
    return 'Welcome...' #this line will be executed
@app.route('/members')
def welcome_members():
    return 'Welcome members'

@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the marks is'+str(score)

@app.route('/failure/<int:score>')
def failure(score):
    return 'The person has failed and the marks is'+str(score)
@app.route('/results/<int:marks>')
def results(marks):
    result=" "
    if marks<50:
        result='failure'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)

