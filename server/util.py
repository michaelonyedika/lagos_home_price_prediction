import json
import pickle

import numpy as np

__locations = None
__ajax_json = None
__model = None
__property_type = None
__model_columns = None


def get_estimated_price(location, property_type, bhk):
    try:
        loc_index = __model_columns.index(location.lower())
    except:
        loc_index = -1
    try:
        type_index = __model_columns.index(property_type.lower())
    except:
        type_index = -1

    x = np.zeros(len(__model_columns))
    x[0] = bhk

    if loc_index >= 0:
        x[loc_index] = 1
    if type_index >= 0:
        x[type_index] = 1
    num = round(__model.predict([x])[0])
    return f'{num:,}'


def load_saved_artifacts():
    print('loading saved artifacts...start')
    # global __data_columns
    global __locations
    global __property_type
    global __model_columns
    global __ajax_json

    with open('./artifacts/lagos_columns_now.json', 'r') as f:
        __data_columns = json.load(f)['location']
        __locations = __data_columns[9:]
        __property_type = __data_columns[1:9]

    with open('./artifacts/model_columns_now.json', 'r') as f:
        __model_columns = json.load(f)['model_columns']

    with open('./artifacts/data.json', 'r') as f:
        __ajax_json = json.load(f)

    global __model
    if __model is None:
        with open('./artifacts/lagos_prediction_using_tree_now.pickle', 'rb') as f:
            __model = pickle.load(f)
    print('Loading saved artifacts...done')


def get_location_names():
    return __locations


def get_property_type():
    return __property_type


def get_ajax_json():
    return __ajax_json


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_property_type())
    print(get_ajax_json())
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('agege', 'bungalow', 3))
    # print(get_estimated_price(1, 'lekki'))
    # print(get_estimated_price(3, 'Abule-Egba'))
    # print(get_estimated_price(3, 'Apapa'))
    # print(__data_columns.index('Lekki'.lower()))
