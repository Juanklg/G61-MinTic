from types import MethodDescriptorType
from flask import Flask , render_template,request,jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    elemento = 'Hola'
    return render_template('index.html',elemento=elemento)

@app.route("/test")
def test():
    return "<p>Hello, test!</p>"

@app.route("/http",methods = ['GET','POST','PUT','DELETE'])
def httpPage():
    if request.method == 'POST':
        print(request.form)
        return jsonify(request.form)
    else:
        elemento = 'Hola'
        return render_template('httppage.html',elemento=elemento)

@app.route("/doc")
def Edoc():
    title='Documentacion'
    return render_template("doc/index.html",title=title)

@app.route("/doc/<documento>")
def Edocu(documento='index'):
    print(f'var = {documento}'.center(50,'-'))
    return render_template(f"doc/{documento}.html")

# export FLASK_ENV=development