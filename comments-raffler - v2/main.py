from flask import Flask, render_template, request
from sorteador import sorteador

app = Flask("Sorteio")
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/result')
def result():
  try:
    url = request.args.get('url')
    number = int(request.args.get('winners'))
    resultado = sorteador(url, number)
    return render_template('result.html', result = resultado[1], number = number, comments = resultado[0])
  except:
    print('batata')
    #return redirect('/')
    return render_template('home.html')

  
app.run(host='0.0.0.0')
