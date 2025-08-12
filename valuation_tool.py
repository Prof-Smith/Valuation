import streamlit as st

# Title
st.title("Equity Valuation Comparison Tool")

# Sidebar inputs
st.sidebar.header("Input Financial Data")

# Case study autofill
use_case_study = st.sidebar.checkbox("Load TechNova Case Study")

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
def ddm_value(D1, g, k):
    return D1 / (k - g)

def fcfe_value(fcfe, g, k, shares):
    return (fcfe * (1 + g)) / (k - g) / shares

def fcff_value(fcff, g, wacc, debt, cash, shares):
    firm_value = (fcff * (1 + g)) / (wacc - g)
    equity_value = firm_value - debt + cash
    return equity_value / shares

# Display results
st.subheader("Valuation Results")
st.write(f"**Dividend Discount Model (DDM) Value per Share:** ${ddm_value(dividend, dividend_growth, cost_of_equity):.2f}")
st.write(f"**Free Cash Flow to Equity (FCFE) Value per Share:** ${fcfe_value(fcfe, fcfe_growth, cost_of_equity, shares_outstanding):.2f}")
st.write(f"**Free Cash Flow to the Firm (FCFF) Value per Share:** ${fcff_value(fcff, fcff_growth, wacc, debt, cash, shares_outstanding):.2f}")

# Case Study Notes
st.subheader("TechNova Inc. Case Study Notes")
st.markdown("""
TechNova Inc. is a mid-sized technology firm with stable growth and moderate debt. This case provides students with the opportunity to apply three equity valuation models using realistic financial data. Students are encouraged to compare the outcomes and reflect on the assumptions and implications of each model.
""")

# Questions and Potential Responses
st.subheader("Questions and Potential Responses")

st.markdown("""
**1. Which valuation model produced the highest value per share for TechNova Inc., and why might that be the case?**  
*Sample Response:* The FCFF model produced the highest value per share because it considers the entire firm value before adjusting for debt and cash. This broader scope often results in a higher valuation compared to models focused solely on equity cash flows.

**2. How do the assumptions about growth rates and discount rates influence the valuation outcomes?**  
*Sample Response:* Higher growth rates increase the numerator in each model, leading to higher valuations. Lower discount rates reduce the denominator, also increasing valuations. These assumptions are critical and must reflect realistic expectations for the firm and market.

**3. If TechNova were to increase its debt significantly, how would that affect the FCFF valuation compared to the FCFE valuation?**  
*Sample Response:* Increasing debt would reduce the equity value in the FCFF model after subtracting liabilities, potentially lowering the per-share value. In the FCFE model, higher debt repayments would reduce free cash flow to equity, also lowering the valuation. However, the impact may differ based on how debt affects growth and risk.
""")





