import smtplib
import time
import random
import logging
import base64
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- AUTHENTICATION ---
SMTP_SERVER = "smtp.zoho.com"
SMTP_PORT = 465
SENDER_EMAIL = "********" 
SENDER_PASSWORD = "***********" 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- DATA MANAGEMENT ---
# These are everyone who was successful in your last two log windows
already_sent = [
    
]

# Remaining to be sent:
recipients = [
    
]

# --- IMAGE ENCODING ---
IMAGE_PATH = "Assets/Isaac.JPG" # Adjusted for your folder structure
img_data = ""
if os.path.exists(IMAGE_PATH):
    with open(IMAGE_PATH, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode('utf-8')

def send_direct_email(first_name, email_addr):
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = f"Yisehak Wondwossen <{SENDER_EMAIL}>"
        msg['To'] = email_addr
        msg['Subject'] = f"{first_name} - Quick DTA Cohort 'ask' (KnotifyApp)"

        html_body = f"""
        <html>
        <body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background-color: #ffffff; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: #ffffff; border: 1px solid #eeeeee;">
                <div style="background-color: #000000; padding: 30px; text-align: center;">
                    <h1 style="margin: 0; color: #ffffff; font-size: 24px; letter-spacing: 3px; font-weight: bold;">KNOTIFY</h1>
                </div>
                <div style="padding: 40px; color: #000000; line-height: 1.6;">
                    <p style="font-size: 16px;">Hey {first_name},</p>
                    <p>While we were navigating the RLC program, I was obsessed with one thing: <b>Closing the school communication gap in East Africa.</b></p>
                    <p>As a fellow DTA Cohort 1 member, I’m giving you early access to the KnotifyApp MVP. Explore the experience using these testing profiles:</p>
                    <div style="background-color: #f4f4f4; padding: 20px; border-radius: 4px; margin: 20px 0; border-left: 4px solid #000;">
                        <p style="margin: 0 0 10px 0;"><b>1. SCHOOL ADMIN:</b><br>UserName: 934268954 | Pass: Passworddta2026!</p>
                        <p style="margin: 0 0 10px 0;"><b>2. TEACHER ACCESS:</b><br>Phone: 911223344 | Pass: Knotify@2026</p>
                        <p style="margin: 0;"><b>3. PARENT ACCESS:</b><br>Phone: 922334455 | Pass: Parent#Test</p>
                    </div>
                    <p>Could you give me 5 minutes of your "DTA eyes"? I value your perspective on our infrastructure.</p>
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="https://knotifyapp.com" style="background-color: #000000; color: #ffffff; padding: 15px 30px; text-decoration: none; font-weight: bold; border-radius: 2px; display: inline-block;">EXPLORE THE MVP</a>
                    </div>
                </div>
                <div style="padding: 30px 40px; background-color: #ffffff; border-top: 1px solid #eeeeee;">
                    <table border="0" cellpadding="0" cellspacing="0">
                        <tr>
                            <td><img src="data:image/jpeg;base64,{img_data}" alt="Isaac" style="width: 75px; height: 75px; border-radius: 6px; object-fit: cover; display: block;"></td>
                            <td style="padding-left: 20px;">
                                <p style="margin: 0; font-size: 16px; font-weight: bold; color: #000;">Yisehak (Isaac) Wondwossen</p>
                                <p style="margin: 2px 0; font-size: 13px; color: #666;">Chief Executive Officer & Growth Lead</p>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(html_body, 'html'))

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            
        logging.info(f"SUCCESS: {first_name} | Target: {email_addr}")
        return True
    except Exception as e:
        logging.error(f"FAIL: {email_addr} | Error: {e}")
        return False

def main():
    for name, email in recipients:
        if email.lower() in [e.lower() for e in already_sent]:
            continue
            
        success = send_direct_email(name, email)
        
        # Consistent cooling to stay under the radar
        wait = random.randint(150, 350)
        logging.info(f"Cooling for {wait}s...")
        time.sleep(wait)

    logging.info("Batch completed.")

if __name__ == "__main__":
    main()
