from flask import Flask, jsonify
import requests, json
from datetime import datetime

app = Flask(__name__)
@app.route("/heartrate/last", methods=["GET"])
def get_heartrate():
    myheader = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1/user/-/activities/heart/date/2022-09-13/1d/1min.json"
    resp = requests.get(myurl, headers=myheader).json()
    time = resp["activities-heart-intraday"]["dataset"][-1]["time"]
    value = resp["activities-heart-intraday"]["dataset"][-1]["value"]
    ret = {'heart-rate': value, 'time offset': time}
    return jsonify(ret)

@app.route("/steps/last", methods=["GET"])
def get_steps():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1/user/-/activities/steps/date/2022-09-13/1d.json"
    disturl = "https://api.fitbit.com/1/user/-/activities/distance/date/2022-09-13/1d.json"
    resp = requests.get(myurl, headers=myheader).json()
    resp2 = requests.get(disturl, headers=myheader).json()
    totalSteps = resp["activities-steps"][0]["value"]
    distance = resp2["activities-distance"][0]["value"]
    #duration = resp["activities"]["duration"]

    cur = datetime.now()
    time = datetime.now().strftime('%m/%d/%y') + " " + resp["activities-steps-intraday"]["dataset"][-1]["time"]
    difference = datetime.strptime(time, '%m/%d/%y %H:%M:%S')
    off = (cur - difference).total_seconds()/60

    ret = {'step-count': totalSteps, 'distance': distance, 'time offset': off}
    return jsonify(ret)
    
@app.route("/sleep/<date>", methods=["GET"])
def get_sleep(date):
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1.2/user/-/sleep/date/2022-09-12.json"
    resp = requests.get(myurl, headers=myheader).json()
    deepSleep = resp["summary"]["stages"]["deep"]
    lightSleep = resp["summary"]["stages"]["light"]
    remSleep = resp["summary"]["stages"]["rem"]
    wakeSleep = resp["summary"]["stages"]["wake"]

    ret = {'deep': deepSleep, 'light': lightSleep, 'rem': remSleep, 'wake': wakeSleep}
    return jsonify(ret)

@app.route("/activity/<date>", methods=["GET"])
def get_activeness(date):
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/2022-09-13.json"
    resp = requests.get(myurl, headers=myheader).json()
    sedentaryMinutes = resp["summary"]["sedentaryMinutes"]
    veryActive = resp["summary"]["veryActiveMinutes"]
    lightlyActive = resp["summary"]["lightlyActiveMinutes"]
    ret = {'very-active': veryActive, 'lightly-active': lightlyActive, 'sedentary': sedentaryMinutes}
    return jsonify(ret)

if __name__ == '__main__':
    app.run(debug=True)