from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Hello</h1> This is Flask test."

if __name__ == "__main__":
    app.run(host='192.168.0.150',port=80,debug=True)

