import streamlit as st
from fpdf import FPDF
import base64

# --- CALCULATOR LOGIC ---
def calculate_compliance(income, expense):
    actual_margin = ((income - expense) / expense) * 100
    target_margin = 15.5
    if actual_margin >= target_margin:
        return "SAFE", round(actual_margin, 2), 0
    else:
        required_income = expense * (1 + (target_margin / 100))
        adjustment = required_income - income
        return "AT RISK", round(actual_margin, 2), round(adjustment, 2)

# --- PDF GENERATOR ---
def create_pdf(name, income, expense, margin, status, adjustment):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "2026 SAFE HARBOUR READINESS REPORT", 0, 1, 'C')
    pdf.ln(10)
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Company Name: {name}", 0, 1)
    pdf.cell(0, 10, f"Operating Income: INR {income:,.2f}", 0, 1)
    pdf.cell(0, 10, f"Operating Expense: INR {expense:,.2f}", 0, 1)
    pdf.cell(0, 10, f"Calculated Margin: {margin}%", 0, 1)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Compliance Status: {status}", 0, 1)
    
    if status == "AT RISK":
        pdf.set_text_color(255, 0, 0)
        pdf.multi_cell(0, 10, f"ADJUSTMENT REQUIRED: You must declare an additional INR {adjustment:,.2f} in profit to meet the 15.5% Safe Harbour threshold.")
    
    return pdf.output(dest='S').encode('latin-1')

# --- STREAMLIT UI ---
st.set_page_config(page_title="SafeHarbour26", page_icon="🛡️")

st.title("🛡️ Safe Harbour 2026 Compliance Checker")
st.markdown("Assess your IT/ITeS export compliance against the latest **15.5% Margin** rules.")

with st.form("calc_form"):
    company_name = st.text_input("Company Name")
    income = st.number_input("Total Operating Income (INR)", min_value=0.0)
    expense = st.number_input("Total Operating Expense (INR)", min_value=1.0)
    submitted = st.form_submit_button("Analyze Risk")

if submitted:
    status, margin, adjustment = calculate_compliance(income, expense)
    
    st.divider()
    
    # Display the "Bait" - The current status
    if status == "SAFE":
        st.success(f"ANALYSIS COMPLETE: Your margin is {margin}%. You appear to be COMPLIANT.")
        st.info("You may still want the full report for your 2026 documentation.")
    else:
        st.error(f"ANALYSIS COMPLETE: Your margin is {margin}%. Status: AT RISK.")
        st.warning("You are below the 15.5% Safe Harbour threshold for FY 2026.")

    # The Paywall Section
    st.subheader("🔓 Unlock Your Compliance Action Plan")
    st.write("""
    To avoid a Transfer Pricing Audit, you need to calculate your **Secondary Adjustment**. 
    Our certified report provides:
    1. The exact INR amount to increase your declared profit.
    2. The specific Clause 92CB reference for your CA.
    3. An audit-ready PDF document.
    """)
    
    # Button to your Razorpay Payment Link
    # REPLACE the URL below with your actual Razorpay Payment Link URL later
    payment_link = "https://rzp.io/l/your_link_here" 
    
    # Corrected Button Code
    # The Paywall Section
    st.subheader("🔓 Unlock Your Compliance Action Plan")
    st.write("""
    To avoid a Transfer Pricing Audit, you need to calculate your **Secondary Adjustment**. 
    Our certified report provides:
    1. The exact INR amount to increase your declared profit.
    2. The specific Clause 92CB reference for your CA.
    3. An audit-ready PDF document.
    """)
    
    # Replace the old st.markdown block with this:
    st.link_button(
        label="Pay ₹1,999 to Download Certified Report",
        url="https://rzp.io/l/your_link_here",  # Replace with your actual Razorpay link
        type="primary",
        use_container_width=True
    )