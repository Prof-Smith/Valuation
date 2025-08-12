import streamlit as st

# Title
st.title("Equity Valuation Tool")

# Sidebar inputs
st.sidebar.header("Input Financial Data")

# Case study loader
use_case = st.sidebar.checkbox("Load TechNova Case Study")

if use_case:
    # Pre-filled data for TechNova Inc.
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
    # Manual input
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
    st.write("DDM calculation error: Check that cost of equity > dividend growth.")

# FCFE
try:
    fcfe_value = (fcfe * (1 + fcfe_growth)) / (cost_of_equity - fcfe_growth)
    fcfe_per_share = fcfe_value / shares_outstanding
    st.subheader("Free Cash Flow to Equity (FCFE)")
    st.write(f"Estimated Value per Share: ${fcfe_per_share:.2f}")
except ZeroDivisionError:
    st.write("FCFE calculation error: Check that cost of equity > FCFE growth.")

# FCFF
try:
    fcff_value = (fcff * (1 + fcff_growth)) / (wacc - fcff_growth)
    equity_value = fcff_value - debt + cash
    fcff_per_share = equity_value / shares_outstanding
    st.subheader("Free Cash Flow to the Firm (FCFF)")
    st.write(f"Estimated Value per Share: ${fcff_per_share:.2f}")
except ZeroDivisionError:
    st.write("FCFF calculation error: Check that WACC > FCFF growth.")

# Case Study Notes
st.header("TechNova Inc. Case Study Notes")
st.markdown("""
TechNova Inc. is a mid-sized technology firm with stable growth and moderate debt. This case allows students to apply three valuation models using realistic financial data. Each model uses different assumptions and discount rates, offering insights into how valuation outcomes vary.
""")

# Discussion Questions
st.header("Discussion Questions and Potential Responses")
st.markdown("""
**1. Which model produced the highest value and why?**  
*Response:* The FCFF model may produce a higher value if the firm has significant debt and cash reserves, as it values the entire enterprise.

**2. How do growth and discount rate assumptions affect outcomes?**  
*Response:* Higher growth rates increase valuation, while higher discount rates reduce it. The sensitivity to these inputs varies by model.

**3. What impact would increased debt have on FCFF vs. FCFE?**  
*Response:* Increased debt reduces FCFE (as more cash goes to debt service) but may not affect FCFF directly. It also affects equity value derived from FCFF.
""")

# Valuation Formulas
st.header("Valuation Formulas Used")
st.markdown("""
**Dividend Discount Model (DDM):**  
\\[
Value per Share = D_1/{k - g}
\\]  
Where \\( D_1 \\) is next year's dividend, \\( k \\) is the cost of equity, and \\( g \\) is the dividend growth rate.

**Free Cash Flow to Equity (FCFE):**  
\\[
Value per Share = [FCFE * (1 + g)/{k - g}] / Shares Outstanding
\\]  
Where \\( FCFE \\) is next year's free cash flow to equity, \\( g \\) is its growth rate, and \\( k \\) is the cost of equity.

**Free Cash Flow to the Firm (FCFF):**  
\\[
Equity Value = [(FCFF * (1 + g)) / {WACC - g}] - [Debt + Cash]
\\]  
\\[
\\Value per Share = Equity Value / Shares Outstanding
\\]  
Where \\( FCFF \\) is next year's free cash flow to the firm, \\( g \\) is its growth rate, and \\( WACC \\) is the weighted average cost of capital.
""")

