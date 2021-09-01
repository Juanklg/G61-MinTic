from flask import Flask , render_template
import dev as fn
# import funciones as fn
fn.isLogin('Login')
print('Corriendo la app',__name__)
# Inicializacion ------------------------------------------------
#Configura la app
app = Flask(__name__)
# Crea las diferentes rutas -------------------------------------
@app.route("/")
def hello_world():    
    return render_template("index.html")
    
@app.route("/proy")
def proy():
    s = fn.solicitarDoc()
    print(s)    
    return render_template("index.html")
    
@app.route("/doc")
def doc():
    return render_template("doc/index.html")
@app.route("/doc/<documento>")
def docu(documento='index'):
    print(f'var = {documento}'.center(50,'-'))
    return render_template(f"doc/{documento}.html")
# Cierre de rutas ---------------------------------------------- 
# Aca inicia la aplicacion si es el archivo principal
if __name__ == "__main__":
    print("Main".center(50,'-'))
    #debug=True me permite trabajar en desarrollo 
    #y actualizar el servidor cada vez que se hagan cambios
    app.run(debug=True)