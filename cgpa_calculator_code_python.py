# gpa_calculator.py
import streamlit as st
import pandas as pd

# ----------------------- PAGE CONFIG -----------------------
st.set_page_config(page_title="🎓 GPA & CGPA Calculator", layout="centered")

# ----------------------- CUSTOM CSS ------------------------
st.markdown("""
    <style>
        body {
            background-color: #f2f7ff;
        }
        .main {
            background-color: #ffffff;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1, h2, h3 {
            text-align: center;
            color: #0078D4;
        }
        .stButton button {
            background: linear-gradient(90deg, #0078D4, #00B4DB);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 24px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: linear-gradient(90deg, #00B4DB, #0078D4);
            transform: scale(1.05);
        }
        table {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------- TITLE -----------------------------
st.title("🎓 GPA & CGPA Calculator")
st.markdown("Easily calculate your GPA and CGPA based on your marks and credit hours for each subject.")

# ----------------------- INPUT FORM ------------------------
st.header("🧮 Enter Your Subjects Details")

num_subjects = st.number_input("How many subjects do you have?", min_value=1, max_value=20, step=1)

subjects_data = []

for i in range(int(num_subjects)):
    st.subheader(f"📘 Subject {i+1}")
    subject_name = st.text_input(f"Subject {i+1} Name", key=f"name_{i}")
    marks = st.number_input(f"Enter Marks for {subject_name or 'Subject'}", min_value=0.0, max_value=100.0, step=0.5, key=f"marks_{i}")
    credit_hours = st.number_input(f"Credit Hours for {subject_name or 'Subject'}", min_value=1.0, max_value=5.0, step=0.5, key=f"credit_{i}")
    subjects_data.append({"Subject": subject_name, "Marks": marks, "Credit Hours": credit_hours})

# ----------------------- GPA CALCULATION -------------------
def marks_to_gpa(marks):
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0

# ----------------------- RESULT SECTION --------------------
if st.button("🎯 Calculate GPA & CGPA"):
    df = pd.DataFrame(subjects_data)
    df["GPA"] = df["Marks"].apply(marks_to_gpa)
    df["Grade Points"] = df["GPA"] * df["Credit Hours"]
    
    total_credit_hours = df["Credit Hours"].sum()
    total_grade_points = df["Grade Points"].sum()
    cgpa = total_grade_points / total_credit_hours if total_credit_hours > 0 else 0.0
    
    st.success("✅ Calculation Successful!")
    st.subheader("📊 Detailed GPA Report")
    st.dataframe(df.style.background_gradient(cmap="Blues"))
    
    st.markdown(f"### 🎯 **Your Overall CGPA:** `{cgpa:.2f}`")

    # Optional Chart
    st.bar_chart(df.set_index("Subject")["GPA"])

# ----------------------- FOOTER ----------------------------
st.markdown("---")
st.markdown("✨ *Created with ❤️ using Streamlit by Mirza Deen Muhammad*")
