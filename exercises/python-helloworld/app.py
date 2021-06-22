from flask import Flask , render_template ,json
import logging

# logging.basicConfig(filename="app.log" , level=logging.DEBUG, format="%(asctime)s")


app = Flask(__name__)

@app.route("/")
def hello():
    logging.debug("main enddpoint was reached")
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    logging.debug(f'healthcheck endpoint was reached')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    logging.debug(f'metrics endpoint was reached')

    return response



if __name__ == "__main__":
    logging.basicConfig(filename="app.log" , level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

    app.run(host='0.0.0.0' , debug=True)


