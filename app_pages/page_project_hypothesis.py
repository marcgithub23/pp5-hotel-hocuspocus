import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # Conclusions taken from data analysis notebook
    st.success(
        f"* We suspect majority of booking cancellations are in the summer season: Correct. "
        f"Data analysis shows that August and July are the top 2 highest cancellation by month. "
        f"This is during the summer season.\n\n"

        f"* We suspect that there are more cancellations for "
        f"bookings made through distribution partners than direct bookings: Correct. "
        f"The data analysis conducted supports this hypothesis.\n\n "
        
        f"* We suspect that bookings with weekend nights stay are "
        f"more likely to be cancelled than those with none: False. "
        f"Data analysis shows that bookings without any weekend nights stay "
        f"are cancelled more than bookings with weekend nights stay."
        )
