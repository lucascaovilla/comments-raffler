from flask import Flask, render_template, request, redirect
from sorteador import sorteador
from credentials import cred_username, cred_password

app = Flask("Sorteio")
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/result')
def result():
  """ try: """
  url = request.args.get('url')
  number = int(request.args.get('winners'))
  try:
    username = request.args.get('user')
    password = request.args.get('pass')
  except:
    username = cred_username()
    password = cred_password()
  resultado = sorteador(url, number, username, password)
  return render_template('result.html', result = resultado[1], number = number, comments = resultado[0])


    

  
app.run(host='0.0.0.0')
