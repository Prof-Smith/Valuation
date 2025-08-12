import streamlit as st

# Title
st.title("Equity Valuation Comparison Tool")

# Sidebar inputs
st.sidebar.header("Input Parameters")

# Case study checkbox
use_case_study = st.sidebar.checkbox("Load TechNova Case Study")

# Default values for TechNova Inc.
if use_case_study:
    dividend = 2.50
    dividend_growth = 0.045
    cost_of_equity = 0.09
    fcfe = 1500000
    fcfe_growth = 0.04
    shares_outstanding = 500000
    fcff = 2200000
    fcff_growth = 0.035
    wacc = 0.08
    debt = 3000000
    cash = 500000
else:
    dividend = st.sidebar.number_input("Next Year's Dividend (D₁)", value=2.50)
    dividend_growth = st.sidebar.number_input("Dividend Growth Rate (g)", value=0.045)
    cost_of_equity = st.sidebar.number_input("Cost of Equity (k)", value=0.09)
    fcfe = st.sidebar.number_input("Next Year's FCFE", value=1500000)
    fcfe_growth = st.sidebar.number_input("FCFE Growth Rate", value=0.04)
    shares_outstanding = st.sidebar.number_input("Shares Outstanding", value=500000)
    fcff = st.sidebar.number_input("Next Year's FCFF", value=2200000)
    fcff_growth = st.sidebar.number_input("FCFF Growth Rate", value=0.035)
    wacc = st.sidebar.number_input("WACC", value=0.08)
    debt = st.sidebar.number_input("Total Debt", value=3000000)
    cash = st.sidebar.number_input("Cash & Equivalents", value=500000)

# Valuation calculations
st.header("Valuation Results")

# DDM
try:
    ddm_value = dividend / (cost_of_equity - dividend_growth)
    st.subheader("Dividend Discount Model (DDM)")
    st.write(f"Estimated Value per Share: ${ddm_value:.2f}")
except ZeroDivisionError:
    st.write("DDM calculation error: Check that cost of equity > dividend growth rate.")

# FCFE
try:
    fcfe_value = (fcfe * (1 + fcfe_growth)) / (cost_of_equity - fcfe_growth)
    fcfe_per_share = fcfe_value / shares_outstanding
    st.subheader("Free Cash Flow to Equity (FCFE)")
    st.write(f"Estimated Value per Share: ${fcfe_per_share:.2f}")
except ZeroDivisionError:
    st.write("FCFE calculation error: Check that cost of equity > FCFE growth rate.")

# FCFF
try:
    fcff_value = (fcff * (1 + fcff_growth)) / (wacc - fcff_growth)
    equity_value = fcff_value - debt + cash
    fcff_per_share = equity_value / shares_outstanding
    st.subheader("Free Cash Flow to the Firm (FCFF)")
    st.write(f"Estimated Value per Share: ${fcff_per_share:.2f}")
except ZeroDivisionError:
    st.write("FCFF calculation error: Check that WACC > FCFF growth rate.")

# Case Study Notes
if use_case_study:
    st.header("Case Study Notes")
    st.markdown("""
    **TechNova Inc.** is a mid-sized technology firm with stable growth and moderate debt. This case study provides a practical opportunity to compare three equity valuation models:

    - **Dividend Discount Model (DDM)** estimates value based on projected dividends and growth.
    - **Free Cash Flow to Equity (FCFE)** focuses on cash flows available to shareholders after debt obligations.
    - **Free Cash Flow to the Firm (FCFF)** values the entire firm and adjusts for debt and cash to derive equity value.

    Key assumptions include dividend and cash flow forecasts, growth rates, cost of capital, and capital structure. Students are encouraged to reflect on how each model interprets firm value and how changes in assumptions affect valuation outcomes.
    """)



