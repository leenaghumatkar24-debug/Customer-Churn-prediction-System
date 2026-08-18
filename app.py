import streamlit as st

st.set_page_config(
    page_title="Customer Retention",
    page_icon="📊",
    layout="wide",
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

            /* Hide sidebar button */
            [data-testid="collapsedControl"] {
                display: none;
            }

            /* Remove top spacing */
            .block-container {
            max-width: none !important;
            padding-top: 0px !important;
            padding-left: 0px !important;
            padding-right: 0px !important;
            margin: 0px !important;
            }

            /* Full width */
            [data-testid="stAppViewContainer"] {
            padding: 0px !important;
            padding-top: 0px !important;
            padding-left: 0px !important;
            padding-right: 0px !important;
            margin: 0px !important;
            
            [data-testid = "stBottom"]{
                display : none !important;
            }
            }
            </style>
            """, unsafe_allow_html=True)

st.markdown("""
            <style>
            [data-testid = "stSidebar"]{
                display : none !important;
            }
            header{
                display : none !important;
            }
            </style>
            """,unsafe_allow_html = True)

st.markdown("""
            <style>
            .stApp{
                background: 
                    radial-gradient(
                        ellipse at 15% 20%,
                        rgba(70,45,255,0.35),
                        transparent 25%
                    ),
                    radial-gradient(
                        ellipse at 75% 15%,
                        rgba(100,50,255,0.25),
                        transparent 30%
                    ),
                    radial-gradient(
                        ellipse at 45% 65%,
                        rgba(35,35,150,0.30),
                        transparent 35%
                    ),                    
                    radial-gradient(
                        ellipse at 90% 80%,
                        rgba(80,30,180,0.22),
                        transparent 30%
                    ),
                #16001F;
            }
            .block-container{
                max-width : none !important;
                padding-top : 0px !important;
                padding-left : 0px !important;
                padding-right : 0px !important;
                width : 100%;
                margin : 0px !important;
            }
            [data-testid="stAppViewContainer"]{
                width: 100%;
                padding: 0;
                margin: 0;
            }
            .hero{
                width : 100%;
                height : 320px;
                margin-top : -55px;
                background :
                linear-gradient(
                    rgba(0,0,0,0.5),
                    rgba(0,0,0,0.5)
                ),
                url("https://images.unsplash.com/photo-1497366811353-6870744d04b2");
                
                background-size : cover;
                background-position : center;
                
                display : flex;
                flex-direction : column;
                justify-content : center;
                align-items : center;
                
                text-align : center;
                color : #F5F2FF;   
                position : relative;
            }
            .hero h1{
                font-family : Georgia, serif;
                font-size : 85px;
                letter-spacing : 8px;
                margin : 0;
                color : #F5F2FF;
                text-shadow : 
                0 0 10px rgba(170,150,255,0.45),
                0 0 30px rgba(90,60,255,0.35);
            }
            .hero p{
                font-size : 19px;
                letter-spacing : 2px; 
                color : #C9FFD9;
                text-shadow :
                0 0 12px rgba(201,255,217,0.3);
            }
            .about-section {
                width: 90%;
                margin: 60px auto;
                display: flex;
                align-items: center;
                gap: 45px;
            }
            .image-card {
                width: 50%;
                height: 350px;
                overflow: hidden;
                border-radius: 5px;
            }
            .image-card img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            .about {
                width: 50%;
                background: 
                linear-gradient(
                    135deg,
                    rgba(35,0,55,0.90),
                    rgba(25,10,70,0.88),
                    rgba(15,20,65,0.90)
                );
                color: #F5F2FF;
                padding: 35px;
                border-radius: 12px;
                border : 1px solid rgba(169,154,255,0.30);
                box-shadow:
                0 10px 35px rgba(0,0,0,0.35),
                0 0 25px rgba(90,60,255,0.12)
            }
            .about h2 {
                font-family: Georgia, serif;
                font-size: 35px;
                margin-top: 0;
                color : #D8D0FF;
                letter-spacing : 2px;
                text-shadow : 
                0 0 15px rgba(120,90,255,0.35);
            }
            .about p {
                font-size: 17px;
                line-height: 1.7;
                color : #E4DFF2;
                letter-spacing : 0.3px;
            }
            .stButton{
                display : flex;
                justify-content : center;
                width : 100%;
            }
            .stButton > button{
                width : 250px;
                height : 75px;
                background : 
                linear-gradient(
                    90deg,
                    #3520A8,
                    #5B3FE8,
                    #704DFF
                );
                color : #F5F2FF;
                border : 1px solid rgba(190,175,255,0.55);
                font-size : 18px;
                font-weight : bold;
                letter-spacing : 2px;
                box-shadow : 
                0 0 15px rgba(90,60,255,0.30),
                0 8px 25px rgba(0,0,0,0.30);
                transition : all 0.3s ease;
            }
            .stButton > button:hover{
                background : 
                linear-gradient(
                    90deg,
                    #4B32D0,
                    #704DFF,
                    #8B7CFF
                );
                color : white;
                border : 1px solid #C4B8FF;
                box-shadow : 
                0 0 25px rgba(112,77,255,0.55),
                0 8px 30px rgba(0,0,0,0.35);
                transform : translateY(-2px);
            }
            .footer{
                width : 100%;
                margin-left : calc(-50vw + 50%);
                background : 
                linear-gradient(
                    135deg,
                    #10001F,
                    #17002D,
                    #0D1235
                );
                color : #D8D0FF;
                text-align : center;
                padding : 35px 0;
                margin-top : 60px;
                box-sizing : border-box;
                border-top : 1px solid rgba(139,124,255,0.25);
                box-shadow : 
                0 -10px 30px rgba(70,40,255,0.08);
            }
            .footer h3{
                font-family : Georgia, serif;
                margin : 0 0 10px 0;
                text-align : center;
                font-size : 24px;
                color : #F5F2FF;
                letter-spacing : 1px;
                text-shadow : 
                0 0 12px rgba(139,124,255,0.3);
            }
            .footer p{
                font-size : 14px;
                margin : 8px 0;
                text-align : center;
                color : #AFA6C8;
            }
            .block-container{
                padding-bottom : 0px !important;
                margin-bottom : 0px !important;
            }
            </style>
            """,unsafe_allow_html = True)

st.markdown("""
            <div class = "hero">
            <h1>Customer Retention</h1>
            <p>AI-POWERED RETENTION PREDICTION SYSTEM</p>
            </div>
            """,unsafe_allow_html = True)

st.markdown("""
            <div class="about-section">
            <div class="image-card">
            <img src="https://www.radius.com/_next/image/?q=75&url=https%3A%2F%2Fcms-radius-com-bucket.s3.eu-west-2.amazonaws.com%2FAdobe_Stock_671359381_ef22378f46.jpeg&w=3840">
            </div>

            <div class="about">
            <h2>About</h2>

            <p>
            Customer Retention Prediction System is an AI-powered project designed        
            to predict whether a customer is likely to continue using a company's        
            products or services. It analyzes customer information and behavioral
            patterns to identify customers who may be at risk of leaving.
            </p>

            <p>
            The system helps businesses understand customer retention patterns
            and make better decisions by providing an early prediction. This can
            help companies improve customer satisfaction, strengthen relationships,
            and develop suitable strategies to retain valuable customers.
            </p>
            </div>
            </div>
            """, unsafe_allow_html=True)


col1,col2,col3,col4,col5 = st.columns(5)

with col3:
                
    if st.button("CLICK TO BEGIN"):
        st.switch_page("pages\customer_input.py")
        
    st.markdown("</div>" , unsafe_allow_html =True)
    
st.markdown("""
            <div  class = "footer">
            <h3>Customer Retention Prediction System</h3>
            <p>AI-Powered customer retention analysis and prediction</p>
            <p>Developed as a Group Project</p>
            <p>© 2026 Customer Retention Prediction System</p>
            </div>
            """,unsafe_allow_html = True)