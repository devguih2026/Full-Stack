from flask import Flask
from controller import projeto_bp
from flask_cors import CORS


app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(projeto_bp)

if __name__ == "__main__":
    app.run(debug=True)