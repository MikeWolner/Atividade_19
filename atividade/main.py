from flask import Flask
app = Flask(__name__)

# Problema 1: Ao substituir string por float a url se tornará inativa
@app.route('/<string:x1>/<string:x2>/<string:y1>/<string:y2>')
def equacao(x1, x2, y1, y2):
    #Solução: Converti do tipo String para formato float
     resultado = (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)) ** 0.5
     return str(resultado) #Todo retorno tem, obrigatoriamente que ser enviado no tipo String
if __name__ == "__main__":
    app.run (debug = True, port = 5000)
 
