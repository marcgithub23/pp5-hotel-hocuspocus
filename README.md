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
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.

