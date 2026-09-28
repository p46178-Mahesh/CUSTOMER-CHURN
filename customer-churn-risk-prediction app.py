import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Risk Predictor",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load("customer_churn_model.pkl")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Customer Churn Risk Prediction")

st.write(
    """
    This AI-powered tool estimates the probability that a customer
    may churn based on their profile, engagement, purchase behaviour,
    digital activity and satisfaction.
    """
)

st.info(
    "This tool is intended to support managerial decision-making. "
    "The prediction should be considered alongside human judgement."
)

st.divider()

# ==================================================
# CUSTOMER PROFILE
# ==================================================

st.header("👤 Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    Customer_Age = st.number_input(
        "Customer Age",
        min_value=18,
        max_value=100,
        value=30
    )

    Gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    Country = st.text_input(
        "Country",
        value="India"
    )

with col2:
    Continent = st.text_input(
        "Continent",
        value="Asia"
    )

    City = st.text_input(
        "City",
        value="Mumbai"
    )

    Region = st.text_input(
        "Region",
        value="West"
    )

with col3:
    Customer_Segment = st.selectbox(
        "Customer Segment",
        ["New", "Regular", "Premium"]
    )

    Loyalty_Tier = st.selectbox(
        "Loyalty Tier",
        ["Bronze", "Silver", "Gold", "Platinum"]
    )

    Preferred_Category = st.text_input(
        "Preferred Category",
        value="Electronics"
    )


# ==================================================
# CUSTOMER ENGAGEMENT
# ==================================================

st.header("📱 Customer Engagement")

col1, col2, col3 = st.columns(3)

with col1:
    Total_Sessions = st.number_input(
        "Total Sessions",
        min_value=0,
        value=10
    )

    Total_Page_Views = st.number_input(
        "Total Page Views",
        min_value=0,
        value=50
    )

    Average_Session_Duration_Minutes = st.number_input(
        "Average Session Duration (Minutes)",
        min_value=0.0,
        value=5.0
    )

with col2:
    Products_Viewed = st.number_input(
        "Products Viewed",
        min_value=0,
        value=20
    )

    Products_Added_To_Cart = st.number_input(
        "Products Added to Cart",
        min_value=0,
        value=5
    )

    Cart_Abandonment_Count = st.number_input(
        "Cart Abandonment Count",
        min_value=0,
        value=1
    )

with col3:
    Wishlist_Items = st.number_input(
        "Wishlist Items",
        min_value=0,
        value=3
    )

    Product_Reviews_Count = st.number_input(
        "Product Reviews Count",
        min_value=0,
        value=2
    )

    Average_Product_Rating = st.number_input(
        "Average Product Rating",
        min_value=0.0,
        max_value=5.0,
        value=4.0
    )


# ==================================================
# PURCHASE BEHAVIOUR
# ==================================================

st.header("🛒 Purchase Behaviour")

col1, col2, col3 = st.columns(3)

with col1:
    Total_Orders = st.number_input(
        "Total Orders",
        min_value=0,
        value=5
    )

    Completed_Orders = st.number_input(
        "Completed Orders",
        min_value=0,
        value=4
    )

    Cancelled_Orders = st.number_input(
        "Cancelled Orders",
        min_value=0,
        value=0
    )

with col2:
    Returned_Orders = st.number_input(
        "Returned Orders",
        min_value=0,
        value=0
    )

    Total_Items_Purchased = st.number_input(
        "Total Items Purchased",
        min_value=0,
        value=8
    )

    Total_Spending_USD = st.number_input(
        "Total Spending (USD)",
        min_value=0.0,
        value=500.0
    )

with col3:
    Average_Order_Value_USD = st.number_input(
        "Average Order Value (USD)",
        min_value=0.0,
        value=100.0
    )

    Discount_Usage_Count = st.number_input(
        "Discount Usage Count",
        min_value=0,
        value=2
    )

    Average_Discount_Percentage = st.number_input(
        "Average Discount (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0
    )


# ==================================================
# CUSTOMER RELATIONSHIP
# ==================================================

st.header("🤝 Customer Relationship")

col1, col2, col3 = st.columns(3)

with col1:
    Coupon_Usage_Count = st.number_input(
        "Coupon Usage Count",
        min_value=0,
        value=1
    )

    Customer_Support_Contacts = st.number_input(
        "Customer Support Contacts",
        min_value=0,
        value=1
    )

with col2:
    Complaint_Count = st.number_input(
        "Complaint Count",
        min_value=0,
        value=0
    )

    Customer_Satisfaction_Score = st.number_input(
        "Customer Satisfaction Score",
        min_value=0.0,
        max_value=5.0,
        value=3.5
    )

with col3:
    Loyalty_Points = st.number_input(
        "Loyalty Points",
        min_value=0,
        value=500
    )

    Purchase_Frequency = st.text_input(
        "Purchase Frequency",
        value="Monthly"
    )


# ==================================================
# DIGITAL ENGAGEMENT
# ==================================================

st.header("📧 Digital Engagement")

col1, col2, col3 = st.columns(3)

