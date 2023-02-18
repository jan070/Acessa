from flask import Flask, render_template
app=Flask(__name__,template_folder='templates' , static_folder='static')

@app.route('/home')
def home():
   return render_template('index.html')

@app.route('/contacts')
def contacts():
   return render_template('contact.html')

@app.route('/ISL')
def ISL():
   return render_template('ISL.html')

@app.route('/TextToSpeech')
def TOS():
   return render_template('CaptureText.html')

@app.route('/NGO')
def NGO():
   return render_template('NGO.html')

@app.route('/Hearing')
def hearing():
   return render_template('Hearing Disablity.html')

@app.route('/Speaking')
def speaking():
   return render_template('Speaking Disablity.html')






if __name__ == '__main__':
   app.run(debug=True)