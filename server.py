from flask import Flask, render_template, request
# Import the Maths package here
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    return summation(num1, num2).__str__()

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    return subtraction(num1, num2).__str__()

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here  
    return multiplication(num1, num2).__str__()

@app.route("/")
def render_index_page():
    # Write your code here
    return render_template('index.html')

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "Invalid Input"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
