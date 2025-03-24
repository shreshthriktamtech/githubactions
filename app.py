from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def index():
    return jsonify({"message":"done with change"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)