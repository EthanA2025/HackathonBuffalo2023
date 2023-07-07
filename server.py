from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_script', methods=['GET'])
def run_regression():
    result = subprocess.run(['python3', 'regression_model.py'], stdout="subproccess.PIPE")
    output = result.stdout.decode('utf-8')
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(port=5000, debug=True)