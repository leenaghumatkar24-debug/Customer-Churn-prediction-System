import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title = "Prediction Result",
    page_icon = "📊",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

st.markdown("""
            <style>
            /* Hide Streamlit top bar */
            [data-testid="stHeader"] {
                display: none;
            }

            /* Hide sidebar */
            [data-testid="stSidebar"] {
                display: none;
            }
            </style>
            """,unsafe_allow_html = True)

model = joblib.load("model\\churn_model.pkl")

feature_columns = joblib.load("model\\feature_columns.pkl")

if "customer" not in st.session_state:
    st.warning("No customer information Input")
    if st.button("Go to Customer Input"):
        st.switch_page("pages/customer_input.py")
    st.stop()

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
            .header{
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
                border : 1px solid rgba(169,154,255,0.30);
                border-radius : 12px;
                box-shadow : 
                0 10px 35px rgba(0,0,0,0.30),
                0 0 25px rgba(90,60,255,0.12);
            }
            .header h1{
                color : #F5F2FF;
                font-family : Georgia, serif;
                font-size : 60px;
                letter-spacing : 4px;
                margin : 0;
                text-shadow : 
                0 0 12px rgba(169,154,255,0.45),
                0 0 28 rgba(70,45,255,0.30);
            }
            .result-card{
                height : 100px;
                background : 
                linear-gradient(
                    135deg,
                    #24104F,
                    #38206B,
                    #2A175A
                );
                text-align : center;
                border-radius : 12px;
                border : 1px solid rgba(169,154,255,0.45);
                box-shadow : 
                0 10px 35px rgba(0,0,0,0.30),
                0 0 30px rgba(90,60,255,0.20);
                margin-bottom : 30px;
            }
            .result-card h1{
                color : #F5F2FF;
                font-family : Georgia, serif;
                font-size : 40px;
                letter-spacing : 2px;
                margin :0;
                text-shadow : 
                0 0 12px rgba(169,154,255,0.50),
                0 0 25px rgba(90,60,255,0.35);             
            }
            .metric-card{
                background : 
                linear-gradient(
                    135deg,
                    #30205C,
                    #44317A
                    );
                padding : 25px;
                text-align : center;
                margin-bottom : 20px;
                border-radius : 10px;
                border : 1px solid rgba(169,154,255,0.35);
                box-shadow : 
                0 8px 25px rgba(0,0,0,0.20),
                0 0 18px rgba(90,60,255,0.12);
                margin-bottom : 20px;
            }
            .metric-card h3{
                color : #D8D0FF;
                font-family : Georgia, serif;
                font-size : 25px;
                margin : 0 0 10px 0;
            }
            .metric-card h1{
                color : #F5F2FF;
                font-size : 30px;
                margin : 0;
                text-shadow : 
                0 0 12px rgba(169,154,255,0.35);
            }
            .recommendation{
                background : 
                linear-gradient(
                    135deg,
                    rgba(255,255,255,0.90),
                    rgba(238,232,255,0.95)
                    );
                color : #24104F;
                padding : 30px;
                margin-top : 30px;
                border-radius : 12px;
                border-left : 5px solid #704DFF;
                box-shodow : 
                0 8px 25px rgba(40,20,80,0.15),
                0 0 20px rgba(90,60,255,0.10);
            }
            .recommendation h2{
                font-family : Georgia, serif;
                color : #38306B;
                margin-top : 0;
                margin-bottom : 12px;
                font-size: 27px;
            }
            .recommendation p{
                color : #403858;
                font-size : 17px;
                line-height : 1.6;
                margin-bottom : 0;
            }
            .retention-confidence{
                color : #24104F;
                font-size : 18px;
                font-weight : 600;
                letter-spacing : 0.5px;
                margin-top : 10px 0;
            }
            .stButton > button{
                width : 320px;
                height : 58px;
                background : 
                linear-gradient(
                    135deg,
                    #6C4DFF,
                    #4B2E83
                    );
                color : white;
                border : 1px solid #9B7CFF;
                border-radius : 10px;
                font-size : 16px;
                font-weight : bold;
                letter-spacing : 1.5px;
                box-shadow : 
                0 8px 25px rgba(90,60,255,0.30);
                transition : 0.3s;
            }
            .stbutton >button:hover{
                background : 
                linear-gradient(
                    135deg,
                    #805FFF,
                    #5B3A9E
                    );
                color : white;
                border : 1px solid #B9A4FF;
                box-shadow : 
                0 10px 30px rgba(90,60,255,0.45);
                transform : translateY(-2px);
            }
            </style>
            """,unsafe_allow_html = True)

st.markdown("""
            <div class = "header">
            <h1>Prediction Result</h1>
            </div>
            """,unsafe_allow_html = True)

customer_data = st.session_state.customer
customer = pd.DataFrame([customer_data])
customer = pd.get_dummies(customer)
customer = customer.reindex(
    columns = feature_columns,
    fill_value = 0
)

prediction = model.predict(customer)[0]

if hasattr(model, "predict_proba"):
    probalility = model.predict_proba(customer)[0]
    churn_probability = probalility[1] * 100
    retention_probability = probalility[0] * 100
    confidence = max(churn_probability, retention_probability)
    
else:
    churn_probability = None
    retention_probability = None
    confidence = None
    
if prediction == 0:
    result = "CUSTOMER LIKELY TO STAY"
    recommendation = """
    The customer shows a lower probability of churn.
    Maintain the current customer experience and consider
    loyalty benefits or personalised offers to strengthen
    the relationship.    
    """
else:
    result = "CUSTOMER LIKELY TO CHURN"
    recommendation = """
    The customer shows a higher probability of churn.
    Consider personalised offers, improved customer support,
    and a targeted retention campaign.    
    """

st.markdown(f"""
            <div class = "result-card">
            <h1>{result}</h1>
            </div>
            """,unsafe_allow_html = True)

col1,col2,col3 = st.columns(3)

with col1:
    if retention_probability is not None:
        st.markdown(f"""
                    <div class = "metric-card">
                    <h3>Retention Probability</h3>
                    <h1>{retention_probability:.1f}</h1>
                    </div>
                    """,unsafe_allow_html = True)

with col2:
    if churn_probability is not None:
        st.markdown(f"""
                    <div class = "metric-card">
                    <h3>Churn Probability</h3>
                    <h1>{churn_probability:.1f}%</h1>
                    </div>
                    """,unsafe_allow_html = True)
        
with col3:
    st.markdown(f"""
                <div class = "metric-card">
                <h3>Retention Confidence</h3>
                <h1>{confidence:.1f}%</h1>
                </div>
                """,unsafe_allow_html = True)

if churn_probability is not None:
    if churn_probability < 30:
        risk = "LOW RISK"
    elif churn_probability < 60:
        risk = "MEDIUM RISK"
    else:
        risk = "HIGH RISK"
    st.markdown(f"""
                <div class = "metric-card">
                <h3>Customer Risk Level</h3>
                <h1>{risk}</h1>
                </div>
                """,unsafe_allow_html = True)
        
if retention_probability is not None:
    st.markdown(f'<div class = "retention-confidence">Retention Confidence</div>',
                unsafe_allow_html =True)
    st.progress(int(retention_probability))
    st.markdown(f'<div class = "retention-confidence">{retention_probability:.1f}%</div>',
                unsafe_allow_html =True)

st.markdown(f"""
            <div class = "recommendation">
            <h2>💡 Recommended Action</h2>
            <p>{recommendation}</p>
            </div>
            """,unsafe_allow_html = True)

with st.expander("View Customer Information"):
    st.dataframe(
        customer,
        use_container_width = True
    )
    
st.markdown("<br>",unsafe_allow_html = True)

if st.button("← Go To Another Customer"):
    st.session_state.pop("customer",None)
    st.switch_page("pages/customer_input.py")