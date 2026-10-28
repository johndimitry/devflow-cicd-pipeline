from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html', 
        env=os.getenv('ENV', 'production'),
        version=os.getenv('APP_VERSION', '1.0.0'))

@app.route('/api/products')
def products():
    return jsonify([
        {"id": 1, "name": "Notebook DevFlow Pro", "price": 4500.00},
        {"id": 2, "name": "Mouse Gamer", "price": 199.90}
    ])

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "devflow-store"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)