import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Real Estate Buyer Segmentation", page_icon="🏡", layout="wide")
st.title("🏡 Real Estate Buyer Segmentation")
st.caption("K-Means clustering | Final model: K = 7")
st.write("Explore the seven buyer segments identified in the project. These are the segment-level results recorded during analysis.")

segments = pd.DataFrame([
    [0, "Premium Home Buyers", 399, 19.95, 3.44, 1478320.34, 431199.10, 1416.35, 2.81, "100% Home", "100% Individual"],
    [1, "Individual Investment Buyers", 326, 16.30, 3.56, 1055098.88, 296773.69, 985.59, 2.90, "100% Investment", "100% Individual"],
    [2, "Satisfied Home Buyers", 496, 24.80, 3.70, 1186392.92, 320824.55, 1065.44, 4.21, "100% Home", "100% Individual"],
    [3, "Low-Satisfaction Home Buyers", 392, 19.60, 3.56, 1072649.55, 301399.41, 1002.73, 1.71, "100% Home", "100% Individual"],
    [4, "Larger-Property Investors", 237, 11.85, 3.47, 1420361.42, 410221.86, 1343.78, 3.17, "100% Investment", "100% Individual"],
    [5, "Corporate Property Buyers", 102, 5.10, 3.61, 1240325.73, 345480.71, 1145.10, 3.05, "65.7% Home / 34.3% Investment", "100% Company"],
    [6, "High-Frequency Individual Buyers", 48, 2.40, 7.38, 2393135.81, 325918.58, 1077.65, 3.54, "64.6% Home / 35.4% Investment", "97.9% Individual / 2.1% Company"],
], columns=["cluster", "segment_name", "buyer_count", "buyer_percentage", "avg_properties", "avg_total_purchase_value", "avg_purchase_price", "avg_floor_area", "avg_satisfaction", "purpose_profile", "client_profile"])

a, b, c, d = st.columns(4)
a.metric("Buyer profiles", "2,000")
b.metric("Segments", "7")
c.metric("Largest segment", "496 buyers")
d.metric("Silhouette score", "0.289")
st.info("The reported silhouette score indicates modest separation between clusters. Segment names are descriptive interpretations, not verified customer categories.")

chosen = st.multiselect("Filter segments", segments["segment_name"].tolist(), default=segments["segment_name"].tolist())
view = segments[segments["segment_name"].isin(chosen)]
left, right = st.columns(2)
with left:
    fig = px.bar(view.sort_values("buyer_count", ascending=False), x="segment_name", y="buyer_count", title="Number of buyers by segment", text="buyer_count")
    fig.update_layout(xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)
with right:
    fig = px.bar(view.sort_values("avg_satisfaction", ascending=False), x="segment_name", y="avg_satisfaction", title="Average satisfaction by segment", text="avg_satisfaction")
    fig.update_layout(xaxis_tickangle=-30, yaxis_range=[0, 5])
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Segment profile")
st.dataframe(view, use_container_width=True, hide_index=True)
st.download_button("Download segment summary CSV", segments.to_csv(index=False).encode("utf-8"), "real_estate_segment_summary_k7.csv", "text/csv")

st.subheader("Optional: inspect buyer-level CSV")
uploaded = st.file_uploader("Upload your final buyer-level CSV", type=["csv"])
if uploaded:
    buyers = pd.read_csv(uploaded)
    st.write("Dataset shape:", buyers.shape)
    st.dataframe(buyers.head(20), use_container_width=True)
    cols = [x for x in buyers.columns if "cluster" in x.lower() or "segment" in x.lower()]
    if cols:
        col = st.selectbox("Select cluster/segment column", cols)
        st.dataframe(buyers[col].value_counts(dropna=False).rename_axis(col).reset_index(name="records"), use_container_width=True, hide_index=True)

with st.expander("Methodology and limitations"):
    st.markdown("""
- Model: K-Means with K = 7.
- Selected buyer-level features: properties purchased, average purchase price, average floor area, satisfaction score, acquisition purpose, and client type.
- Categorical fields were one-hot encoded and features standardized before clustering.
- K = 7 had the highest reported silhouette score among the tested values (K = 3–8): 0.289.
- Summary values reproduce the project results shared during development; they have not been independently recalculated from raw CSVs here.
- Confirm the currency/unit of purchase values from the source dataset.
""")
st.caption("Real Estate Buyer Segmentation | Exploratory decision-support dashboard")
