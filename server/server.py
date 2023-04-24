from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_property_type', methods=['GET'])
def get_property_type():
    response = jsonify({
        'property_type': util.get_property_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    bhk = int(request.form['bhk'])
    location = request.form['location']
    property_type = request.form['property_type']
    # total_sqft = float(request.form['total_sqft'])
    # bath = int(request.form['bhk'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, property_type, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_ajax_json', methods=['GET'])
def get_ajax_json():
    response = jsonify(
        util.get_ajax_json()
    )
    response.headers.add("Access-Control-Allow-Origin", '*')

    return response


if __name__ == '__main__':
    print('Starting Python Flask server for Home Price Prediction...')
    util.load_saved_artifacts()
    app.run()