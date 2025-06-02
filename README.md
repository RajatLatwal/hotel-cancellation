# 🏨 Hotel Booking Cancellation Prediction

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?style=for-the-badge)](https://hotel-cancellation.streamlit.app/)

A machine learning web app built with **Streamlit** that predicts whether a hotel booking will be **canceled or not** based on user input. This project aims to assist hotel managers in identifying potential cancellations to manage resources more efficiently.

---

## 🔍 Features

- User-friendly **web interface** using Streamlit
- **Real-time prediction** of booking cancellations
- Supports input for features like lead time, number of adults, booking changes, deposit type, and more
- Trained on **Hotel Booking Demand dataset**
- Visual feedback on input data and prediction result

---

## 🚀 Demo

👉 **Live App:** [hotel-cancellation.streamlit.app](https://hotel-cancellation.streamlit.app/)

---

## 🧠 Model Details

- **Algorithm Used:** Random Forest Classifier
- **Accuracy:** ~87% on test data
- **Libraries Used:** pandas, scikit-learn, streamlit, numpy, matplotlib

---

## 🛠️ Tech Stack

- 🐍 Python
- 📊 Pandas, NumPy
- 🧠 Scikit-learn
- 🎨 Streamlit (Frontend UI)
- 📈 Matplotlib / Seaborn (EDA & visualization)

---

## 📁 Project Structure

hotel-cancellation/
├── app.py # Main Streamlit app script
├── model.pkl # Trained machine learning model
├── requirements.txt # Python dependencies
├── dataset.csv # (Optional) Dataset used for training
└── README.md # Project documentation
