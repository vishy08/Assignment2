from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/myjoke", methods=["GET"])
def mymethod():
    joke = "Why did everyone cross the road? Ha! ha, ha!"
    ret = {'category' : 'very funny', 'value' : joke}
    return jsonify(ret)
if __name__ == '__main__':
    app.run(debug=True)