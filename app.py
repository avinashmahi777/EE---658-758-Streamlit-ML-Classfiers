# Libraries
import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Styling Code  
# Sidebar section for dataset selection
st.sidebar.title("Select Dataset")
dataset_name = st.sidebar.selectbox("Select Dataset", ("IRIS", "Digits"))


# Sidebar section for choosing classifier
st.sidebar.title("Select Classifier")
classifier_name = st.sidebar.selectbox("Select Classifier", ("Logistic Regression", "Neural Networks", "Naïve Bayes"))


# Adding CSS For Header & Predicted Class
st.write(
    f"""
    <style>
    h1 {{
        text-align: center;
        color: orange;
    }}
    .predicted {{
        font-weight: bold;
        color: green;
    }}
    </style>
    <h1>Machine Learning Streamlit Assignment </h1>
    """,
    unsafe_allow_html=True
)


# Load datasets
iris = datasets.load_iris()
digits = datasets.load_digits()



# Defining classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(),
    "Neural Networks": MLPClassifier(max_iter=1000),
    "Naïve Bayes": GaussianNB()
}


# Loading Datasets using dropdown menu
if dataset_name == "IRIS":
    data = iris
else:
    data = digits


# Actual Machine Learning Starts here
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)


# Initialize accuracy dictionary
accuracy_dict = {}

# Training and evaluating selected classifier
selected_classifier = classifiers[classifier_name]
selected_classifier.fit(X_train, y_train)
y_pred = selected_classifier.predict(X_test)

# Choosing Input Features using Horizontal Bars
st.sidebar.subheader("Input Feature Values")
feature_values = []
for i in range(len(data.feature_names)):
    min_val = float(data.data[:, i].min())
    max_val = float(data.data[:, i].max())
    if min_val == max_val:
        min_val -= 0.1
        max_val += 0.1
    feature_values.append(st.sidebar.slider(data.feature_names[i], min_val, max_val))

# Class Prediction along with predict button
if st.sidebar.button("Predict", help="predict-button", key="predict-button"):
    prediction = selected_classifier.predict([feature_values])
    st.write(f"<span class='predicted'>Predicted Class ({classifier_name}): {prediction[0]}</span>", unsafe_allow_html=True)

# Checkbox to display accuracy score
display_accuracy = st.sidebar.checkbox("Display Accuracy Score", value=True)

if display_accuracy:
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Accuracy for {classifier_name}: {accuracy:.2f}")
