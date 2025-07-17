from flask import Flask
from config import Config
from models import db
from routes import api

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 自动创建表
    app.run(debug=True)
