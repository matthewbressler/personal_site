import streamlit as st
import info
import pandas as pd

#About Me
def aboutMeSection():
    st.header("About Me")
    st.image(info.profile_picture, width = 500)
    st.write(info.about_me)
    st.write("---")
aboutMeSection()

#Sidebar Links
def linksSection():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_img_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_img_url}" alt="GitHub" width="75" height="75"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    
    st.sidebar.text("Contact me")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_img_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
linksSection()

#Education
def educationSection(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")

    st.write("**Relevant Coursework:** ")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config = {
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "Description"},
        hide_index = True,
        )
    st.write("---")

educationSection(info.education_data,info.course_data)

#Professional Experience

def experienceSection(experience_data):
    st.header("Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width = 250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experienceSection(info.experience_data)

#Projects

def projectSection(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
projectSection(info.projects_data)

#Skills

def skillsSection(programming_data, spoken_data):
    '''
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill)}")
        st.progress(percentage)
    '''
    st.header("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write("{}{}: {}".format(spoken, info.spoken_icons.get(spoken), proficiency))
    st.write("---")
# skillsSection(info.programming_data, info.spoken_data)

#Activities

def activitiesSection(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Extracurriculars"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander("{}".format(title))
            expander.image(image, width = 250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Extracurriculars")
        for title, details in activity_data.items():
            expander = st.expander("{}".format(title))
            for bullet in details:
                expander.write(bullet)

    st.write("---")
                
activitiesSection(info.leadership_data, info.activity_data)



