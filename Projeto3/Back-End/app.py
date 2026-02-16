from flask import Flask
from flask_cors import CORS
from controllers import projeto_bp
from controllers.agendamento_controller import agendamento_bp
from App.db import engine, Base
from models import usuario, agendamento

app = Flask(__name__)   # 🔹 primeiro cria o app
CORS(app)

Base.metadata.create_all(bind=engine)

# 🔹 depois registra os blueprints
app.register_blueprint(projeto_bp)
app.register_blueprint(agendamento_bp)

if __name__ == "__main__":
    app.run(debug=True)



