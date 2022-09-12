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
    ret = {'heart-rate': value, 'time offset': time}
    return jsonify(ret)

app = Flask(__name__)
@app.route("/steps/last", methods=["GET"])
def get_steps():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/2022-08-24.json"
    resp = requests.get(myurl, headers=myheader).json()
    totalSteps = resp["activities"]["steps"]
    distance = resp["activities"]["distance"]
    duration = resp["activities"]["duration"]
    ret = {'step-count': totalSteps, 'distance': distance, 'time offset': duration}
    return jsonify(ret)
    
def get_sleep():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1.2/user/-/sleep/date/2022-08-24.json"
    resp = requests.get(myurl, headers=myheader).json()
    sleep = resp["summary"]["totalMinutesAsleep"]
    print("you slept for " + str(sleep) + " minutes last night.")

def get_activeness():
    myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"}
    myurl = "https://api.fitbit.com/1/user/-/activities/date/2022-08-24.json"
    resp = requests.get(myurl, headers=myheader).json()
    sedentaryMinutes = resp["summary"]["sedentaryMinutes"]
    veryActive = resp["summary"]["veryActiveMinutes"]
    print("today, you were sedentary for " + str(sedentaryMinutes) + " minutes and active for " + str(veryActive) + " minutes in the very high activity zone.")

if __name__ == '__main__':
    app.run(debug=True)