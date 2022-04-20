# seazone_challenge
![image](https://user-images.githubusercontent.com/94136773/164302391-3e35882e-acfe-45bd-a44f-cb98d6cb5c85.png)


## Context
### EDA project for a technical case proposed by the company Seazone.

Seazone is a real estate startup that uses technology to monetize properties through season rentals. 
In this context, the company made available some data from its advertisements to develop a data analysis and exploration project, requesting a final report on the development of this project and with some questions to be answered.
#### The report generated from the entire process can be accessed here [report](https://github.com/LucasAsilveira/seazone_challenge/blob/main/report_seazone_challenge.pdf)

## 1. Business Question

### 1.1. Problem

The company has some data regarding listings and revenue from properties leased on its platform.
These data need to be analyzed, organized and clean, so that some questions regarding property prices, company revenue and reservations can be answered.



 
### 1.2. Solution

It will be developed according to the request:

<b>Q1.</b> Prepare a report in pdf with the detailed development of the project.

<b>Q2.</b> Perform data analysis and cleaning

<b>Q3.</b> An interactive dashboard with filters for exploring and plotting data

<b>Q4.</b> Report with Business Hypotheses.

## 2. Solution Planning

### 2.1. what will be delivered

- Report with all stages of the project
- Interactive dashboard separated by topics and with multiple filters developed in Power BI.
- Report with business hypotheses and insights generated

### 2.2. Tools Used

- Python 3.8 
- Pycharm 2020.2
- Libries Pandas
- Git and GitHub
- Google Sheets
- Power BI 


### 2.3. Process

- Data collect: Provided by the customer in csv files
- Data Cleaning: Organize and Rename columns, describe types, dimensions, check missing data and Perform statistical Description, create business hypotheses creating new variables for further exploration.
- Data exploration: Perform graphical analysis of the variables, validate the hypotheses raised.
- Dashboard production: Plot graphs with the main features to answer questions

## 3. Key Insights from Data

1. Weekends can have up to 20% more occupancy.(FALSO)
- Generated Insight: Despite the higher occupancy during weekends, they do not have such a high rate. Being able to carry out campaigns and promotions based on this

2. Annual revenue grows by 20% per year or more.(TRUE)
- Generated Insight: Revenue growth was 175% from 2020 to 2021,and in the year 2022, in the first three months, it has already surpassed the total for 2021. Therefore, the company can work with expectations of increasing revenues.

3. Hotel type properties have a higher occupancy rate than other types.(TRUE)
- Generated Insight: Hotels have a higher occupancy rate, which may lead the company to think about increasing the disclosure of other types of properties since they have many advertisements of other types

More business hypotheses and the survey and solution of all hypotheses can be found at this [bussiness_hypoteses.pdf](https://github.com/LucasAsilveira/seazone_challenge/blob/main/bussiness_hypoteses.pdf) 

## 4. Business Questions:
### Below is just a summary with the questions and answers, the entire development of the answers and graphics used are in Item 8 of the report that can be found in this [report_seazone_challenge.pdf](https://github.com/LucasAsilveira/seazone_challenge/blob/main/report_seazone_challenge.pdf)


Q.1. What is the expected price and revenue for a listing tagged as JUR MASTER 2Q in march?

RESPOSTA: R$ 645,00

Q.2. What is Seazone’s expected revenue for 2022? Why?

RESPOSTA: R$ 30 milhões

Q.3. How many reservations should we expect to sell per day? Why?¶

RESPOSTA: An average of 183 reservations per day is expected

Q.4. At what time of the year should we expect to have sold 10% of our new year'snights? And
50%? And 80%?

RESPOSTA: of the year should we expect to have sold 10% : 70 days in advance,
50% : 20 days in advance and 80% : 8 days in advance


Q.5. On the impact of the COVID-19 pandemic:

RESPOSTA: Analyzing the plotted data, we can estimate strong losses in billing due to the
pandemic.

- Has the industry recovered?

RESPOSTA: It is in the process of full recovery and should be normalized by the next high
season.

## 5. Dashboard:

The dashboard developed to answer business questions and carry out business hypotheses can be found through this [seazone_challange_dashboard](https://app.powerbi.com/view?r=eyJrIjoiMjA0Y2FmMDQtY2M0NC00MTkzLWEzZDctMTZmYjliZWJhMDZlIiwidCI6Ijc1ZDUwYjU2LWY2YWUtNDUzZS1hZGU2LTc3OThmODM1ZTAwZiJ9) or viewed in pdf form at this [seazone_challange_dashboard.pdf](https://github.com/LucasAsilveira/seazone_challenge/blob/main/power_bi_project/seazone_challange_dashboard.pdf)

This dashboard has been divided into 4 tabs:

- 'Faturamento': Where there are graphs of the average income of each type of property, total annual invoicing, invoicing by seasons of the year and monthly invoicing.

- 'Reservas': There is a graph with listings that were occupied and remained vacant by percentage in the form of a pie, a stacked graph with this relationship over time and a bar graph where we have the total of Listings that were month by month busy and left vacant.

- 'Localizaçao': In this tab we find the average revenue per location, the number of properties per location and a table where we have some detail of each Listing

- 'Ano Novo' : In this tab we have a table where we have the days in advance that each New Year's reservation took place and a cumulative chart where we can see the dates that were occupied in relation to the percentage of occupancy on New Year's night.

## 6. Conclusion:

 The final objective was achieved, using the available data to answer the questions and formulate a report. There were some difficulties encountered during the process, the data history is short, having only 2 full years and these suffering interference from the pandemic. The time factor was also an obstacle because the deadline for carrying out the project was narrow.
 Based on the data, we can see that it is a sector with growing demand, even though the pandemic factor has disrupted the number of ads and revenue has grown in recent years, being a sector in growth and development.
 

## 7. Next steps:

- Possible improvements, after receiving feedback on the usability of the dashboard. 
- Implementation of Machine Learning to estimate prices and occupancy rate 








