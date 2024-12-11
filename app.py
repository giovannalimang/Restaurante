from flask import Flask
from controller import prato_controllers

app = Flask(__name__)

app.secret_key = 'sua_chave_secreta_aqui' 

app.register_blueprint(prato_controllers)


if __name__ == "__main__":
    app.run(debug=True)