import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Load the model
with open("final_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the transformer
with open("transformer.pkl", "rb") as file:
    transformer = pickle.load(file)

# Prediction logic
def prediction(input_list):
    input_list = np.array(input_list, dtype=object)
    pred = model.predict_proba([input_list])[:, 1][0]

    if pred > 0.5:
        return f"This booking is more likely to get canceled, chances {round(pred * 100, 2)}%"
    else:
        return f"This booking is less likely to get canceled, chances {round(pred * 100, 2)}%"

# Main Streamlit app
def main():
    st.title("🏨 INN HOTEL GROUP - Cancellation Predictor")

    # User inputs
    lt = float(st.text_input("Enter the lead time in days", "0"))
    mkt = 1 if st.selectbox("How the booking was made", ["Online", "Offline"]) == "Online" else 0
    price = float(st.text_input("Enter the price of the room", "0"))
    adult = int(st.selectbox("How many adults?", [1, 2, 3, 4]))
    arr_m = st.slider("What is the month of arrival?", min_value=1, max_value=12, step=1)

    # Weekday mapping
    week_lambda = lambda x: ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"].index(x)

    arr_w = week_lambda(st.selectbox("What is the weekday of arrival", ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]))
    dep_w = week_lambda(st.selectbox("What is the weekday of departure", ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]))

    weekn = int(st.text_input("Enter the number of week nights in stay", "0"))
    wkndn = int(st.text_input("Enter the number of weekend nights in stay", "0"))
    totan = weekn + wkndn

    park = 1 if st.selectbox("Does the customer need parking?", ["yes", "no"]) == "yes" else 0
    spcl = int(st.selectbox("How many special requests have been made", [0, 1, 2, 3, 4, 5]))

    # Transform lead time and price
    lt_t, price_t = transformer.transform([[lt, price]])[0]

    # Final input list (12 features)
    inp_list = [lt_t, spcl, price_t, adult, wkndn, park, weekn, mkt, arr_m, arr_w, totan, dep_w]

    # Predict button
    if st.button("Predict"):
        response = prediction(inp_list)
        st.success(response)

# Entry point
if __name__ == "__main__":
    main()
