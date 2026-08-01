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
            final_amount = 0.0
            
            # Condition 1: If consumed units are less than 500 (First 200 units free)
            if consumed_current < 500:
                billable_units = max(0.0, consumed_current - 200)
                # Apply rates for units above 200 up to 400 and 400-500
                if billable_units <= 200:
                    final_amount = billable_units * 4.50
                else:
                    final_amount = (200 * 4.50) + ((billable_units - 200) * 6.30)
            
            # Condition 2: If consumed units are 500 or more (Only first 100 units free)
            else:
                billable_units = max(0.0, consumed_current - 100)
                
                # Calculating slab by slab for accuracy
                if billable_units <= 300: # 101 to 400 range
                    final_amount = billable_units * 4.50
                elif billable_units <= 400: # up to 500
                    final_amount = (300 * 4.50) + ((billable_units - 300) * 6.30)
                elif billable_units <= 500: # up to 600
                    final_amount = (300 * 4.50) + (100 * 6.30) + ((billable_units - 400) * 8.40)
                elif billable_units <= 700: # up to 800
                    final_amount = (300 * 4.50) + (100 * 6.30) + (100 * 8.40) + ((billable_units - 500) * 9.45)
                elif billable_units <= 900: # up to 1000
                    final_amount = (300 * 4.50) + (100 * 6.30) + (100 * 8.40) + (200 * 9.45) + ((billable_units - 700) * 10.50)
                else: # above 1000
                    final_amount = (300 * 4.50) + (100 * 6.30) + (100 * 8.40) + (200 * 9.45) + (200 * 10.50) + ((billable_units - 900) * 11.55)

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
