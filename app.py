from flask import Flask, request, render_template

app = Flask(__name__)
secret_key = 99


@app.route('/', methods=["GET", "POST"])
@app.route('/encode', methods=["GET", "POST"])
def encode_result():
    if request.method == "POST":
        userInput = request.form.get("encode")
        result_value = doEncode(userInput)
        return render_template("encode.html", data=result_value)
    return render_template("encode.html")


@app.route('/decode', methods=["GET", "POST"])
def decode_result():
    if request.method == "POST":
        userInput = request.form.get("decode")
        result_value = doDecode(userInput)
        return render_template("decode.html", data=result_value)
    return render_template("decode.html")


def doEncode(data):
    algo = ""
    for i in data:
        algo += chr(ord(i) + secret_key)
    return str(secret_key) + algo


def doDecode(data):
    algo = ""
    # global secret_key
    secret_key_length = len(str(secret_key))
    data = data[secret_key_length:]
    for i in data:
        algo += chr(ord(i) - secret_key)
    return algo


if __name__ == '__main__':
    app.run(debug=True)
