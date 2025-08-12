import streamlit as st

# Function to calculate DDM value per share
def calculate_ddm(dividend, growth_rate, cost_of_equity):
    try:
        value = dividend / (cost_of_equity - growth_rate)
        return round(value, 2)
    except ZeroDivisionError:
        return "Invalid inputs"

# Function to calculate FCFE value per share
def calculate_fcfe(fcfe, growth_rate, cost_of_equity, shares_outstanding):
    try:
        equity_value = fcfe * (1 + growth_rate) / (cost_of_equity - growth_rate)
        value_per_share = equity_value / shares_outstanding
        return round(value_per_share, 2)
    except ZeroDivisionError:
        return "Invalid inputs"

# Function to calculate FCFF value per share
def calculate_fcff(fcff, growth_rate, wacc, debt, cash, shares_outstanding):
    try:
        firm_value = fcff * (1 + growth_rate) / (wacc - growth_rate)
        equity_value = firm_value - debt + cash
        value_per_share = equity_value / shares_outstanding
        return round(value_per_share, 2)
    except ZeroDivisionError:
        return "Invalid inputs"

# Sidebar inputs
st.sidebar.title("Valuation Inputs")

use_case_study = st.sidebar.checkbox("Load TechNova Case Study")

if use_case_study:
    st.sidebar.markdown("**TechNova Inc. Case Study Loaded**")
    dividend = 2.50
    dividend_growth = 0.045
    cost_of_equity = 0.09
    fcfe = 1500000
    fcfe_growth = 0.04
    fcff = 2200000
    fcff_growth = 0.035
    wacc = 0.08
    debt = 3000000
    cash = 500000
    shares_outstanding = 500000
else:
    dividend = st.sidebar.number_input("Next Year's Dividend (D₁)", value=2.50)
    dividend_growth = st.sidebar.number_input("Dividend Growth Rate (g)", value=0.045)
    cost_of_equity = st.sidebar.number_input("Cost of Equity (k)", value=0.09)
    fcfe = st.sidebar.number_input("Next Year's FCFE", value=1500000)
    fcfe_growth = st.sidebar.number_input("FCFE Growth Rate", value=0.04)
    fcff = st.sidebar.number_input("Next Year's FCFF", value=2200000)
    fcff_growth = st.sidebar.number_input("FCFF Growth Rate", value=0.035)
    wacc = st.sidebar.number_input("WACC", value=0.08)
    debt = st.sidebar.number_input("Total Debt", value=3000000)
    cash = st.sidebar.number_input("Cash & Equivalents", value=500000)
    shares_outstanding = st.sidebar.number_input("Shares Outstanding", value=500000)

# Main app
st.title("Equity Valuation Comparison Tool")
st.subheader("Compare DDM, FCFE, and FCFF Valuation Models")

# Calculate values
ddm_value = calculate_ddm(dividend, dividend_growth, cost_of_equity)
fcfe_value = calculate_fcfe(fcfe, fcfe_growth, cost_of_equity, shares_outstanding)
fcff_value = calculate_fcff(fcff, fcff_growth, wacc, debt, cash, shares_outstanding)

# Display results
st.markdown("### 📈 Valuation Results (Value per Share)")
st.write(f"**Dividend Discount Model (DDM):** ${ddm_value}")
st.write(f"**Free Cash Flow to Equity (FCFE):** ${fcfe_value}")
st.write(f"**Free Cash Flow to the Firm (FCFF):** ${fcff_value}")

# Discussion section
st.markdown("### 💬 Discussion")
st.markdown("""
Use the results above to reflect on the following:
- Which model gives the highest valuation and why?
- How do assumptions about growth and discount rates affect each model?
- How does the treatment of debt and cash influence the FCFF result?
- Which model do you think is most appropriate for TechNova Inc. and why?
""")

