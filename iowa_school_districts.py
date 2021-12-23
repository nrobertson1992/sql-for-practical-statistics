# Source for this data: https://data.iowa.gov/browse?category=Education

# Streamlit!
import streamlit as st 

# Python packages for supporting the query engine.
from pandasql import sqldf
import pandas as pd 

# Import data.
iowa_district_expenditures = pd.read_csv('iowa_district_expenditures.csv')
iowa_district_graduations = pd.read_csv('iowa_district_graduations.csv')


# Update columns.
iowa_district_expenditures.columns = ['fiscal_year','actual_re_estimated_budget','aea','dist','de_dist','district_name','column_name', 'fund','source','expenditures_per_pupil','amount','enrollment_category','enrollment_category_number']
iowa_district_graduations.columns = ['graduating_class','fall_freshman_year','district','district_name','graduates','total_cohort','graduation_rate','graduation_rate_category']

st.title('SQL for Practical Statistics: Iowa School Districts')




st.write('A workspace for querying data provided by data.iowa.gov on their school districts.')

st.sidebar.subheader('Table Documentation')

st.sidebar.write('Use this to better understand what data are in each of the tables in our database.')

with st.sidebar.expander('Table Reference: iowa_district_expenditures', expanded=False):
	st.write("""
			School district expenditures by fiscal year starting in FY 2017 (year ending June 30, 2017). 
			Data is provided by school districts to the Department of Education to complete their Certified 
			Annual Report (CAR).

			* fiscal_year: Fiscal Year of Expenditure.
			* actual_re_estimated_budget: Actual - Data is from the Certified Annual Report ReEstimated - Data is for the budget year when the file is submitted to the DOM on April 15. Budget - Budget year or upcoming year when the file is submitted to the DOM on April 15.
			* aea: Area Education Agency Number.
			* dist: Department of Management District Number.
			* de_dist: Department of Education District Number.
			* district_name: School District Name.
			* column_name: Original Column Name of Data.
			* fund: School District Fund.
			* source: Source of Expenditure.
			* expenditures_per_pupil: Expenditures divided by the budget enrollment for the fiscal year.
			* amount: Amount of Expenditure.
			* enrollment_category: Enrollment Category based on district budget enrollment for the fiscal year.
			* enrollment_category_number: Enrollment category number. One equals lowest enrollment, Six is the highest enrollment.

			[More info here.](https://data.iowa.gov/School-Finance/Iowa-School-District-Expenditures-by-Fiscal-Year/uutu-bzs3)
			""")

with st.sidebar.expander('Table Reference: iowa_district_graduations', expanded=False):
	st.write("""
			This dataset provides the 4-Year graduation rates in Iowa by cohort (represented by graduating class) and 
			public school district starting with the Class of 2009. A cohort in the graduation rate calculation starts 
			with a group of students entering ninth grade for the first time. The cohort is adjusted to add students that 
			transfer in and subtract students that transfer out during a four year time period for calculating a graduation rate.

			* graduating_class: Year the class is expected to graduate.
			* fall_freshman_year: The year the cohort entered their freshman year of high school.
			* district: ID given by the Department of Education for the school district.
			* district_name: Name of the school district. Name of a school district associated with a district number may change over time due to school consolidations.
			* graduates: First time freshman in year indicated in fall freshman year and transfers into the cohort in grades 9 to 12 who graduated in year indicated in graduating class or earlier. SCS (small cell size) indicates data was redacted to ensure privacy standards where met.
			* total_cohort: First time freshman in year indicated in fall freshman year and transfers into the cohort in grades 9 to 12 less those who transferred out (including deceased). SCS (small cell size) indicates data was redacted to ensure privacy standards where met.
			* graduation_rate: Graduates divided by Total Cohort multiplied by 100. SCS (small cell size) indicates data was redacted to ensure privacy standards where met.
			* graduation_rate_category: Range of graduation rates created to form categories for summary purposes.

			[More info here.](https://data.iowa.gov/Primary-Secondary-Ed/4-Year-Graduation-Rates-in-Iowa-by-Cohort-and-Publ/tqti-3w6t)
			""")


q = st.text_area("Enter SQL Query here.", height = 300, placeholder='SELECT * \nFROM iowa_district_expenditures\n LIMIT 10')


if st.button('Execute SQL Query'):
	st.write(f'Query executed: {q}')
	st.write(f'Fetching results...')
	st.write(sqldf(q, locals()))