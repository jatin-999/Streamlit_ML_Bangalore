import streamlit as st
import json
import pickle
import numpy as np
import os






__data = None
__model = None
__locations = None

def main():
    st.title("Housing Price Prediction")

    # Input components
    area_sqft = st.number_input("Area in sqft", min_value=0.0, step=1.0, value=1000.0)
    num_bedrooms = st.selectbox("Number of Bedrooms", list(range(1, 6)), index=2)
    num_bathrooms = st.selectbox("Number of Bathrooms", list(range(1, 6)), index=2)
    location_options = read_location_options(os.path.join(".", "columns.json"))
    #read_location_options(r".\columns.json")# 
    selected_location = st.selectbox("Location", location_options)

    # Button to estimate price
    if st.button("Estimate Price"):
        # Perform the price estimation based on the inputs
        estimated_price = estimate_price(area_sqft, num_bedrooms, num_bathrooms, selected_location)

        # Display the result
        st.success(f"Estimated Price: {estimated_price:,.2f}")



def read_location_options(json_file):
    # Read location options from JSON file
    
    global __data, __locations, __model
    
    with open(json_file, 'r') as file:
        __data = json.load(file)['data_columns']
        __locations = __data[3:]
        print("Loaded data:", __data)
        
    
    with open(os.path.join(".", "bangalore_ML_predictions.pickle"), 'rb') as file:
        __model = pickle.load(file)
        
    return __locations
        
        
    
def estimate_price(area_sqft, num_bedrooms, num_bathrooms, location):
    
    global __data, __model
    # Placeholder function for price estimation logic
    # Replace this with your actual price estimation logic
    # For now, let's just return a random value
    try:
        loc_index = __data.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data))
    x[0] = area_sqft
    x[1] = num_bathrooms
    x[2] = num_bedrooms
    if (loc_index >= 0):
        x[loc_index] = 1
    
    return round(__model.predict([x])[0], 2)

    import random
    return random.uniform(50000, 200000)

if __name__ == "__main__":
    main()