import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Star Airfare | Flight Booking System",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Professional Styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #F9FAFB;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E5E7EB;
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State
if "profiles" not in st.session_state:
    st.session_state.profiles = {}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = ""

# App Header
st.markdown(
    '<div class="main-header">🌟 STAR AIRFARE</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-header">Your Trusted Partner for Seamless Journeys</div>',
    unsafe_allow_html=True,
)

# Sidebar Navigation / Login Simulator
with st.sidebar:
    st.image(
        "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=500&auto=format&fit=crop&q=60",
        use_container_width=True,
    )
    st.title("🔐 Authentication")

    if not st.session_state.logged_in:
        username = st.text_input("Username (Min 8 chars)")
        password = st.text_input("Password (Digits only)", type="password")

        if st.button("Log In", use_container_width=True):
            if len(username) >= 8 and password.isdigit():
                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error(
                    "Please provide valid info: Username >= 8 chars, Password must be digits."
                )
    else:
        st.success(f"Logged in as: **{st.session_state.current_user}**")
        if st.button("Log Out", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_user = ""
            st.rerun()

    st.markdown("---")
    st.markdown("### 📞 Quick Support")
    st.info("Need help? Call us at **1800-STAR-FLY**")

# Main Application Tabs (Only accessible if logged in, or viewable with warnings)
if st.session_state.logged_in:
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "👤 Create Profile",
            "✈️ Flight Details",
            "🏷️ Discounts",
            "🎫 Book a Seat",
            "❓ Enquiry",
        ]
    )

    # 1. Create Profile Tab
    with tab1:
        st.subheader("Create Your Passenger Profile")
        with st.form("profile_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name")
                dob = st.date_input("Date of Birth")
                number = st.text_input("Mobile Number (10 digits)")
            with col2:
                email = st.text_input("Email Address")
                anum = st.text_input("Aadhaar Number (12 digits)", type="password")

            submitted = st.form_submit_button(
                "Generate Profile", use_container_width=True
            )
            if submitted:
                if len(number) != 10 or not number.isdigit():
                    st.error("Please provide a valid 10-digit mobile number.")
                elif len(anum) != 12 or not anum.isdigit():
                    st.error("Please provide a valid 12-digit Aadhaar number.")
                elif not name or not email:
                    st.warning("All fields are required.")
                else:
                    profile_code = random.randint(1000, 9999)
                    st.session_state.profiles[profile_code] = {
                        "name": name,
                        "dob": str(dob),
                        "number": number,
                        "email": email,
                        "Anum": "[Aadhaar Redacted]",
                    }
                    st.success(
                        f"Profile Created Successfully! Your Profile Code is: **{profile_code}**"
                    )

    # 2. Flight Details Tab
    with tab2:
        st.subheader("Available Flights in Gujarat")

        flights = [
            {
                "id": 1,
                "route": "Ahmedabad to Uttarakhand",
                "price": 7000,
                "plane_id": 4678,
                "date": "7 August",
                "time": "12:00 AM",
                "class": "Economy Only",
            },
            {
                "id": 2,
                "route": "Rajkot to Mumbai",
                "price": 5000,
                "plane_id": 7645,
                "date": "7 August",
                "time": "1:00 AM",
                "class": "Economy Only",
            },
            {
                "id": 3,
                "route": "Ahmedabad to Delhi",
                "price": 6000,
                "plane_id": 8723,
                "date": "7 August",
                "time": "10:00 AM",
                "class": "All Economy",
            },
            {
                "id": 4,
                "route": "Rajkot to Goa",
                "price": 8000,
                "plane_id": 3409,
                "date": "7 August",
                "time": "9:00 PM",
                "class": "Economy Only",
            },
            {
                "id": 5,
                "route": "Ahmedabad to Kolkata",
                "price": 8000,
                "plane_id": 9823,
                "date": "7 August",
                "time": "7:00 AM",
                "class": "Economy Only",
            },
        ]

        for f in flights:
            with st.container():
                st.markdown(
                    f"""
                    <div class="card">
                        <h3>Flight #{f['id']}: {f['route']}</h3>
                        <p><b>Plane ID:</b> {f['plane_id']} | <b>Date:</b> {f['date']} | <b>Time:</b> {f['time']}</p>
                        <p><b>Class:</b> {f['class']} | <b>Price:</b> ₹{f['price']}</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

    # 3. Discount Details Tab
    with tab3:
        st.subheader("Available Discount Schemes")
        st.markdown(
            """
        - 🎓 **Student Discount:** Get **10% OFF** on applicable fares.
        - 👥 **Group Discount:** Get **5% OFF** when traveling in groups.
        - ❌ **No Discount:** Standard pricing applies.
        """
        )

        selected_discount = st.selectbox(
            "Select your discount category:",
            ["Select...", "Student Discount (10%)", "Group Discount (5%)", "None (0%)"],
        )
        if "10%" in selected_discount:
            st.success("You qualify for a 10% discount!")
        elif "5%" in selected_discount:
            st.success("You qualify for a 5% discount!")
        elif "None" in selected_discount:
            st.info("Standard pricing will apply.")

    # 4. Book a Seat Tab
    with tab4:
        st.subheader("Book Your Flight Seat")

        flight_price = {1: 7000, 2: 5000, 3: 6000, 4: 8000, 5: 8000}
        flight_names = {
            1: "Ahmedabad to Uttarakhand (₹7000)",
            2: "Rajkot to Mumbai (₹5000)",
            3: "Ahmedabad to Delhi (₹6000)",
            4: "Rajkot to Goa (₹8000)",
            5: "Ahmedabad to Kolkata (₹8000)",
        }
        discount_map = {
            "Student Discount (10%)": 10,
            "Group Discount (5%)": 5,
            "None (0%)": 0,
        }

        selected_flight = st.selectbox(
            "Choose Preferred Flight",
            options=list(flight_names.keys()),
            format_func=lambda x: flight_names[x],
        )
        selected_disc_type = st.selectbox(
            "Choose Discount Plan", options=list(discount_map.keys())
        )

        if st.button("Calculate & Confirm Booking", use_container_width=True):
            base_price = flight_price[selected_flight]
            disc_percent = discount_map[selected_disc_type]
            dis_amount = base_price * disc_percent / 100
            final_amount = base_price - dis_amount

            st.balloons()
            st.success("Booking Confirmed!")
            st.metric(label="Base Price", value=f"₹{base_price}")
            st.metric(label="Discount Applied", value=f"₹{dis_amount} ({disc_percent}%)")
            st.metric(label="Final Payable Amount", value=f"₹{final_amount}")

    # 5. Enquiry Tab
    with tab5:
        st.subheader("Customer Support & Enquiries")
        enquiry_option = st.selectbox(
            "What would you like to know about?",
            [
                "Class Information",
                "Emergency Flight Information",
                "Discount Information",
            ],
        )

        if enquiry_option == "Class Information":
            st.markdown(
                """
                ### Class Information
                * **Economy, Premium Economy, Business, & First Class** available.
                * Choose based on your budget, comfort needs, and baggage allowance.
                * Each class offers generous seating space and curated food services.
            """
            )
        elif enquiry_option == "Emergency Flight Information":
            st.markdown(
                """
                ### Emergency Flight Support
                * In case of emergency, visit our airport office directly.
                * We facilitate emergency seat bookings for individuals or groups (5+ people).
                * Nominal emergency handling charges may apply.
            """
            )
        elif enquiry_option == "Discount Information":
            st.markdown(
                """
                ### Discount Policy
                * **10%** discount exclusively for students with valid IDs.
                * **5%** discount for group bookings.
                * Limited period offers apply.
            """
            )

else:
    st.warning("⚠️ Please log in via the sidebar to access the Star Airfare portal.")