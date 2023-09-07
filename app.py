import streamlit as st
import pandas as pd
import sklearn
import pickle

model = pickle.load(open("rf_random.pkl", "rb"))

st.set_page_config(page_title='Flight Price Prediction')

st.markdown('''
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        padding-top: 20px;
    }
    </style>
''', unsafe_allow_html=True)

st.markdown('<h1 class="title">Flight Price Prediction</h1>', unsafe_allow_html=True)
st.write('You want to book your flight ticket at a low price but don\'t know when to book?')

@st.cache
def predict_flight_price(features):
    prediction = model.predict([features])
    return round(prediction[0], 2)

date_dep = st.date_input('Date of Journey')
dep_time = st.time_input('Departure Time')
arr_time = st.time_input('Arrival Time')

source = st.selectbox('Source', ('Delhi', 'Kolkata', 'Mumbai', 'Chennai'))
destination = st.selectbox('Destination', ('Cochin', 'Delhi', 'New Delhi', 'Hyderabad', 'Kolkata'))

total_stops = st.selectbox('Number of Stops', (0, 1, 2, 3, 4))

airline = st.selectbox('Airline', ('Jet Airways', 'IndiGo', 'Air India', 'Multiple carriers', 'SpiceJet', 'Vistara', 'GoAir', 'Multiple carriers Premium economy', 'Jet Airways Business', 'Vistara Premium economy', 'Trujet'))

journey_day = date_dep.day
journey_month = date_dep.month

dep_hour = dep_time.hour
dep_minute = dep_time.minute

arr_hour = arr_time.hour
arr_minute = arr_time.minute

duration_hours = abs(arr_hour - dep_hour)
duration_minutes = abs(arr_minute - dep_minute)

airline_mapping = {
    'Jet Airways': 1,
    'IndiGo': 2,
    'Air India': 3,
    'Multiple carriers': 4,
    'SpiceJet': 5,
    'Vistara': 6,
    'GoAir': 7,
    'Multiple carriers Premium economy': 8,
    'Jet Airways Business': 9,
    'Vistara Premium economy': 10,
    'Trujet': 11
}

source_mapping = {
    'Delhi': 1,
    'Kolkata': 2,
    'Mumbai': 3,
    'Chennai': 4
}

destination_mapping = {
    'Cochin': 1,
    'Delhi': 2,
    'New Delhi': 3,
    'Hyderabad': 4,
    'Kolkata': 5
}

features = [
    total_stops,
    journey_day,
    journey_month,
    dep_hour,
    dep_minute,
    arr_hour,
    arr_minute,
    duration_hours,
    duration_minutes,
    airline_mapping[airline],
    source_mapping[source],
    destination_mapping[destination]
]

if st.button('Predict'):
    prediction = predict_flight_price(features)
    st.success(f'Your Flight Price is INR {prediction}')
