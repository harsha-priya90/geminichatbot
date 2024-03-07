import streamlit as st
st.title("LEARNER'S HUB")
st.markdown("#### Offering the best courses")
st.text("Welcome to learners school. We offer the top courses,learn the courses of your interest here")
st.markdown(":smiley:")
st.sidebar.title("Student Details")
st.sidebar.text_input("Enter the name")
st.sidebar.text_input("Enter your email address")
st.sidebar.button("Submit")
st.selectbox("Which course do you want to study",["Azure","AWS","Python","SQL","Langchain"])
st.radio("Enter the level to which you want to learn course",["Beginner","Intermediate","Advance","Expert"])
st.multiselect("Enter your Qualifications",["B.TECH","M.TECH"])
st.multiselect("Enter your skills",["C","JAVA","C++","dotnet","scala"])
st.slider("Rate your Skill on 10",0,10)
st.select_slider("Enter your grade",["A","A+","B","B+","C","c+"])
st.date_input("Enter the date from which you want to start the course")
st.time_input("Start time of live class")
st.text_area("Suggest the other courses you  want to learn")
st.file_uploader("upload your resume here for future reference")
st.checkbox("Remember My Details")



Access the webpage here
https://myfirstwebpage.streamlit.app/
