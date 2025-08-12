import streamlit as st

# Title
st.title("Equity Valuation Comparison Tool")

# Sidebar inputs
st.sidebar.header("Input Parameters")

# Case study toggle
use_case_study = st.sidebar.checkbox("Load TechNova Case Study")

# Default or case study values
if use_case_study:
    st.subheader("📘 TechNova Inc. Case Study Notes")
    st.markdown("""
    TechNova Inc. is a mid-sized technology firm with stable growth and moderate debt. This case study allows students to compare equity valuation models using realistic financial data.
    """)
    
    # Input values for TechNova
    dividend = 2.50
    dividend_growth = 0.05
    cost_of_equity = 0.09
    fcfe = 1500000
    fcfe_growth = 0.04
    shares_outstanding = 500000
    fcff = 2200000
    fcff_growth = 0.04
    wacc = 0.08
    debt = 3000000
    cash = 500000
else:
    dividend = st.sidebar.number_input("Next Year's Dividend (D₁)", value=2.50)
    dividend_growth = st.sidebar.number_input("Dividend Growth Rate (g)", value=0.05)
    cost_of_equity = st.sidebar.number_input("Cost of Equity (k)", value=0.09)
    fcfe = st.sidebar.number_input("Next Year's FCFE", value=1500000.0)
    fcfe_growth = st.sidebar.number_input("FCFE Growth Rate", value=0.04)
    shares_outstanding = st.sidebar.number_input("Shares Outstanding", value=500000)
    fcff = st.sidebar.number_input("Next Year's FCFF", value=2200000.0)
    fcff_growth = st.sidebar.number_input("FCFF Growth Rate", value=0.04)
    wacc = st.sidebar.number_input("WACC", value=0.08)
    debt = st.sidebar.number_input("Total Debt", value=3000000.0)
    cash = st.sidebar.number_input("Cash & Equivalents", value=500000.0)

# Valuation calculations
ddm_value = dividend / (cost_of_equity - dividend_growth)
fcfe_value = (fcfe * (1 + fcfe_growth)) / (cost_of_equity - fcfe_growth)
fcff_value = ((fcff * (1 + fcff_growth)) / (wacc - fcff_growth) - debt + cash) / shares_outstanding

# Display results
st.subheader("📈 Valuation Results")
st.write(f"**Dividend Discount Model (DDM) Value per Share:** ${ddm_value:.2f}")
st.write(f"**Free Cash Flow to Equity (FCFE) Value per Share:** ${fcfe_value / shares_outstanding:.2f}")
st.write(f"**Free Cash Flow to the Firm (FCFF) Value per Share:** ${fcff_value:.2f}")

# Summary of input data
st.subheader("📊 Summary of Input Data")
st.markdown(f"""
- **Dividend (D₁):** ${dividend}
- **Dividend Growth Rate (g):** {dividend_growth * 100:.2f}%
- **Cost of Equity (k):** {cost_of_equity * 100:.2f}%
- **FCFE:** ${fcfe}
- **FCFE Growth Rate:** {fcfe_growth * 100:.2f}%
- **FCFF:** ${fcff}
- **FCFF Growth Rate:** {fcff_growth * 100:.2f}%
- **WACC:** {wacc * 100:.2f}%
- **Debt:** ${debt}
- **Cash & Equivalents:** ${cash}
- **Shares Outstanding:** {shares_outstanding}
""")

# Discussion questions
st.subheader("🧠 Questions and Potential Responses")
st.markdown("""
**1. Which model produced the highest value and why?**  
*Sample Response:* The FCFF model may produce a higher value if the firm has significant debt and cash reserves, as it values the entire enterprise.

**2. How do growth and discount rate assumptions affect outcomes?**  
*Sample Response:* Higher growth rates increase valuation, while higher discount rates reduce it. Small changes in these inputs can lead to large differences in estimated value.

**3. What impact would increased debt have on FCFF vs. FCFE?**  
*Sample Response:* Increased debt reduces FCFE due to higher interest and repayments, but may not affect FCFF directly unless it changes operating cash flows or WACC.
""")

# Valuation formulas
st.subheader("📐 Valuation Formulas Used")
st.markdown(r"""
**Dividend Discount Model (DDM):**  
$V = \frac{D_1}{k - g}$

**Free Cash Flow to Equity (FCFE):**  
$V = \frac{FCFE \times (1 + g)}{k - g}$

**Free Cash Flow to the Firm (FCFF):**  
$V = \frac{FCFF \times (1 + g)}{WACC - g}$  
**Equity Value per Share:**  
$V_{equity} = \frac{Firm\ Value - Debt + Cash}{Shares\ Outstanding}$
""")

