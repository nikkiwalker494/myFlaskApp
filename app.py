from flask import Flask, render_template
from datetime import datetime

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template('index.html', date=current_date)
    
    return app
