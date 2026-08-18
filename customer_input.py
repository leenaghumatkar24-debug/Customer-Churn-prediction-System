import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Customer Input",
    page_icon = "📊",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

df = pd.read_csv("Telco_Customer_Churn.csv")
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors = "coerce"
)
df = df.dropna()

st.markdown("""
            <style>
            .stApp{
                background: 
                    radial-gradient(
                        ellipse at 10% 10%,
                        rgba(120,80,255,0.22),
                        transparent 30%
                    ),
                    radial-gradient(
                        ellipse at 90% 20%,
                        rgba(150,100,255,0.18),
                        transparent 32%
                    ),                 
                    radial-gradient(
                        ellipse at 50% 90%,
                        rgba(70,90,200,0.18),
                        transparent 35%
                    ),
                #F4F0FF;
            }
            .block-container{
                padding-top : 2rem;
            }
            .title{
                background : 
                linear-gradient(
                    135deg,
                    rgba(35,0,55,0.90),
                    rgba(25,10,70,0.88),
                    rgba(15,20,65,0.90)
                    );
                padding : 40px;
                text-align : center;
                margin-bottom : 35px;
                border : 1px solid rgba(169,154,255,0.030);
                border-radius : 12px;
                box-shadow :
                0 10px 35px rgba(169,154,255,0.30);
                border-radius : 12px;
                box-shadow : 0 10px 35px rgba(0,0,0,0.30),
                0 0 25px rgba(90,60,255,0.12);
            }
            .title h1{
                color : #F5F2FF;
                font-family : Georgia, serif;
                font-size : 65px;
                letter-spacing : 5px;
                margin : 0;
                text-shadow : 
                0 0 12px rgba(169,154,255,0.45),
                0 0 28px rgba(70,45,255,0.30);
            }
            .title p{
                color : #C9FFD9;
                letter-spacing : 1px;
                margin-top : 12px;
                font-size : 17px;
                text-shadow : 
                0 0 10px rgba(201,255,217,0.25);
            }
            .section{
                background : 
                linear-gradient(
                    135deg,
                    rgba(35,0,55,0.88),
                    rgba(25,10,70,0.85)
                    );
                color : #F5F2FF;
                padding : 16px 25px;
                margin-top : 30px;
                margin-bottom : 20px;
                border-left : 4px solid #704DFF;
                border-radius : 8px;
                box-shadow : 
                0 6px 20px rgba(0,0,0,0.25),
                0 0 18px rgba(90,60,255,0.12);
            }
            .section h2{
                font-family : Georgia,  serif;
                margin : 0;
                color : #D8D0FF;
                font-size : 24px;
                letter-spacing : 1px;
                text-shadow :
                0 0 10px rgba(139,124,255,0.3);
            }
            label{
                color : #002349 !important;
                font-weight : 600 !important;
            }
            .stButton > button{
                width : 100%;
                height : 50px;
                background : linear-gradient(135deg, #6C4DFF, #4B2E83);
                color : white;
                border : 1px solid #9B7CFF;
                border-radius : 0px;
                font-size : 17px;
                font-weight : bold;
                letter-spacing : 1.5px;
                box-shadow : 0 8px 25px rgba(90,60,255,0.30);
                transition : 0.3s;
            }
            div.stButton{
                display : flex;
                justify-content : center;
                margin-top : 25px;
                margin-bottom : 40px;
            }
            .stButton >button:hover{
                background : linear-gradient(135deg, #805FFF, #5B3A9E);
                color : white;
                border : 1px solid #B9A4FF;
                box-shadow :0 10px 30px rgba(90,60,255,0.45);
                transform : translateY(-2px);
            }
            </style>
            """,unsafe_allow_html = True)

st.markdown("""
            <div class = "title">
            <h1>Customer Information</h1>
            <p>Enter the customer's information to generate a retention prediction.</p>
            </div>
            """,unsafe_allow_html = True)

st.markdown("""
            <div class = "section">
            <h2>👤 Personal Information</h2>
            </div>
            """,unsafe_allow_html = True)

col1,col2,col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        df["gender"].unique()
    )
    
with col2:
    senior = st.selectbox(
        "Senior Citizen",
        [0,1],
        format_func = lambda x:
        "Yes" if x == 1 else "No"
    )
    
with col3:
    partner = st.selectbox(
        "Partner",
        df["Partner"].unique()
    )
    
col1,col2 = st.columns(2)

with col1:
    dependents = st.selectbox(
        "Dependents",
        df["Dependents"].unique()
    )
    
with col2:
    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )


st.markdown("""
            <div class = "section">
            <h2>📡 Services</h2>
            </div>
            """,unsafe_allow_html = True)
 
col1,col2,col3 = st.columns(3)

with col1:
    phone = st.selectbox(
        "Phone Service",
        df["PhoneService"].unique()
    )
    multiple_lines = st.selectbox(
        "Multiple Lines",
        df["MultipleLines"].unique()
    )
    internet = st.selectbox(
        "Internet Service",
        df["InternetService"].unique()
    )

with col2:
    security = st.selectbox(
        "Online Security",
        df["OnlineBackup"].unique()
    )
    backup = st.selectbox(
        "Online Backup",
        df["OnlineSecurity"].unique()
    )
    device = st.selectbox(
        "Device Protection",
        df["DeviceProtection"].unique()
    )
    
with col3:
    support = st.selectbox(
        "Tech Support",
        df["TechSupport"].unique()
    )
    streaming_tv = st.selectbox(
        "Streaming TV",
        df["StreamingTV"].unique()
    )
    streaming_movies = st.selectbox(
        "Streaming Movies",
        df["StreamingMovies"].unique()
    )
    
st.markdown("""
            <div class = "section">
            <h2>💳 Subscription & Billing</h2>
            </div>
            """,unsafe_allow_html = True)

col1,col2,col3 = st.columns(3)

with col1:
    contract = st.selectbox(
        "Contract",
        df["Contract"].unique()
    )
    
with col2:
    paperless = st.selectbox(
        "Paperless Billing",
        df["PaperlessBilling"].unique()
    )
    
with col3:
    payment = st.selectbox(
        "Payment Method",
        df["PaymentMethod"].unique()
    )
    
st.markdown("""
            <div class = "section">
            <h2>💰 Charges</h2>
            </div>
            """,unsafe_allow_html = True)

col1,col2 = st.columns(2)

with col1:
    monthly = st.number_input(
        "Monthly Charges",
        min_value = 0.0,
        value = 70.0,
        step = 5.0
    )
    
with col2:
    total = st.number_input(
        "Total Charges",
        min_value = 0.0,
        value = monthly * tenure,
        step = 100.0
    )
    
customer_data = {
    "gender" : gender,
    "SeniorCitizen" : senior,
    "Partner" : partner,
    "Dependents" : dependents,
    "tenure" : tenure,
    "PhoneService" : phone,
    "MultipleLines" : multiple_lines,
    "InternetService" : internet,
    "OnlineSecurity" : security,
    "OnlineBackup" : backup,
    "DeviceProtection" : device,
    "TechSupport" : support,
    "StreamingTV" : streaming_tv,
    "StreamingMovies" : streaming_movies,
    "Contract" : contract,
    "PaperlessBilling" : paperless,
    "PaymentMethod" : payment,
    "MonthlyCharges" : monthly,
    "TotalCharges" : total
}

st.markdown("<br>",unsafe_allow_html = True)

if st.button("PREDICT CUSTOMER RETENTION"):
    st.session_state.customer = customer_data
    st.switch_page("pages/result.py")