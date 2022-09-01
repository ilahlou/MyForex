from flask import Flask

app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Congratulations, it's a web app!"

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

value = input("What is the Value in Fahrenheit? ")
fahrenheit_from(value)
