import streamlit as st
from prediction_helper import predict

st.title("Laxmi Finance: Credit Risk Modelling")


st.sidebar.title("Credit Risk Guide")

st.sidebar.markdown("""
### Applicant Details

**Age**
- Age of loan applicant.
- Helps estimate financial stability.

**Income**
- Annual income of applicant.
- Higher income improves repayment ability.

---

### Loan Information

**Loan Amount**
- Total requested loan amount.

**Loan Tenure**
- Time allowed to repay loan (months).

**Loan to Income Ratio**
- Loan Amount ÷ Income.
- Higher ratio means higher repayment burden.

---

### Credit Behaviour

**Avg DPD (Days Past Due)**
- Average delay in past loan payments.
- Higher value indicates risky behaviour.

**Delinquency Ratio**
- Percentage of delayed or missed payments.

**Credit Utilization Ratio**
- Credit used compared to available credit limit.
- Above 70% indicates financial stress.

**Open Loan Accounts**
- Number of currently active loans.

---

### Residence Information

**Residence Type**
- Owned → Lower risk  
- Rented → Moderate risk  
- Mortgage → Existing liability

---

### Loan Details

**Loan Purpose**
- Education
- Home
- Auto
- Personal

Different purposes carry different risk levels.

**Loan Type**
- Secured → Backed by collateral.
- Unsecured → Higher default probability.

---

### Model Output

**Default Probability**
- Chance of loan default (0–1).

**Credit Score**
- Range: 300 – 900.
- Higher score = safer borrower.

**Rating**
- Poor
- Average
- Good
- Excellent
""")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100,step=1)
with row1[1]:
    income = st.number_input("Income", min_value=0, max_value=1200000)
with row1[2]:
    loan_amount = st.number_input("Loan Amount", min_value=0, max_value=2560000)

loan_to_income_ratio = loan_amount/income if income > 0 else 0
with row2[0]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")

with row2[1]:
    loan_tenure_months = st.number_input("Loan Tenure (Months)", min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_deliquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquent_ratio = st.number_input("Delinquent Ratio", min_value=0, max_value=100,step=1,value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio", min_value=0, max_value=100,step=1,value=30)
with row3[2]:
    num_open_accounts = st.number_input("Open Loan Accounts", min_value=1, max_value=4,step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned','Rented','Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education','Home','Auto','Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured','Secured'])

# if st.button("Calculate Risk"):
#     probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_deliquency,
#                                                 delinquent_ratio, credit_utilization_ratio, num_open_accounts,
#                                                 residence_type,loan_purpose, loan_type)
#
#     st.write(f"Default Probability: {probability:.2f}")
#     st.write(f"Credit Score: {credit_score}")
#     st.write(f"Rating: {rating}")

calculate = st.button("Calculate Risk")

if calculate:

    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_deliquency,
        delinquent_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    st.success("Prediction Updated ✅")

    st.write(f"Default Probability: {probability:.2f}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")

