import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

def analyze_dropout():
    np.random.seed(42)
    X = np.random.rand(100, 22)  # 100 samples, 5 features
    y = (X.sum(axis=1) > 11).astype(int)  # Binary classification

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Convert categorical variables to numeric using one-hot encoding
    marital_status = 1 if marital_status_var.get() == 'Married' else 0
    application_mode = 1 if application_mode_var.get() == 'Offline' else 0
    course = 1 if course_var.get() == 'Mathematics' else 0  # Replace with your actual values
    daytime_attendance = 1 if daytime_attendance_var.get() == 'Evening' else 0
    previous_qualification = 1 if previous_qualification_var.get() == "Bachelor's Degree" else 0  # Replace with your actual values
    nationality = 1 if nationality_var.get() == 'UK' else 0  # Replace with your actual values
    mothers_qualification = 1 if mothers_qualification_var.get() == "Bachelor's Degree" else 0  # Replace with your actual values
    fathers_qualification = 1 if fathers_qualification_var.get() == "Bachelor's Degree" else 0  # Replace with your actual values
    mothers_occupation = 1 if mothers_occupation_var.get() == 'Doctor' else 0  # Replace with your actual values
    fathers_occupation = 1 if fathers_occupation_var.get() == 'Doctor' else 0  # Replace with your actual values
    displaced = 1 if displaced_var.get() == 'Yes' else 0
    educational_needs = 1 if educational_needs_var.get() == 'Yes' else 0
    debtor = 1 if debtor_var.get() == 'Yes' else 0
    fees_up_to_date = 1 if fees_up_to_date_var.get() == 'No' else 0  # Replace with your actual values
    gender = 1 if gender_var.get() == 'Female' else 0  # Replace with your actual values
    scholarship_holder = 1 if scholarship_holder_var.get() == 'Yes' else 0
    international_student = 1 if international_student_var.get() == 'Yes' else 0

    # Get the input values from the entry fields
    age_at_enrollment = int(age_at_enrollment_entry.get())
    curricular_units_credited = int(curricular_units_credited_entry.get())
    curricular_units_enrolled = int(curricular_units_enrolled_entry.get())
    curricular_units_evaluations = int(curricular_units_evaluations_entry.get())
    curricular_units_approved = int(curricular_units_approved_entry.get())

    # Prepare the feature vector for prediction
    features = np.array([
        [marital_status, application_mode, course, daytime_attendance,
        previous_qualification, nationality, mothers_qualification, fathers_qualification,
        mothers_occupation, fathers_occupation, displaced, educational_needs, debtor,
        fees_up_to_date, gender, scholarship_holder, age_at_enrollment, international_student,
        curricular_units_credited, curricular_units_enrolled, curricular_units_evaluations,
        curricular_units_approved]
    ])
    print("Features:", [marital_status, application_mode,course, daytime_attendance,
        previous_qualification, nationality, mothers_qualification, fathers_qualification,
        mothers_occupation, fathers_occupation, displaced, educational_needs, debtor,
        fees_up_to_date, gender, scholarship_holder, age_at_enrollment, international_student,
        curricular_units_credited, curricular_units_enrolled, curricular_units_evaluations,
        curricular_units_approved])

    # Perform dropout prediction using the trained model
    dropout_probability = model.predict_proba(features)[:, 1]

    # Display the dropout probability in a message box
    messagebox.showinfo("Dropout Probability", f"The probability of dropout is: {dropout_probability[0]:.2f}")

# Create the main window
window = tk.Tk()
window.title("Student Dropout Analysis")

# (Rest of the code remains the same)
# Create and organize the widgets using the grid layout
label = tk.Label(window, text="Welcome to Student Dropout Analysis")
label.grid(row=0, column=0, columnspan=2, pady=10)

# Marital Status
marital_status_label = tk.Label(window, text="Marital Status:")
marital_status_label.grid(row=1, column=0, padx=10)
marital_status_var = tk.StringVar(window)
marital_status_var.set("Single")
marital_status_option_menu = tk.OptionMenu(window, marital_status_var, "Single", "Married", "Divorced")
marital_status_option_menu.grid(row=1, column=1, padx=10)

