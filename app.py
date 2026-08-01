import streamlit as st

st.set_page_config(page_title="Electricity Bill Calculator", page_icon="⚡", layout="centered")

st.title("⚡ Electricity Bill Calculator")
st.write("Enter your consumer details and meter readings below to calculate your tiered electricity bill.")

st.markdown("---")

# Input fields
user_name = st.text_input("Enter the consumer name:")
user_id = st.text_input("Enter the consumer id:")

col1, col2 = st.columns(2)
with col1:
    current_reading = st.number_input("Enter the current reading:", min_value=0.0, step=1.0)
with col2:
    previous_reading = st.number_input("Enter the previous reading:", min_value=0.0, step=1.0)

st.markdown("---")

if st.button("Generate Bill", type="primary"):
    if not user_name or not user_id:
        st.error("Please enter both consumer name and consumer ID.")
    else:
        consumed_current = current_reading - previous_reading

        if consumed_current < 0:
            st.error("The current reading cannot be less than the previous reading.")
        else:
            # Multi-tier slab billing logic
            if consumed_current < 200:
                final_amount = consumed_current * 0
            elif consumed_current < 400:
                final_amount = consumed_current * 5
            elif consumed_current < 600:
                final_amount = consumed_current * 8
            elif consumed_current < 800:
                final_amount = consumed_current * 11
            else:
                final_amount = consumed_current * 13

            # Bill Report Display
            st.subheader("📋 BILL REPORT")
            st.markdown(f"**Consumer Name:** {user_name}")
            st.markdown(f"**Consumer ID:** {user_id}")
            st.markdown("---")
            st.markdown(f"**Current Reading:** {current_reading}")
            st.markdown(f"**Previous Reading:** {previous_reading}")
            st.markdown(f"**Consumed Units:** {consumed_current}")
            st.markdown("---")
            st.success(f"### Total Bill: ₹{final_amount:.2f}")
