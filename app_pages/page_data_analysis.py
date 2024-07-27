import numpy as np
import streamlit as st
from src.data_management import load_bookings_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_data_analysis_body():

    # Load data
    df = load_bookings_data()

    # Hard copied from data analysis notebook
    vars_to_study = [
        'arrival_date_month',
        'country',
        'distribution_channel',
        'stays_in_weekend_nights'
    ]

    st.write("### Data analysis")
    st.info(
        f"* The client is interested in answering the following questions:\n"
        f"Which months have the highest number of cancellations?\n"
        f"What are the top 5 countries with the highest number of cancellations?\n"
        f"Which booking channels have the highest number of cancellations?\n"
        f"Are bookings with weekend nights stay more likely to be cancelled than those with none?\n")

    # Inspect data
    if st.checkbox("Inspect Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Conventional Data Analysis Study Summary
    st.write(
        f"* A conventional data analysis study was conducted in the notebook "
        f"to answer the questions listed above. \n"
        f"The following variables were used for data analysis: **{vars_to_study}**"
    )

    # Text from summary of conclusions section in data analysis notebook
    st.info(
        f"* August and July are the top 2 months with the highest number of cancellations. "
        f"This is during the summer season.\n"
        f"* The top 5 countries with the highest number of cancellations are: "
        f"Portugal, the Uk, France, Spain, and Italy.\n"
        f"* There are more cancellations of bookings made through TA's (Travel Agencies) "
        f"or TO's (Tour Operators) as opposed to bookings made directly with the hotel.\n"
        f"* Bookings without any weekend nights stay are cancelled "
        f"more than bookings with weekend nights stay.\n"
    )

    # Code copied from data analysis notebook in conventional data analysis section
    df_eda = df.filter(vars_to_study + ['is_canceled'])

    # Arrival date month
    if st.checkbox("Arrival date month"):
        cancellations_by_month(df_eda)

    # Country
    if st.checkbox("Country"):
        cancellations_by_country(df_eda)

    # Distribution channels
    if st.checkbox("Distribution channels"):
        cancellations_by_dist_channel(df_eda)

    # Weekend nights stay
    if st.checkbox("Weekend nights stay"):
        cancellations_by_weekend_nights(df_eda)


# Code logic from arrival date month section in data analysis notebook
def cancellations_by_month(df_eda):
    cancellations = df_eda[df_eda['is_canceled'] == 1].groupby(
        'arrival_date_month'
    ).size()
    sorted_months = cancellations.sort_values(ascending=False).index.tolist()

    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=df_eda,
        x='arrival_date_month',
        hue='is_canceled',
        order=sorted_months
    )
    plt.xticks(rotation=90)
    plt.title('Number of Cancellations per Month')
    plt.xlabel('arrival_date_month')
    plt.ylabel('count')
    st.pyplot()


# Code logic from country section in data analysis notebook
def cancellations_by_country(df_eda):
    cancellations_by_country = df_eda[df_eda['is_canceled'] == 1].groupby(
    'country'
    ).size()
    top_5_countries = cancellations_by_country.nlargest(5).index.tolist()
    df_top_5 = df_eda[df_eda['country'].isin(top_5_countries)]

    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=df_top_5,
        x='country',
        hue='is_canceled',
        order=top_5_countries
    )
    plt.title('Top 5 Countries with the Highest Number of Cancellations')
    plt.xlabel('country')
    plt.ylabel('count')
    plt.xticks(rotation=90)
    st.pyplot()


# Code logic from distribution channels section in data analysis notebook
def cancellations_by_dist_channel(df_eda):
    cancellations_by_channel = df_eda[df_eda['is_canceled'] == 1].groupby(
    'distribution_channel'
    ).size()
    sorted_channels = cancellations_by_channel.sort_values(
    ascending=False
    ).index.tolist()

    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=df_eda,
        x='distribution_channel',
        hue='is_canceled',
        order=sorted_channels
    )
    plt.title('Number of Cancellations by Distribution Channel')
    plt.xlabel('distribution_channel')
    plt.ylabel('count')
    plt.xticks(rotation=90)
    st.pyplot()


# Code logic from weekend nights stay section in data analysis notebook
def cancellations_by_weekend_nights(df_eda):
    plt.figure(figsize=(12, 6))
    sns.histplot(
        data=df_eda,
        x='stays_in_weekend_nights',
        hue='is_canceled',
        kde=True,
        element='step'
    )
    plt.title('Distribution of Stays in Weekend Nights')
    plt.xlim(0, 8)
    plt.xlabel('stays_in_weekend_nights')
    plt.ylabel('count')
    st.pyplot()
