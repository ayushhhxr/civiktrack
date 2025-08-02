from flask import Flask
from flask_cors import CORS
from extensions import db  # ✅ now importing from extensions.py

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/civic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # ✅ setup db

from models import User, Issue
from routes.auth import auth_bp
from routes.issues import issues_bp

app.register_blueprint(auth_bp)
app.register_blueprint(issues_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
