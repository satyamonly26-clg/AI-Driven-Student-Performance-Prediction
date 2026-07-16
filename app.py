import streamlit as st
import pandas as pd
import joblib
model = joblib.load("student_performance_model.pkl")

st.title("🎓 AI-Driven Student Performance Prediction System")
st.header("Enter Student Details")
student_name = st.text_input(
    "👤 Student Name",
    placeholder="Enter Student Name"
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)
race = st.selectbox(
    "Race/Ethnicity",
    ["Group A", "Group B", "Group C", "Group D", "Group E"]
)
parent_education = st.selectbox(
    "Parental Level of Education",
    [
        "Some High School",
        "High School",
        "Some College",
        "Associate Degree",
        "Bachelor Degree",
        "Master Degree"
    ]
)
lunch = st.selectbox(
    "Lunch",
    ["Standard", "Free/Reduced"]
)
test_preparation = st.selectbox(
    "Test Preparation Course",
    ["None", "Completed"]
)
st.subheader("Enter Exam Scores")

math_score = st.number_input(
    "Math Score",
    min_value=0,
    max_value=100,
    value=50
)

reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=50
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=50
)
average_score = (math_score + reading_score + writing_score) / 3

st.write("Average Score:", round(average_score, 2))

if st.button("Predict"):

    # Mapping dictionaries
    gender_map = {
        "Female": 0,
        "Male": 1
    }

    race_map = {
        "Group A": 0,
        "Group B": 1,
        "Group C": 2,
        "Group D": 3,
        "Group E": 4
    }

    parent_education_map = {
        "Some High School": 0,
        "High School": 1,
        "Some College": 2,
        "Associate Degree": 3,
        "Bachelor Degree": 4,
        "Master Degree": 5
    }

    lunch_map = {
        "Free/Reduced": 0,
        "Standard": 1
    }

    test_preparation_map = {
        "None": 0,
        "Completed": 1
    }

    # Convert text to numbers
    gender = gender_map[gender]
    race = race_map[race]
    parent_education = parent_education_map[parent_education]
    lunch = lunch_map[lunch]
    test_preparation = test_preparation_map[test_preparation]

    # Create DataFrame
    input_data = pd.DataFrame(
        [[
            gender,
            race,
            parent_education,
            lunch,
            test_preparation,
            math_score,
            reading_score,
            writing_score,
            average_score
        ]],
        columns=[
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course",
    "math score",
    "reading score",
    "writing score",
    "Average Score"
]
    )

           # Prediction
    prediction = model.predict(input_data)
    confidence = model.predict_proba(input_data)

   # Display result
if prediction[0] == 0:
    st.success(f"🎉 {student_name} is predicted to have Good Performance.")

    confidence_percent = confidence[0][0] * 100
    st.write(f"Confidence: {confidence_percent:.2f}%")
    st.progress(confidence_percent / 100)

else:
    st.error(f"📚 {student_name} is predicted to Need Improvement.")

    confidence_percent = confidence[0][1] * 100
    st.write(f"Confidence: {confidence_percent:.2f}%")
    st.progress(confidence_percent / 100)
