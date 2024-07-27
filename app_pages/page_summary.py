import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **customer** is a person who makes a hotel room booking.\n"
        f"* A **booking** has details of the reservation per customer's choices.\n"
        f"* A **cancelled** booking is a reservation that's been cancelled.\n\n"
        f"**Project Dataset**\n"
        f"* This data set contains booking information for a city hotel and a resort hotel. "
        f"It includes information such as when the booking was made, "
        f"length of stay, the number of adults, children, and/or babies, "
        f"and the number of available parking spaces, among other things. "
        f"All personally identifying information has been removed from the data.")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/marcgithub23/pp5-hotel-hocuspocus).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - Conducting conventional data analysis, the client is interested in "
        f"answering the following questions:\n "
        f"Which months have the highest number of cancellations?\n"
        f"What are the top 5 countries with the highest number of cancellations?\n"
        f"Which booking channels have the highest number of cancellations?\n"
        f"Are bookings with weekend nights stay more likely to be cancelled than those with none?\n"
        f"* 2 - The client is interested in determining whether or not a given booking will be cancelled."
        )
