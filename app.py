import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_data_analysis import page_data_analysis_body
from app_pages.page_predictor import page_predictor_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_cancellation import page_predict_cancellation_body

# Create an instance of the app
app = MultiPage(app_name="Predictor")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Data Analysis", page_data_analysis_body)
app.add_page("Predict Cancellation", page_predictor_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predict Cancellation", page_predict_cancellation_body)

# Run the  app
app.run()