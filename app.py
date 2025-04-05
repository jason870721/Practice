from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    # 這樣可以改成任何你想要 print 的字
    return "Hello Kai Chuang"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)