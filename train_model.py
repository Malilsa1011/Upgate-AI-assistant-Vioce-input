import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib  # For saving and loading the trained model

# Global variable to hold the trained model
model = None


def prepare_data(data_path="synthetic_diagnostic_data.csv"):
    """
    Load and preprocess the dataset for training the model.

    Args:
        data_path (str): Path to the CSV file containing the dataset.

    Returns:
        tuple: Features (X) and labels (y) for training/testing.
    """
    # Load dataset
    data = pd.read_csv(data_path)

    # Encode categorical features (e.g., symptoms, severity, diagnosis)
    label_encoder = LabelEncoder()
    data["Diagnosis"] = label_encoder.fit_transform(data["Diagnosis"])
    data["Severity"] = label_encoder.fit_transform(data["Severity"])
    
    # Save encoders for decoding later
    joblib.dump(label_encoder, "diagnosis_label_encoder.pkl")
    
    # Define features and labels
    X = data.drop(columns=["Diagnosis", "Severity"])
    y = data[["Diagnosis", "Severity"]]

    return X, y


def train_model(data_path="synthetic_diagnostic_data.csv"):
    """
    Train the machine learning model using the provided dataset.

    Args:
        data_path (str): Path to the CSV file containing the dataset.

    Returns:
        RandomForestClassifier: Trained machine learning model.
    """
    global model

    # Prepare the data
    X, y = prepare_data(data_path)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Model trained with an accuracy of {accuracy * 100:.2f}%")

    # Save the trained model
    joblib.dump(model, "diagnostic_model.pkl")

    return model


def predict_diagnosis(temperature, systolic_bp, diastolic_bp, symptoms, age, gender):
    """
    Use the trained model to predict the diagnosis and severity for a patient.

    Args:
        temperature (float): Body temperature in Celsius.
        systolic_bp (int): Systolic blood pressure.
        diastolic_bp (int): Diastolic blood pressure.
        symptoms (list of str): List of symptoms.
        age (int): Age of the patient.
        gender (int): Gender of the patient (0 for Female, 1 for Male).

    Returns:
        tuple: Predicted diagnosis and severity.
    """
    global model

    # Check if the model is already loaded, if not load it
    if model is None:
        model = joblib.load("diagnostic_model.pkl")

    # Prepare input features for prediction
    symptoms_vector = [1 if symptom in symptoms else 0 for symptom in ["fever", "cough", "fatigue", "headache"]]
    input_data = np.array([[temperature, systolic_bp, diastolic_bp, age, gender] + symptoms_vector])

    # Predict diagnosis and severity
    prediction = model.predict(input_data)
    diagnosis_encoder = joblib.load("diagnosis_label_encoder.pkl")

    # Decode the diagnosis and severity
    diagnosis = diagnosis_encoder.inverse_transform([prediction[0][0]])[0]
    severity = diagnosis_encoder.inverse_transform([prediction[0][1]])[0]

    return diagnosis, severity


if __name__ == "__main__":
    print("Training the diagnostic model...")
    train_model()
    print("Model training complete!")