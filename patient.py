from train_model import predict_diagnosis
from suggestion_dispensary import provide_suggestions
import pyttsx3  # For text-to-speech
import speech_recognition as sr  # For voice input


def get_voice_input(prompt):
    """
    Function to collect voice input using the microphone.

    Args:
        prompt (str): A spoken prompt to inform the user what data is being collected.

    Returns:
        str: The user's response as text.
    """
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    engine.say(prompt)
    engine.runAndWait()

    print(prompt)  # Display prompt for reference
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            response = recognizer.recognize_google(audio)
            print(f"You said: {response}")
            return response.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Please repeat.")
        return get_voice_input(prompt)
    except sr.RequestError:
        print("Voice service is unavailable. Please try again later.")
        return None


def collect_patient_data():
    """
    Collects patient data (gender, age, temperature, blood pressure, and symptoms) via voice input.

    Returns:
        tuple: Contains gender, age, temperature, systolic_bp, diastolic_bp, and symptoms.
    """
    print("Welcome to the AI Diagnostic System (Voice-Only Mode)!")
    engine = pyttsx3.init()
    engine.say("Welcome to the AI Diagnostic System. I will collect your health data via voice.")
    engine.runAndWait()

    # Collecting Gender
    gender_response = get_voice_input("Please say your gender. Say male or female.")
    if "male" in gender_response:
        gender = 1  # Male = 1
    elif "female" in gender_response:
        gender = 0  # Female = 0
    else:
        print("Invalid gender input. Please try again.")
        return collect_patient_data()

    # Collecting Age
    age_response = get_voice_input("Please say your age.")
    try:
        age = int(age_response)
    except ValueError:
        print("Invalid age input. Please try again.")
        return collect_patient_data()

    # Collecting Temperature
    temp_response = get_voice_input("Please say your body temperature in Celsius.")
    try:
        temperature = float(temp_response)
    except ValueError:
        print("Invalid temperature input. Please try again.")
        return collect_patient_data()

    # Collecting Blood Pressure
    systolic_bp_response = get_voice_input(
        "Please say your systolic blood pressure, the upper number."
    )
    diastolic_bp_response = get_voice_input(
        "Please say your diastolic blood pressure, the lower number."
    )
    try:
        systolic_bp = int(systolic_bp_response)
        diastolic_bp = int(diastolic_bp_response)
    except ValueError:
        print("Invalid blood pressure values. Please try again.")
        return collect_patient_data()

    # Collecting Symptoms
    symptoms_response = get_voice_input(
        "Please say your symptoms, separated by pauses, like fever, cough, or headache."
    )
    symptoms = symptoms_response.split(", ")

    return gender, age, temperature, systolic_bp, diastolic_bp, symptoms


def interactive_diagnosis():
    """
    Main interactive function to run the voice-only AI Diagnostic System.
    """
    # Initialize Text-to-Speech engine
    