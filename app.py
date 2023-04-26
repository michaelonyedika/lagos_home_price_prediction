import json
import numpy as np
import streamlit as st
import pickle

__locations = None
__ajax_json = None
__model = None
__property_type = None
__model_columns = None

lagos_columns = './server/artifacts/lagos_columns_now.json'
model_columns = './server/artifacts/model_columns_now.json'
data_json = './server/artifacts/data.json'
pickle_ = './server/artifacts/lagos_prediction_using_tree_now.pickle'


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

    with open(lagos_columns, 'r') as f:
        __data_columns = json.load(f)['location']
        __locations = __data_columns[9:]
        __property_type = __data_columns[1:9]

    with open(model_columns, 'r') as f:
        __model_columns = json.load(f)['model_columns']

    with open(data_json, 'r') as f:
        __ajax_json = json.load(f)

    global __model
    if __model is None:
        with open(pickle_, 'rb') as f:
            __model = pickle.load(f)
    print('Loading saved artifacts...done')


load_saved_artifacts()


st.title('Lagos House Rent Prediction')

bedroom = st.selectbox(
    'Bedroom',
    [1,2,3,4,5,6,7,8]
)


locations = st.selectbox(
    'Lagos Location',
    __locations
)


property_type = st.selectbox(
    'Property Type',
    __property_type
)


if st.button('Estimate Price'):
    st.write(get_estimated_price(locations, property_type, bedroom), 'Naira')


if st.button('Michael Okoyenta (linkedin)'):
    # url = '<a href="https://www.linkedin.com/in/michael-okoyenta-8357aa163"></a>'
    "https://www.linkedin.com/in/michael-okoyenta-8357aa163"
