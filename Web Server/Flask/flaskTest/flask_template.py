from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('testing.html')

if __name__ == "__main__":
    app.run(host='192.168.0.150',port=80,debug=True)
