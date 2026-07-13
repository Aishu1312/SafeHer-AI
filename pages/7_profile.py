import streamlit as st
from styles.css import inject_custom_css

st.set_page_config(page_title="Profile Settings - SafeHer AI", page_icon="👤", layout="wide")
inject_custom_css()

st.title("👤 Profile Settings")
st.caption("Manage your personal information and emergency contacts")
st.markdown("---")

tab1, tab2 = st.tabs(["Personal Information", "Emergency Contacts"])

with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Edit Profile")
    
    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            username = st.text_input("Full Name", value=st.session_state.user['username'])
            email = st.text_input("Email", value=st.session_state.user['email'])
        with col2:
            mobile = st.text_input("Mobile Number", value=st.session_state.user['mobile'])
            bg_options = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Unknown"]
            current_bg = st.session_state.user.get('blood_group', 'Unknown')
            if current_bg not in bg_options: current_bg = "Unknown"
            blood_group = st.selectbox("Blood Group", bg_options, index=bg_options.index(current_bg))
            
        if st.form_submit_button("💾 Save Profile", type="primary"):
            st.session_state.user['username'] = username
            st.session_state.user['email'] = email
            st.session_state.user['mobile'] = mobile
            st.session_state.user['blood_group'] = blood_group
            st.success("✅ Profile updated successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Manage Emergency Contacts")
    
    contacts = st.session_state.user.get('emergency_contacts', [])
    
    for i, contact in enumerate(contacts):
        c1, c2, c3, c4 = st.columns([3, 3, 3, 1])
        with c1:
            st.text_input("Name", value=contact['name'], key=f"name_{i}", disabled=True)
        with c2:
            st.text_input("Phone", value=contact['phone'], key=f"phone_{i}", disabled=True)
        with c3:
            st.text_input("Relation", value=contact['relation'], key=f"rel_{i}", disabled=True)
        with c4:
            st.write("")
            st.write("")
            if st.button("🗑️", key=f"del_{i}"):
                contacts.pop(i)
                st.session_state.user['emergency_contacts'] = contacts
                st.rerun()
                
    st.markdown("---")
    st.subheader("Add New Contact")
    with st.form("add_contact_form"):
        nc1, nc2, nc3 = st.columns(3)
        with nc1:
            new_name = st.text_input("Contact Name")
        with nc2:
            new_phone = st.text_input("Phone Number")
        with nc3:
            new_relation = st.selectbox("Relation", ["Mother", "Father", "Sister", "Brother", "Friend", "Husband", "Other"])
            
        if st.form_submit_button("➕ Add Contact"):
            if new_name and new_phone:
                contacts.append({"name": new_name, "phone": new_phone, "relation": new_relation})
                st.session_state.user['emergency_contacts'] = contacts
                st.success(f"Added {new_name} to emergency contacts!")
                st.rerun()
            else:
                st.error("Please fill in name and phone number.")
    
    st.markdown("</div>", unsafe_allow_html=True)