# Application Mode
application_mode_label = tk.Label(window, text="Application Mode:")
application_mode_label.grid(row=2, column=0, padx=10)
application_mode_var = tk.StringVar(window)
application_mode_var.set("Online")
application_mode_option_menu = tk.OptionMenu(window, application_mode_var, "Online", "Offline")
application_mode_option_menu.grid(row=2, column=1, padx=10)

# Course
course_label = tk.Label(window, text="Course:")
course_label.grid(row=4, column=0, padx=10)
course_var = tk.StringVar(window)
course_var.set("Computer Science")
course_option_menu = tk.OptionMenu(window, course_var, "Computer Science", "Mathematics", "Physics")
course_option_menu.grid(row=4, column=1, padx=10)

# Daytime Attendance
daytime_attendance_label = tk.Label(window, text="Daytime Attendance:")
daytime_attendance_label.grid(row=5, column=0, padx=10)
daytime_attendance_var = tk.StringVar(window)
daytime_attendance_var.set("Day")
daytime_attendance_option_menu = tk.OptionMenu(window, daytime_attendance_var, "Day", "Evening")
daytime_attendance_option_menu.grid(row=5, column=1, padx=10)

# Previous Qualification
previous_qualification_label = tk.Label(window, text="Previous Qualification:")
previous_qualification_label.grid(row=6, column=0, padx=10)
previous_qualification_var = tk.StringVar(window)
previous_qualification_var.set("High School Diploma")
previous_qualification_option_menu = tk.OptionMenu(
    window,
    previous_qualification_var,
    "High School Diploma",
    "Associate Degree",
    "Bachelor's Degree",
)
previous_qualification_option_menu.grid(row=6, column=1, padx=10)

# Nationality
nationality_label = tk.Label(window, text="Nationality:")
nationality_label.grid(row=7, column=0, padx=10)
nationality_var = tk.StringVar(window)
nationality_var.set("US")
nationality_option_menu = tk.OptionMenu(
    window,
    nationality_var,
    "US",
    "UK",
    "Canada",
    "Other",
)
nationality_option_menu.grid(row=7, column=1, padx=10)

# Mother's Qualification
mothers_qualification_label = tk.Label(window, text="Mother's Qualification:")
mothers_qualification_label.grid(row=8, column=0, padx=10)
mothers_qualification_var = tk.StringVar(window)
mothers_qualification_var.set("High School Diploma")
mothers_qualification_option_menu = tk.OptionMenu(
    window,
    mothers_qualification_var,
    "High School Diploma",
    "Associate Degree",
    "Bachelor's Degree",
)
mothers_qualification_option_menu.grid(row=8, column=1, padx=10)

# Father's Qualification
fathers_qualification_label = tk.Label(window, text="Father's Qualification:")
fathers_qualification_label.grid(row=9, column=0, padx=10)
fathers_qualification_var = tk.StringVar(window)
fathers_qualification_var.set("High School Diploma")
fathers_qualification_option_menu = tk.OptionMenu(
    window,
    fathers_qualification_var,
    "High School Diploma",
    "Associate Degree",
    "Bachelor's Degree",
)
fathers_qualification_option_menu.grid(row=9, column=1, padx=10)

# Mother's Occupation
mothers_occupation_label = tk.Label(window, text="Mother's Occupation:")
mothers_occupation_label.grid(row=10, column=0, padx=10)
mothers_occupation_var = tk.StringVar(window)
mothers_occupation_var.set("Teacher")
mothers_occupation_option_menu = tk.OptionMenu(
    window,
    mothers_occupation_var,
    "Teacher",
    "Engineer",
    "Doctor",
    "Other",
)
mothers_occupation_option_menu.grid(row=10, column=1, padx=10)

# Father's Occupation
fathers_occupation_label = tk.Label(window, text="Father's Occupation:")
fathers_occupation_label.grid(row=11, column=0, padx=10)
fathers_occupation_var = tk.StringVar(window)
fathers_occupation_var.set("Engineer")
fathers_occupation_option_menu = tk.OptionMenu(
    window,
    fathers_occupation_var,
    "Teacher",
    "Engineer",
    "Doctor",
    "Other",
)
fathers_occupation_option_menu.grid(row=11, column=1, padx=10)

# Displaced
displaced_label = tk.Label(window, text="Displaced:")
displaced_label.grid(row=12, column=0, padx=10)
displaced_var = tk.StringVar(window)
displaced_var.set("No")
displaced_option_menu = tk.OptionMenu(window, displaced_var, "Yes", "No")
displaced_option_menu.grid(row=12, column=1, padx=10)

