from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/is-caption-gif/<url>")
def is_caption_gif(url):
    return jsonify(result=True), 200

if __name__ == "__main__":
    app.run(debug=True)

print("Hi")