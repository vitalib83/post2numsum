from flask import Flask, request
app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    return {'sum': num1 + num2}

if __name__ == '__main__':
    app.run(debug=True)
