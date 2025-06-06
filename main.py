import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

st.set_page_config(page_title="Promo Mailer - One stop solution for your business promotion", layout="centered")
st.markdown('<h1 style="text-align: center;">📧 Promo Mailer</h1>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📎 Upload CSV (columns: name, email)", type=["csv"])

# Optional Attachment
attachment_file = st.file_uploader("📎 Upload an Attachment (Max 5 MB)", type=None)

sender_email = st.text_input("Your Email (e.g. youremail@email.com)", value="")
sender_password = st.text_input("App Password", type="password")
smtp_server = st.text_input("SMTP Server", value="smtp.gmail.com")
smtp_port = st.number_input("SMTP Port", value=465)

# Email Message
st.subheader("✉️ Compose Your Message")
subject = st.text_input("Email Subject", value="🚀 Let's Build With TestCompany")
default_body = """Hi {name},

We’re TestCompany -  helping businesses like yours with affordable and reliable technology services:

- Custom Websites
- Mobile Apps
- CRM & ERP Solutions
- Digital Marketing

Visit us: https://testcompany.com  
Contact: testcompany@test.com

Regards,  
Team TestCompany"""

body_template = st.text_area("Email Body (use {name} to personalize)", value=default_body, height=250)

confirm_word = st.text_input("Type 'CONFIRM' to send emails")

# Function to send email with optional attachment
def send_email(to_email, name):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    # Add email body
    body = MIMEText(body_template.format(name=name), 'plain')
    msg.attach(body)

    # Add attachment if provided
    if attachment_file is not None:
        if attachment_file.size <= 5 * 1024 * 1024:  # 5 MB limit
            part = MIMEApplication(attachment_file.read(), Name=attachment_file.name)
            part['Content-Disposition'] = f'attachment; filename="{attachment_file.name}"'
            msg.attach(part)
        else:
            return False, "Attachment exceeds 5 MB limit."

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
