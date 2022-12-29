from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'fwzDx37vs92zbzmr3NFih7JfnmTHAoXc'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      session['studentid'] = request.form['studentid']
      return redirect(url_for('success'))
   return render_template('login.html')


@app.route('/success')
def success():
   if session['username'] != '' and session['studentid'] != '':
      username = session['username']
      studentid = session['studentid']
      flash('You were successfully logged in')
      return render_template('success.html', username = username, studentid = studentid)
   else:
      error = 'Invalid username or student ID . Please try again!'
      return render_template('login.html', error = error)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   session.pop('studentid', None)
   return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug = True)