import streamlit as st
import pandas as pd
from src.data_management import load_bookings_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_cancellation


def page_predictor_body():

    # Load predict cancellation files
    version = 'v1'
    cancel_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_cancellation/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    cancel_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_cancellation/{version}/clf_pipeline_model.pkl")
    cancel_features = (
        pd.read_csv(f"outputs/ml_pipeline/predict_cancellation/{version}/X_train.csv")
            .columns
            .to_list()
    )

    st.write("### Predict Cancellation Interface")
    st.info(
        f"* The client is interested in determining whether or not a given booking will be cancelled. "
    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict on live data
    if st.button("Run Predictive Analysis"):
        cancel_prediction = predict_cancellation(
            X_live, cancel_features, cancel_pipe_dc_fe, cancel_pipe_model)


def check_variables_for_UI(cancel_features):
    import itertools

    # The widgets inputs are the features used in the cancel pipeline
    combined_features = set(
        list(
            itertools.chain(cancel_features)
        )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    # Load dataset
    df = load_bookings_data()

    # Create input widgets for 8 features
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
    # {
    #     'market_segment', 'adr', 'arrival_date_day_of_month', 'deposit_type',
    #     'lead_time', 'arrival_date_week_number', 'total_of_special_requests',
    #     'stays_in_week_nights'
    # }

    # Create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # Draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "deposit_type"
        st_widget = st.selectbox(
            label="Deposit type",
            options=df[feature].unique(),
            help="Type of deposit made"
        )
    X_live[feature] = st_widget

    with col2:
        feature = "lead_time"
        st_widget = st.number_input(
            label="Lead time",
            min_value=0,
            max_value=365,
            help="Number of days between booking and arrival"
        )
    X_live[feature] = st_widget

    with col3:
        feature = "market_segment"
        st_widget = st.selectbox(
            label="Market segment",
            options=df[feature].unique(),
            help="Market segment designation"
        )
    X_live[feature] = st_widget

    with col4:
        feature = "total_of_special_requests"
        st_widget = st.number_input(
            label="Number of special requests",
            min_value=0,
            max_value=df[feature].max(),
            help="Number of special requests made"
        )
    X_live[feature] = st_widget

    with col5:
        feature = "adr"
        st_widget = st.number_input(
            label="Average daily rate",
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=df[feature].median(),
            help="Number of special requests made"
        )
    X_live[feature] = st_widget

    with col6:
        feature = "arrival_date_week_number"
        st_widget = st.number_input(
            label="Arrival date week number",
            min_value=1,
            max_value=53,
            help="Week number of the year for arrival"
        )
    X_live[feature] = st_widget

    with col7:
        feature = "arrival_date_day_of_month"
        st_widget = st.number_input(
            label="Day of the month of arrival",
            min_value=1,
            max_value=31,
            help="Day of the month of arrival"
        )
    X_live[feature] = st_widget

    with col8:
        feature = "stays_in_week_nights"
        st_widget = st.number_input(
            label="Number of week nights booked",
            min_value=0,
            max_value=260,
            help="Number of week nights booked"
        )
    X_live[feature] = st_widget

    return X_live
