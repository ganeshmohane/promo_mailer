import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="Promo Mailer - It delivers with 100/ gurantee", layout="centered")
st.title("📧 Promo Mailer")

uploaded_file = st.file_uploader("📎 Upload CSV (columns: name, email)", type=["csv"])

sender_email = st.text_input("Your Email (e.g. youremail@email.com)", value="")
sender_password = st.text_input("App Password", type="password")
smtp_server = st.text_input("SMTP Server", value="smtp.gmail.com")
smtp_port = st.number_input("SMTP Port", value=465)

# Email Message
st.subheader("✉️ Compose Your Message")
subject = st.text_input("Email Subject", value="🚀 Let's Build With Vassu Infotech")
default_body = """Hi {name},

We’re Vassu Infotech – helping businesses like yours with affordable and reliable technology services:

- Custom Websites
- Mobile Apps
- CRM & ERP Solutions
- Digital Marketing

Visit us: https://vassuinfotech.com  
Contact: vassu@infotech.com

Regards,  
Team Vassu Infotech"""

body_template = st.text_area("Email Body (use {name} to personalize)", value=default_body, height=250)

confirm_word = st.text_input("Type 'CONFIRM' to send emails")

# sending mail fn
def send_email(to_email, name):
    msg = MIMEText(body_template.format(name=name))
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True, ""
    except Exception as e:
        return False, str(e)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "name" not in df.columns or "email" not in df.columns:
        st.error("CSV must contain 'name' and 'email' columns.")
    else:
        st.success("✅ File loaded successfully!")
        st.write(df)

        if st.button("🔍 Preview First Email"):
            st.code(body_template.format(name=df.iloc[0]['name']), language='text')

        if confirm_word.strip().upper() == "CONFIRM":
            if st.button("🚀 Send Emails"):
                success, failed = 0, []

                for index, row in df.iterrows():
                    ok, err = send_email(row['email'], row['name'])
                    if ok:
                        success += 1
                    else:
                        failed.append((row['email'], err))

                st.success(f"✅ Sent {success} emails!")
                if failed:
                    st.error("Some emails failed to send:")
                    for email, error in failed:
                        st.text(f"{email} → {error}")
        else:
            st.warning("Type 'CONFIRM' to enable the send button.")