# Educational Special Needs
educational_needs_label = tk.Label(window, text="Educational Special Needs:")
educational_needs_label.grid(row=13, column=0, padx=10)
educational_needs_var = tk.StringVar(window)
educational_needs_var.set("No")
educational_needs_option_menu = tk.OptionMenu(window, educational_needs_var, "Yes", "No")
educational_needs_option_menu.grid(row=13, column=1, padx=10)

# Debtor
debtor_label = tk.Label(window, text="Debtor:")
debtor_label.grid(row=14, column=0, padx=10)
debtor_var = tk.StringVar(window)
debtor_var.set("No")
debtor_option_menu = tk.OptionMenu(window, debtor_var, "Yes", "No")
debtor_option_menu.grid(row=14, column=1, padx=10)

# Tuition Fees Up to Date
fees_up_to_date_label = tk.Label(window, text="Tuition Fees Up to Date:")
fees_up_to_date_label.grid(row=15, column=0, padx=10)
fees_up_to_date_var = tk.StringVar(window)
fees_up_to_date_var.set("Yes")
fees_up_to_date_option_menu = tk.OptionMenu(window, fees_up_to_date_var, "Yes", "No")
fees_up_to_date_option_menu.grid(row=15, column=1, padx=10)

# Gender
gender_label = tk.Label(window, text="Gender:")
gender_label.grid(row=16, column=0, padx=10)
gender_var = tk.StringVar(window)
gender_var.set("Male")
gender_option_menu = tk.OptionMenu(window, gender_var, "Male", "Female")
gender_option_menu.grid(row=16, column=1, padx=10)

# Scholarship Holder
scholarship_holder_label = tk.Label(window, text="Scholarship Holder:")
scholarship_holder_label.grid(row=17, column=0, padx=10)
scholarship_holder_var = tk.StringVar(window)
scholarship_holder_var.set("No")
scholarship_holder_option_menu = tk.OptionMenu(window, scholarship_holder_var, "Yes", "No")
scholarship_holder_option_menu.grid(row=17, column=1, padx=10)

# Age at Enrollment
age_at_enrollment_label = tk.Label(window, text="Age at Enrollment:")
age_at_enrollment_label.grid(row=18, column=0, padx=10)
age_at_enrollment_entry = tk.Entry(window)
age_at_enrollment_entry.grid(row=18, column=1, padx=10)

# International Student
international_student_label = tk.Label(window, text="International Student:")
international_student_label.grid(row=19, column=0, padx=10)
international_student_var = tk.StringVar(window)
international_student_var.set("No")
international_student_option_menu = tk.OptionMenu(window, international_student_var, "Yes", "No")
international_student_option_menu.grid(row=19, column=1, padx=10)

# Curricular Units Credited
curricular_units_credited_label = tk.Label(window, text="Curricular Units Credited:")
curricular_units_credited_label.grid(row=20, column=0, padx=10)
curricular_units_credited_entry = tk.Entry(window)
curricular_units_credited_entry.grid(row=20, column=1, padx=10)

# Curricular Units Enrolled
curricular_units_enrolled_label = tk.Label(window, text="Curricular Units Enrolled:")
curricular_units_enrolled_label.grid(row=21, column=0, padx=10)
curricular_units_enrolled_entry = tk.Entry(window)
curricular_units_enrolled_entry.grid(row=21, column=1, padx=10)

# Curricular Units Evaluations
curricular_units_evaluations_label = tk.Label(window, text="Curricular Units Evaluations:")
curricular_units_evaluations_label.grid(row=22, column=0, padx=10)
curricular_units_evaluations_entry = tk.Entry(window)
curricular_units_evaluations_entry.grid(row=22, column=1, padx=10)

# Curricular Units Approved
curricular_units_approved_label = tk.Label(window, text="Curricular Units Approved:")
curricular_units_approved_label.grid(row=23, column=0, padx=10)
curricular_units_approved_entry = tk.Entry(window)
curricular_units_approved_entry.grid(row=23, column=1, padx=10)

# Button to Trigger Analysis
button = tk.Button(window, text="Analyze", command=analyze_dropout)
button.grid(row=24, column=0, columnspan=2, pady=10)

# Start the main event loop
window.mainloop()