with col1:
    Preferred_Payment_Method = st.selectbox(
        "Preferred Payment Method",
        ["Credit Card", "Debit Card", "UPI", "PayPal", "Cash"]
    )

    Preferred_Device = st.selectbox(
        "Preferred Device",
        ["Mobile", "Desktop", "Tablet"]
    )

with col2:
    Preferred_Marketing_Channel = st.selectbox(
        "Preferred Marketing Channel",
        ["Email", "Social Media", "SMS", "Push Notification"]
    )

    Email_Open_Rate_Percentage = st.number_input(
        "Email Open Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

with col3:
    Email_Click_Rate_Percentage = st.number_input(
        "Email Click Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0
    )

    Push_Notification_Engagement_Percentage = st.number_input(
        "Push Notification Engagement (%)",
        min_value=0.0,
        max_value=100.0,
        value=20.0
    )

Social_Media_Engagement_Score = st.number_input(
    "Social Media Engagement Score",
    min_value=0.0,
    max_value=100.0,
    value=30.0
)


# ==================================================
# RFM / CUSTOMER VALUE
# ==================================================

st.header("📈 Customer Value & Recency")

col1, col2, col3 = st.columns(3)

with col1:
    Customer_Lifetime_Value_USD = st.number_input(
        "Customer Lifetime Value (USD)",
        min_value=0.0,
        value=1000.0
    )

with col2:
    Recency_Days = st.number_input(
        "Recency (Days)",
        min_value=0,
        value=30
    )

with col3:
    RFM_Score = st.number_input(
        "RFM Score",
        min_value=0.0,
        value=5.0
    )


# ==================================================
# PREDICTION
# ==================================================

st.divider()

if st.button("🔮 Predict Customer Churn Risk", use_container_width=True):

    input_data = pd.DataFrame({
        "Customer_Age": [Customer_Age],
        "Gender": [Gender],
        "Country": [Country],
        "Continent": [Continent],
        "City": [City],
        "Region": [Region],
        "Customer_Segment": [Customer_Segment],
        "Total_Sessions": [Total_Sessions],
        "Total_Page_Views": [Total_Page_Views],
        "Average_Session_Duration_Minutes": [Average_Session_Duration_Minutes],
        "Products_Viewed": [Products_Viewed],
        "Products_Added_To_Cart": [Products_Added_To_Cart],
        "Cart_Abandonment_Count": [Cart_Abandonment_Count],
        "Total_Orders": [Total_Orders],
        "Completed_Orders": [Completed_Orders],
        "Cancelled_Orders": [Cancelled_Orders],
        "Returned_Orders": [Returned_Orders],
        "Total_Items_Purchased": [Total_Items_Purchased],
        "Total_Spending_USD": [Total_Spending_USD],
        "Average_Order_Value_USD": [Average_Order_Value_USD],
        "Discount_Usage_Count": [Discount_Usage_Count],
        "Average_Discount_Percentage": [Average_Discount_Percentage],
        "Coupon_Usage_Count": [Coupon_Usage_Count],
        "Wishlist_Items": [Wishlist_Items],
        "Product_Reviews_Count": [Product_Reviews_Count],
        "Average_Product_Rating": [Average_Product_Rating],
        "Customer_Support_Contacts": [Customer_Support_Contacts],
        "Complaint_Count": [Complaint_Count],
        "Preferred_Category": [Preferred_Category],
        "Preferred_Payment_Method": [Preferred_Payment_Method],
        "Preferred_Device": [Preferred_Device],
        "Preferred_Marketing_Channel": [Preferred_Marketing_Channel],
        "Email_Open_Rate_Percentage": [Email_Open_Rate_Percentage],
        "Email_Click_Rate_Percentage": [Email_Click_Rate_Percentage],
        "Push_Notification_Engagement_Percentage": [
            Push_Notification_Engagement_Percentage
        ],
        "Social_Media_Engagement_Score": [
            Social_Media_Engagement_Score
        ],
        "Loyalty_Points": [Loyalty_Points],
        "Loyalty_Tier": [Loyalty_Tier],
        "Customer_Lifetime_Value_USD": [
            Customer_Lifetime_Value_USD
        ],
        "Purchase_Frequency": [Purchase_Frequency],
        "Recency_Days": [Recency_Days],
        "RFM_Score": [RFM_Score],
        "Customer_Satisfaction_Score": [
            Customer_Satisfaction_Score
        ]
    })

    try:

        probability = model.predict_proba(input_data)[0][1]

        churn_percentage = probability * 100

        st.divider()

        st.header("🎯 Prediction Result")

        if probability >= 0.70:

            st.error(
                f"🔴 HIGH CHURN RISK — {churn_percentage:.1f}%"
            )

        elif probability >= 0.40:

            st.warning(
                f"🟡 MEDIUM CHURN RISK — {churn_percentage:.1f}%"
            )

        else:

            st.success(
                f"🟢 LOW CHURN RISK — {churn_percentage:.1f}%"
            )

        st.metric(
            "Predicted Churn Probability",
            f"{churn_percentage:.1f}%"
        )

        st.progress(float(probability))

        st.caption(
            "The prediction represents a model-estimated probability "
            "based on the information entered."
        )

    except Exception as e:

        st.error("Prediction could not be generated.")

        st.write("Error:", e)
