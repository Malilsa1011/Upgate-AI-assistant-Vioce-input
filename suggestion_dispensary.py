#suggestions
def provide_suggestions(diagnosis, severity, gender, age, symptoms):
    """
    Provide personalized suggestions, prescribe basic medications, and refer patients to doctors if necessary.
    
    Parameters:
    - diagnosis: Predicted diagnosis (e.g., "Flu", "Hypertension", "Other")
    - severity: Severity level (e.g., "Mild", "Moderate", "Severe")
    - gender: 1 = Male, 0 = Female
    - age: Patient's age
    - symptoms: List of symptoms (e.g., ["fever", "cough"])
    
    Returns:
    - A string with advice and recommendations.
    """
    advice = []
    
    # Tailored advice based on diagnosis and severity
    if diagnosis == "Flu":
        if severity == "Mild":
            advice.append("Rest, drink plenty of fluids, and monitor your symptoms.")
            if gender == 1:  # Male
                advice.append("Avoid strenuous activities to recover faster.")
            else:  # Female
                advice.append("Ensure you stay hydrated and take frequent naps.")
        elif severity == "Moderate":
            advice.append("Take over-the-counter fever reducers like paracetamol and stay hydrated.")
        else:  # Severe
            advice.append("Your condition is serious. Please see a doctor immediately.")
            return "\n".join(advice)
    
    elif diagnosis == "Hypertension":
        advice.append("Monitor your blood pressure regularly.")
        if age > 50:
            advice.append("Adopt a low-sodium diet and consult a doctor for further treatment.")
        else:
            advice.append("Reduce salt intake, exercise regularly, and avoid stress.")
        if severity == "Severe":
            advice.append("Seek medical attention immediately.")
    
    else:  # Other diagnoses or unrecognized symptoms
        if severity == "Severe":
            advice.append("Your condition is serious. Please consult a doctor immediately.")
        else:
            advice.append("Your symptoms are unclear. It is recommended to see a doctor for further evaluation.")
            return "\n".join(advice)
    
    # Prescribe basic medication
    if "fever" in symptoms:
        advice.append("You can take paracetamol (500 mg) every 6-8 hours to reduce fever.")
    if "cough" in symptoms:
        advice.append("For a dry cough, use a cough suppressant syrup. If the cough is wet, consider an expectorant.")
    if "fatigue" in symptoms:
        advice.append("Ensure adequate rest and consume nutrient-rich foods to restore energy.")

    # Tailored advice for age and gender
    if age < 12:
        advice.append("Ensure the medication dosage is appropriate for children. Consult a pediatrician if needed.")
    elif age > 60:
        advice.append("Be cautious with medications, as older adults may have sensitivities. Consult a doctor if unsure.")
    
    return "\n".join(advice)