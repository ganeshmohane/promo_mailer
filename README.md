<h1 align="center">📧 Promo Mailer</h1>

<h3 align="center">Send personalized promotional emails in seconds using a simple, secure Streamlit interface.</h3>

---

**Promo Mailer** is a lightweight Streamlit-based email broadcasting app designed to help small businesses and teams send individual promotional emails from CSV files. Just upload your contact list, craft a message, and press send. Ideal for marketing, invites, or client outreach — no third-party email tools needed.

---

<h3 align="center">⚙️ Features</h3>

- Upload CSV with `name` and `email` fields
- Compose personalized messages using `{name}` placeholders
- Secure SMTP integration (supports Gmail, Zoho, Outlook, etc.)
- Sends one-to-one email (no CC/BCC spammy blast)
- Live preview + confirmation before sending
- Built with ❤️ using Python + Streamlit

---

<h3 align="center">🖼️ App Previews</h3>

<p align="center">
  <img src="https://github.com/user-attachments/assets/1cc93737-5882-45a7-8dad-06aede8f36be" width="600"/><br/>
  <img src="https://github.com/user-attachments/assets/5cbd0503-0bfb-415e-8c3e-535cb6f57ded" width="600"/><br/>
</p>

---

<h3 align="center">🚀 How to Run</h3>

```bash
uv venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -r requirements.txt
streamlit run main.py
