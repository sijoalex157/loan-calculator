import streamlit as st
import pandas as pd
import numpy as np

def calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_years):
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Calculate total number of payments
    total_payments = loan_term_years * 12
    
    # Calculate monthly payment using formula for fixed monthly payments
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**-total_payments)
    
    # Generate loan schedule
    schedule = []
    remaining_balance = loan_amount
    for i in range(total_payments):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        schedule.append([i+1, interest_payment, principal_payment, remaining_balance])
    
    return pd.DataFrame(schedule, columns=["Month", "Interest Payment (INR)", "Principal Payment (INR)", "Remaining Balance (INR)"])

# Streamlit UI
st.title("Loan Schedule Calculator")

# User input
loan_amount = st.number_input("Loan Amount (INR)", min_value=1, step=1)
annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.01, step=0.01)
loan_term_years = st.number_input("Loan Term (Years)", min_value=1, step=1)

# Calculate and display loan schedule
if st.button("Calculate Loan Schedule"):
    schedule_df = calculate_loan_schedule(loan_amount, annual_interest_rate, loan_term_years)
    st.write(schedule_df)
