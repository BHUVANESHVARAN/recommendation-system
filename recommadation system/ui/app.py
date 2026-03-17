import streamlit as st

st.set_page_config(page_title="Course Recommender", page_icon="🎓")

st.title("🎓 AI-Based Course Recommendation System")
st.write("Confused about what to do after 12th grade? Tell us about yourself, and our AI career counselor will help you find the right path!")

st.header("Tell us about yourself")

interests = st.text_area("What are your main interests? (e.g., coding, helping people, drawing, business)", height=100)
skills = st.text_area("What are your key skills? (e.g., mathematics, communication, problem-solving)", height=100)
academic_preferences = st.selectbox("What is your academic background/preference?", 
                                    ["Science (PCM)", "Science (PCB)", "Commerce", "Arts/Humanities", "Undecided"])

if st.button("Get Recommendations"):
    if interests and skills:
        st.info("Thinking... (Here is where we will call the LLM API via Langchain!)")
        # Placeholder for LLM response
        st.success("Based on your inputs, we recommend exploring fields in **Engineering** or **Computer Science**! (This is a placeholder response)")
    else:
        st.warning("Please provide your interests and skills to get a recommendation.")
