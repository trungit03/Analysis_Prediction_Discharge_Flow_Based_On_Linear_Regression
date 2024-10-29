# **Discharge Flow Prediction**
## Overview
* This project focuses on building a model to predict discharge flow for hydropower reservoirs.
* Data used: Using selenium to scrape data on the website of Vietnam Electricity Company [EVN](https://www.evn.com.vn/c3/thong-tin-ho-thuy-dien/Muc-nuoc-cac-ho-thuy-dien-117-123.aspx). Data was taken from 2021 to July 16, 2024. The data has more than 39,000 records with 3 datasets: South Central Coast, Northwest Region, and Central Highlands.
* Additionally using Streamlit to create a basic website and then embed the model in it.
___
To clone the project to your local machine, use the following command:
```bash
git clone https://github.com/trungit03/Discharge_Flow_Prediction.git
cd Discharge_Flow_Prediction
___
Then, install the required libraries using the following command:
```bash
pip install requirements.txt
cd repo
___
To run web.py, use the following command:
```bash
streamlit run web.py

