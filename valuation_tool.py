
import streamlit as st

st.title("Equity Valuation Comparison Tool")

st.sidebar.header("Input Parameters")

# Dividend Discount Model (DDM) Inputs
st.sidebar.subheader("DDM Inputs")
dividend = st.sidebar.number_input("Next Year's Dividend (D1)", value=2.0)
ddm_growth = st.sidebar.number_input("Growth Rate (g) for DDM (%)", value=5.0) / 100
cost_of_equity = st.sidebar.number_input("Cost of Equity (k) (%)", value=10.0) / 100

# Free Cash Flow to Equity (FCFE) Inputs
st.sidebar.subheader("FCFE Inputs")
fcfe = st.sidebar.number_input("Next Year's FCFE", value=5.0)
fcfe_growth = st.sidebar.number_input("Growth Rate (g) for FCFE (%)", value=4.0) / 100

# Free Cash Flow to the Firm (FCFF) Inputs
st.sidebar.subheader("FCFF Inputs")
fcff = st.sidebar.number_input("Next Year's FCFF", value=10.0)
wacc = st.sidebar.number_input("WACC (%)", value=8.0) / 100
debt = st.sidebar.number_input("Total Debt", value=50.0)
cash = st.sidebar.number_input("Cash & Cash Equivalents", value=20.0)
shares_outstanding = st.sidebar.number_input("Shares Outstanding", value=10.0)

st.header("Valuation Results")

# DDM Valuation
try:
    ddm_value = dividend / (cost_of_equity - ddm_growth)
    st.subheader("Dividend Discount Model (DDM)")
    st.write(f"Value per Share: ${ddm_value:.2f}")
except ZeroDivisionError:
    st.error("DDM calculation error: cost of equity must be greater than growth rate.")

# FCFE Valuation
try:
    fcfe_value = fcfe / (cost_of_equity - fcfe_growth)
    st.subheader("Free Cash Flow to Equity (FCFE)")
    st.write(f"Value per Share: ${fcfe_value:.2f}")
except ZeroDivisionError:
    st.error("FCFE calculation error: cost of equity must be greater than growth rate.")

# FCFF Valuation
try:
    firm_value = fcff / wacc
    equity_value = firm_value - debt + cash
    fcff_value_per_share = equity_value / shares_outstanding
    st.subheader("Free Cash Flow to the Firm (FCFF)")
    st.write(f"Value per Share: ${fcff_value_per_share:.2f}")
except ZeroDivisionError:
    st.error("FCFF calculation error: WACC and shares outstanding must be greater than zero.")
