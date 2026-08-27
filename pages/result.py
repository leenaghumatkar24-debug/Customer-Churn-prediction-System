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

feature_columns = joblib.load("model/feature_columns.pkl")


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
                width : 100%;
                padding : 28px 20px;
                background : 
                linear-gradient(
                    135deg,
                    #24104F,
                    #38206B,
                    #2A175A
                );
                text-align : center;
                border-radius : 16px;
                border : 1px solid rgba(169,154,255,0.45);
                box-shadow : 
                0 10px 35px rgba(0,0,0,0.25),
                0 0 30px rgba(90,60,255,0.18);
                margin-bottom : 15px;
                box-sizing : border-box;
            }
            .result-card h1.stay{
                color : #C9FFD9;
                text-shadow : 
                0 0 12px rgba(100,255,170,0.35),
                0 0 30px rgba(80,220,150,0..20);
                font-family : Georgia, serif;
            }
            .result-card h1.churn{
                color : #FFD0D8;
                text-shadow : 
                0 0 12px rgba(255,100,130,0.35),
                0 0 30px rgba(255,80,110,0.20);
                font-family : Georgia, serif;
            }
            .metric-card{
                width : 100%;
                height : 190%;
                background : 
                linear-gradient(
                    135deg,
                    #24104F,
                    #38206B,
                    #2A175A
                );
                padding : 25px 20px;
                text-align : center;
                border-radius : 12px;
                border : 1px solid rgba(169,154,255,0.45);
                box-shadow : 
                0 10px 35px rgba(0,0,0,0.25),
                0 0 30px rgba(90,60,255,0.18);
                box-sizing : border-box;
            }
            .metric-card h3{
                color : #D8D0FF;
                font-family : Georgia, serif;
                font-size : 20px;
                margin : 0 0 10px 0;
            }
            .metric-card h1{
                color : #F5F2FF;
                font-size : 36px;
                margin : 0;
                text-shadow : 
                0 0 12px rgba(169,154,255,0.35);
            }
            .confidence{
                width : 100%;
                min-height : 10px;
                display : block;
                background : linear-gradient(
                    135deg,
                    #30205C,
                    #44317A
                );
                padding : 25px;
                border-radius : 12px;
                border : 1px solid rgba(169,154,255,0.35);
                box-shadow : 
                0 8px 25px rgba(0,0,0,0.20),
                0 0 18px rgba(90,60,255,0.12);
                box-sizing : border-box;
            }
            .confidence h1{
                color : #D8D0FF;
                font-family : Gorgia, serif;
                font-size : 21px;
                font-weight : bold;
                text-align : left;
                margin : 0 0 18px 0;
            }
            .confidence p{
                color : #F5F2FF;
                font-size : 21px;
                font-family : Gorgia, serif;
                font-weight : bold;
                text-align : left;
                margin-bottom : 14px 0 0 0;
            }
            .confidence-bar{
                width : 100%;
                height : 10px;
                background : #E3DDF2;
                border-radius : 10px;
                overflow : hidden;
            }
            .confidence-fill{
                height : 100%;
                background : linear-gradient(
                    90deg,
                    #704DFF,
                    #9B7CFF
                );
                border-radius : 10px;
            }
            .recommendation{
                width : 100%;
                min-height : 190px;
                background : 
                linear-gradient(
                    135deg,
                    rgba(255,255,255,0.90),
                    rgba(238,232,255,0.95)
                    );
                color : #24104F;
                padding : 25px 30px;
                margin-top : 20px;
                border-radius : 12px;
                border-left : 5px solid #704DFF;
                box-shadow : 
                0 8px 25px rgba(40,20,80,0.15),
                0 0 20px rgba(90,60,255,0.10);
                box-sizing : border-box;
            }
            .recommendation h2{
                font-family : Georgia, serif;
                color : #38306B;
                margin : 0 0 12px 0;
                font-size: 24px;
            }
            .recommendation p{
                color : #403858;
                font-size : 16px;
                line-height : 1.6;
                margin-bottom : 0;
            }
            .retention-box{
                width : 100%;
                margin : 70px;
                background : linear-gradient(
                    135deg,
                    #30205C,
                    #44317A
                );
                border : 1px solid rgba(169,154,255,0.35);
                border-radius : 12px;
                display : flex;
                align-items : center;
                color : #F5F2FF;
                font-family : Georgia , serif;
                font-size : 20px;
                font-weight : bold;
                letter-spacing : 1px;
                box-shadow : 
                0 8px 25px rgba(0,0,0,0.20),
                0 0 18px rgba(90,60,255,0.12);
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

result_class = "stay" if prediction == 0 else "churn"
st.markdown(f"""
            <div class = "result-card">
            <h1 class = "{result_class}">{result}</h1>
            </div>
            """,unsafe_allow_html = True)

col1,col2 = st.columns([2,5] , gap = "medium")

with col1:
    if churn_probability is not None:
        st.markdown(f"""
                    <div class = "metric-card">
                    <h3>Churn Probability</h3>
                    <h1>{churn_probability:.1f}%</h1>
                    </div>
                    """,unsafe_allow_html = True)
        
with col2:
        st.markdown(f"""
                    <div class = "confidence">
                    <h1>Retention Confidence</h1>
                    <div class = "confidence-bar">
                    <div class = "confidence-fill" style = "width : {retention_probability:.1f}%;">
                    </div>
                    </div>
                    <p>{retention_probability:.1f}%</p>
                    </div>
                    """,unsafe_allow_html = True)
        
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