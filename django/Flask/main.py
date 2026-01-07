from flask import Flask,render_template

app = Flask(__name__) #init

@app.route("/")  #url
def index():
    return render_template('index.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/chackout")
def chackout():
    return render_template('chackout.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')


if __name__ == "__main__":
    app.run(debug=True)

