## About Project
* This project aims to build a predictive model to implement as a tool via a dashboard to predict whether a customer will cancel their booking or not.
* The link to the deployed dashboard is: [PP5 Hotel Hocuspocus](https://pp5-hotel-hocuspocus-10951e8f369c.herokuapp.com/)


## Dataset Content
* The dataset is from [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data).
* A fictitious business scenario was created based on the dataset to conduct conventional data analysis and develop an ML predictive model to meet business requirements.
* This dataset contains booking information for a city hotel and a resort hotel, and includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, among other things. All personally identifying information has been removed from the data.
* The dataset from Kaggle originally contains 100k+ entries, but in this project the dataset has been scaled down to 8k entries to minimise the size of the model pipeline for pushing to repo. It contains the following 32 variables:

| __No.__ | __Variable__ | __Description__ | __Units__ |
|   :---    |     :---     |       :---      |       :---      |
| 1 | __hotel__ | Type of hotel | Resort Hotel, City Hotel |
| 2 | __is_canceled__ | Reservation cancellation status |  0 = not cancelled, 1 = cancelled |
| 3 | __lead_time__ | Number of days between booking and arrival | 0-629 days |
| 4 | __arrival_date_year__ | Year of arrival | 2015-2017 |
| 5 | __arrival_date_month__ | Month of arrival | January-December |
| 6 | __arrival_date_week_number__ | Week number of the year for arrival | 1-53 |
| 7 | __arrival_date_day_of_month__ | Day of the month of arrival | 1-31 |
| 8 | __stays_in_weekend_nights__ | Number of weekend nights (Saturday and Sunday) the guest stayed or booked | 0-16 |
| 9 | __stays_in_week_nights__ | Number of week nights the guest stayed or booked | 0-40 |
| 10 | __adults__ | Number of adults | 0-27 |
| 11 | __children__ | Number of children | 0-3 |
| 12 | __babies__ | Number of babies | 0-2 |
| 13 | __meal__ | Type of meal booked | BB, FB, HB, SC, Undefined |
| 14 | __country__ | Country of origin of the guest | Countries |
| 15 | __market_segment__ | Market segment designation | Offline TA/TO, Online TA, Groups, Direct, Corporate, Complementary, Aviation |
| 16 | __distribution_channel__ | Booking distribution channel | TA/TO, Direct, Corporate, GDS |
| 17 | __is_repeated_guest__ | If the guest is a repeat customer | 0 = not repeated, 1 = repeated |
| 18 | __previous_cancellations__ | Number of previous bookings that were canceled by the customer | 0-26
| 19 | __previous_bookings_not_canceled__ | Number of previous bookings that were not canceled by the customer | 0-57 |
| 20 | __reserved_room_type__ | Type of reserved room | A, D, E, G, F, B, P, C, H, L |
| 21 | __assigned_room_type__ | Type of assigned room | 'A', 'D', 'E', 'C', 'G', 'B', 'K', 'F', 'P', 'H', 'I' |
| 22 | __booking_changes__ | Number of changes made to the booking | 0-14 |
| 23 | __deposit_type__ | Type of deposit made | No Deposit, Refundable, Non Refund |
| 24 | __agent__ | ID of the travel agent responsible for the booking | 1-531 |
| 25 | __company__ | ID of the company responsible for the booking | 9-534 |
| 26 | __days_in_waiting_list__ | Number of days the booking was in the waiting list | 0-391 |
| 27 | __customer_type__ | Type of customer | Transient, Contract, Transient-Party, Group |
| 28 | __adr__ | Average Daily Rate | 0-392 |
| 29 | __required_car_parking_spaces__ | Number of car parking spaces required | 0-2 |
| 30 | __total_of_special_requests__ | Number of special requests made | 0-5 |
| 31 | __reservation_status__ | Last reservation status | Check-Out, Canceled, No-Show |
| 32 | __reservation_status_date__ | Date of the last reservation status | Dates |


## Business Requirements
The client wishes to come up with operational planning for minimising cancellations, improving room occupancy, and maximising revenue based on data-driven insights. After discussion with the stakeholders, the following two business requirements were agreed upon:

* Conducting conventional data analysis, the client is interested in answering the following questions: Which months have the highest number of cancellations? What are the top 5 countries with the highest number of cancellations? Which booking channels have the highest number of cancellations? Are bookings with weekend nights stay more likely to be cancelled than those with none?

* The client is interested in determining whether or not a given booking will be cancelled.

## Hypothesis and how to validate?
* We suspect majority of booking cancellations are in the summer season.
    * Plot a countplot of the number of cancellations per month in descending order.
* We suspect that there are more cancellations for bookings made through distribution partners than direct bookings.
    * Plot a countplot of the number of cancellations by distribution channel in descending order.
* We suspect that bookings with weekend nights stay are more likely to be cancelled than those with none.
    * Plot a histogram of the distribution of stays in weekend nights.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1:** Conventional Data Analysis and Visualization
    * We will conduct conventional data analysis on the following variables: arrival_date_month, country, distribution_channel, and stays_in_weekend_nights to answer the questions from stakeholders.
    * We will plot the above variables against is_canceled to visualise insights.

* **Business Requirement 2:** Classification for Predicting Cancellation
    * We want to predict if a customer will cancel their booking or not. We want to build a binary classifier.


## ML Business Case

### Predict Cancellation

#### Classification Model

* We want an ML model to predict if a customer will cancel their booking or not based on historical data, which doesn't include the following variables:
    * company (irrelevant as it's the company's ID number)
    * agent (irrelevant as it's the agent's ID number)
    * country (high cardinality and might affect fitting of model)
    * arrival_date_year (model must be able to generalise future bookings)
    * reservation_status (directly related to is_cancel and might cause data leakage)
    * reservation_status_date (same reason as above)
    * assigned_room_type (same reason as above; only set in the system when guests actually check-in)
* The target variable is categorical and contains 2-classes. We consider a classification model. It is a supervised model, a 2-class, single-label, classification model output: 0 (not cancelled), 1 (cancelled)
* Our ideal outcome is to provide the client's operational planning team with reliable insight into minimising cancellations, improving room occupancy, and thus maximising revenue.
* The model success metrics are:
    * At least 80% Recall for cancellation on train and test sets
    * Version 1 of the predictive model achieves 87% Recall for cancellation on the train set, but only 66% on the test set. This suggests that the model has overfitted as there is a considerable difference.
    * Stakehoders are made aware of this performance and future improvements, such as further extensive hyperparameters optimisation or collection of new variable to add to the dataset, will be made to fine tune the model's performance.
* Heuristics: Currently, there is no approach to predict cancellations.
* The training data to fit the model comes from Kaggle. This dataset contains about 100k+ entries, but in this project the dataset has been scaled down to 8k entries to minimise the size of the model pipeline.
    * Train data - target: is_canceled; features: all other variables, except the ones listed above.


## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
* Quick project summary
    * Project Terms & Jargon
    * Describe Project Dataset
    * State Business Requirements
![Screenshot of quick project summary page](/documentation/quick_project_summary.png)

### Page 2: Data Analysis
* List the questions from the client as per business requirement 1
* Checkbox: data inspection (display the number of rows and columns in the data, and display the first ten rows of the data)
* Display the answers to the questions as bulleted list.
* Checkboxes to show each plot that provides the answers to the questions.
![Screenshot of data analysis page](/documentation/data_analysis1.png)
![Screenshot of data analysis page](/documentation/data_analysis2.png)
![Screenshot of data analysis page](/documentation/data_analysis3.png)
![Screenshot of data analysis page](/documentation/data_analysis4.png)
![Screenshot of data analysis page](/documentation/data_analysis5.png)
![Screenshot of data analysis page](/documentation/data_analysis6.png)
![Screenshot of data analysis page](/documentation/data_analysis7.png)

### Page 3: Predict Cancellation
* State business requirement 2
* Set of widgets inputs, which relates to a customer's booking, to predict cancellation.
* "Run predictive analysis" button that serves the booking data to the ML pipelines and predicts if the customer will cancel their booking or not.
![Screenshot of predict cancellation page](/documentation/predict_cancellation.png)

### Page 4: Project Hypothesis and Validation
* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
    * We suspect majority of booking cancellations are in the summer season.
        * Correct. Data analysis shows that August and July are the top 2 highest cancellation by month. This is during the summer season.
    * We suspect that there are more cancellations for bookings made through distribution partners than direct bookings.
        * Correct. The data analysis conducted supports this hypothesis.
    * We suspect that bookings with weekend nights stay are more likely to be cancelled than those with none.
        * False. Data analysis shows that bookings without any weekend nights stay are cancelled more than bookings with weekend nights stay.
![Screenshot of project hypothesis and validation page](/documentation/hypothesis_validation.png)

### Page 5: ML: Predict Cancellation
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance
![Screenshot of ML predict page](/documentation/ml_predict1.png)
![Screenshot of ML predict page](/documentation/ml_predict2.png)
![Screenshot of ML predict page](/documentation/ml_predict3.png)
![Screenshot of ML predict page](/documentation/ml_predict4.png)


## Unfixed Bugs
* There were no known unfixed bugs in this project.

## Deployment
### Heroku

* The App live link is: https://pp5-hotel-hocuspocus-10951e8f369c.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps:

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Jupyter: used for its interactive web application for creating the necessary notebooks to write the code for the ML project.
* Streamlit: used to create the dashboard to put their code into a web application.
* Numpy: is a Python library used for working with arrays, for example return an array of zeros with the same shape and type as a given array.
* Pandas: used for working with data sets, for example read a comma-separated values (csv) file into DataFrame.
* Matplotlib, Seaborn, and Plotly: used for visualization of the data by generating different type of plots.
* Pandas Profiling: used to create a comprehensive Report of the dataset to help with Exploratory Data Analysis (EDA).
* ppscore: used to determine the predictive power score between two columns.
* feature-engine: used to engineer the dataset’s variables and select features for use in the machine learning model.
* scikit-learn: is a Python library for machine learning used for example split randomly the train and test sets.
* imbalanced-learn: used for handling target imbalance, e.g. SMOTE.


## Credits

### Content

* The dataset is from [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data).

### Coding

* This project was based on Code Institute's Churnometer walkthrough project.
* This [Kaggle notebook](https://www.kaggle.com/code/farzadnekouei/hotel-booking-cancellation-prediction/notebook) by [Farzad Nekouei](https://www.kaggle.com/farzadnekouei) was also consulted for ideas.
* This [Kaggle notebook](https://www.kaggle.com/code/niteshyadav3103/hotel-booking-prediction-99-5-acc) by [Nitesh Yadav](https://www.kaggle.com/niteshyadav3103) was also consulted for ideas.


## Acknowledgements (optional)
* I would like to thank my mentor, Rohit Sharma, for his tips and support in completing this project.