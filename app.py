from flask import Flask, jsonify, render_template
from  services.retrack import *
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/api/toplastfm/<usuario>")
def pegar_tops(usuario):
   dados = pegar_tops_lastfm(usuario)
   return jsonify(dados)

if __name__ == "__main__":
   app.run(debug=True)