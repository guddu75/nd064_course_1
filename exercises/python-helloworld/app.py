from flask import Flask , render_template ,json
import logging


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response



if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)


