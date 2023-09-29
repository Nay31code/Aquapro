import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Waste water predictor",
    page_icon="🌊", 
    layout="wide", 
)
st.title("**Predictor**")
# Read the Excel file
df = pd.read_excel('mix.xlsx')

# Convert Month to numeric
month_mapping = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}
df['Month'] = df['Month'].str.lower().map(month_mapping)

# Train-test split
X = df[['Month']]
y = df['BODaverage']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Display the MSE
st.write(f'Mean Squared Error: {mse}')
user_put = st.selectbox("Select a Parameters:", ['BOD', 'Fat oil and grease', 'Settleable solids', 'Sulfide', 'TKN', 'Total dissolved solids', 'Total suspended solids', 'aug', 'sep', 'oct', 'nov', 'dec'])

# User input for prediction
user_input = st.selectbox("Select a Month:", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])

# Make prediction
predicted_value = model.predict([[month_mapping[user_input]]])

# Display the predicted value
st.write(f'Predicted BODaverage value: {predicted_value[0]}')

# Plot scatter plot
fig, ax = plt.subplots()
ax.scatter(month_mapping[user_input], predicted_value[0], color='red', label='Predicted')
ax.set_xlabel('Month')
ax.set_ylabel('BODaverage')
ax.grid(True)
ax.legend()
st.pyplot(fig)



# Display the plot
# UBU Waste Water Monitoring and Prediction Apparatus 
# 