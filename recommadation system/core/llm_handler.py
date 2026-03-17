# Abstract class or base functions for LLM interaction
from langchain.prompts import PromptTemplate
# You will instantiate your Langchain integrations here.

def get_recommendation_chain(llm):
    """
    Sets up the Langchain chain for course recommendations.
    """
    template = """
    You are an expert career counselor. Based on the following student details, 
    recommend the most suitable higher education fields (e.g., Engineering, Medical, Commerce, Arts, Design).
    
    Student Interests: {interests}
    Student Skills: {skills}
    Academic Preferences: {academic_preferences}
    
    Provide a clear, encouraging recommendation with reasoning.
    """
    prompt = PromptTemplate(
        input_variables=["interests", "skills", "academic_preferences"],
        template=template
    )
    
    # Return the chain (conceptually: prompt | llm)
    return prompt | llm
