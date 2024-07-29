import streamlit as st


def predict_cancellation(X_live, cancel_features, cancel_pipeline_dc_fe, cancel_pipeline_model):

    # From live data, subset features related to this pipeline
    X_live_cancel = X_live.filter(cancel_features)

    # Apply data cleaning / feat engine pipeline to live data
    X_live_cancel_dc_fe = cancel_pipeline_dc_fe.transform(X_live_cancel)

    # Predict
    cancel_prediction = cancel_pipeline_model.predict(X_live_cancel_dc_fe)
    cancel_prediction_proba = cancel_pipeline_model.predict_proba(
        X_live_cancel_dc_fe)
    # st.write(cancel_prediction_proba)

    # Create a logic to display the results
    cancel_prob = cancel_prediction_proba[0, cancel_prediction][0]*100
    if cancel_prediction == 1:
        cancel_result = 'will'
    else:
        cancel_result = 'will not'

    statement = (
        f'### There is {cancel_prob.round(1)}% probability '
        f'that this customer **{cancel_result} cancel their booking**. \n'
        f"Please note that the current model is overfitting, but future improvements "
        f"will be made to fine tune the model performance. "
    )

    st.write(statement)

    return cancel_prediction
