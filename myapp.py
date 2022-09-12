from flask import Flask, jsonify
import requests, json

app = Flask(__name__)
@app.route("/heartrate/last", methods=["GET"])

def get_heartrate():
    myheader = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1/user/-/activities/heart/date/2022-08-24/1d/1min.json"
    resp = requests.get(myurl, headers=myheader).json()
    time = resp["activities-heart-intraday"]["dataset"][-1]["time"]
    value = resp["activities-heart-intraday"]["dataset"][-1]["value"]
    print("your most recent heart rate recorded at " + str(time) + " AM is " + str(value) + " beats per minute")
    return jsonify(value)

if __name__ == '__main__':
    app.run(debug=True)