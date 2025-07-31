from django.shortcuts import render
import pandas as pd
import joblib
import os

# Load model and label encoder once
BASE_DIR = r'C:\Users\Lenovo\Desktop\3-2 Project'

model = joblib.load(os.path.join(BASE_DIR, 'medicine_recommendation_system', 'svc.pkl'))
encoder = joblib.load(os.path.join(BASE_DIR, 'medicine_recommendation_system', 'label_encoder.pkl'))
# Load disease to medicine mapping
disease_med_map = pd.read_csv(os.path.join(BASE_DIR, 'medicine_recommendation_system', 'Dataset', 'medications.csv'))
disease_to_med = dict(zip(disease_med_map['Disease'], disease_med_map['Medication']))

# Load additional dataset mappings
description_data = pd.read_csv(os.path.join(BASE_DIR, 'medicine_recommendation_system', 'Dataset', 'description.csv'))
precaution_data = pd.read_csv(os.path.join(BASE_DIR, 'medicine_recommendation_system', 'Dataset', 'precautions_df.csv'))
workout_data = pd.read_csv(os.path.join(BASE_DIR, 'medicine_recommendation_system', 'Dataset', 'workout_df.csv'))
diet_data = pd.read_csv(os.path.join(BASE_DIR, 'medicine_recommendation_system', 'Dataset', 'diets.csv'))

# Create dictionaries for quick lookup
disease_to_description = dict(zip(description_data['Disease'], description_data['Description']))
disease_to_precaution = dict(zip(precaution_data['Disease'], zip(
    precaution_data['Precaution_1'], 
    precaution_data['Precaution_2'],
    precaution_data['Precaution_3'],
    precaution_data['Precaution_4']
)))
disease_to_workout = dict(zip(workout_data['disease'], workout_data['workout']))
disease_to_diet = dict(zip(diet_data['Disease'], diet_data['Diet']))

# List of all symptoms used during model training (manually defined)
all_symptoms = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze'# Add all other symptoms used during training
]

def home(request):
    # Provide all available symptoms to the template
    symptoms = all_symptoms
    return render(request, 'home.html', {'symptoms': symptoms})

def predict(request):
    if request.method == 'POST':
        selected_symptoms = request.POST.getlist('symptoms[]')
        
        # Remove empty symptoms
        selected_symptoms = [s for s in selected_symptoms if s.strip()]
        
        if not selected_symptoms:
            return render(request, 'home.html', {
                'symptoms': all_symptoms,
                'error': 'Please select at least one symptom'
            })

        # Create input vector for all symptoms
        input_dict = {symptom: 0 for symptom in all_symptoms}
        valid_symptoms = []
        
        for symptom in selected_symptoms:
            if symptom in input_dict:
                input_dict[symptom] = 1
                valid_symptoms.append(symptom)

        # Convert to numpy array
        input_array = pd.DataFrame([input_dict]).values
        
        # Get prediction probabilities
        probabilities = model.predict_proba(input_array)[0]
        
        # Get top 3 predictions
        top_indices = probabilities.argsort()[-3:][::-1]
        
        predictions = []
        for idx in top_indices:
            disease = encoder.inverse_transform([idx])[0]
            confidence = probabilities[idx] * 100
            
            # Calculate symptom match percentage
            symptom_match = (len(valid_symptoms) / len(selected_symptoms)) * 100 if selected_symptoms else 0
            
            # Calculate symptom contributions
            base_prob = probabilities[idx]
            symptom_contributions = []
            
            if base_prob > 0:
                for symptom in valid_symptoms:
                    # Create vector without this symptom
                    test_dict = input_dict.copy()
                    test_dict[symptom] = 0
                    test_array = pd.DataFrame([test_dict]).values
                    
                    # Get probability without this symptom
                    prob_without = model.predict_proba(test_array)[0][idx]
                    
                    # Calculate contribution
                    contribution = base_prob - prob_without
                    contribution_percentage = (contribution / base_prob) * 100
                    
                    symptom_contributions.append({
                        'symptom': symptom.replace('_', ' ').title(),
                        'contribution': round(contribution_percentage, 2)
                    })
                
                # Sort by contribution (highest first)
                symptom_contributions.sort(key=lambda x: x['contribution'], reverse=True)
            
            # Get additional information
            medicines = disease_to_med.get(disease, "No medication found")
            if isinstance(medicines, str):
                medicines = [med.strip() for med in medicines.split(',')]
            
            description = disease_to_description.get(disease, "No description available")
            precautions = list(disease_to_precaution.get(disease, ["No precautions found"]))
            workouts = disease_to_workout.get(disease, "No workout recommendations")
            diets = disease_to_diet.get(disease, "No diet recommendations")
            
            # Clean up the data
            if isinstance(workouts, str):
                workouts = [w.strip() for w in workouts.split(',')]
            if isinstance(diets, str):
                diets = [d.strip() for d in diets.split(',')]
            
            predictions.append({
                'disease': disease,
                'confidence': round(confidence, 2),
                'symptom_match': round(symptom_match, 2),
                'medicines': medicines,
                'description': description,
                'precautions': precautions,
                'workouts': workouts,
                'diets': diets,
                'symptom_contributions': symptom_contributions
            })

        return render(request, 'result.html', {
            'predictions': predictions,
            'selected_symptoms': valid_symptoms,
            'total_symptoms': len(selected_symptoms)
        })

    return render(request, 'home.html', {'symptoms': all_symptoms})