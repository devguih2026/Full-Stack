from flask import Flask
from flask_cors import CORS
from controller import projeto_bp

app = Flask(__name__)
CORS(app)  # <-- ESSENCIAL

app.register_blueprint(projeto_bp)

if __name__ == "__main__":
    app.run(debug=True)
