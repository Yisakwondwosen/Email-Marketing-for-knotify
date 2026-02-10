import smtplib
import os
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# --- MAILJET AUTHENTICATION ---
SMTP_SERVER = "in-v3.mailjet.com"
SMTP_PORT = 587
SENDER_EMAIL = "yisehak@knotifyapp.com" 
API_KEY = "2cc2da20a86382a903744f4e3ce8508a"
API_SECRET = "a05402d509742bc6e9b7da80c15d0bc9"

CALENDLY_LINK = "https://calendly.com/d/cx9x-gdd-2kr/meeting"
TEST_RECIPIENT = "yitzakwondwosen@gmail.com"
RECIPIENT_NAME = "Isaac"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_minimalist_circular_email():
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() 
            server.login(API_KEY, API_SECRET)
            
            # 'related' for CID inline images
            msg = MIMEMultipart('related')
            msg['From'] = f"Yisehak (DTA Alumnus) <{SENDER_EMAIL}>"
            msg['To'] = TEST_RECIPIENT
            msg['Subject'] = "quick dta question"

            # HTML UI/UX with Circle Headshot Only
            html_body = f"""
            <html>
            <body style="margin: 0; padding: 0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #1a1a1a; background-color: #ffffff;">
                <div style="max-width: 600px; margin: 0 auto; padding: 40px; border: 1px solid #f0f0f0;">
                    <p style="font-size: 16px; margin-bottom: 25px;">Hi {RECIPIENT_NAME},</p>
                    
                    <p style="font-size: 16px; line-height: 1.6;">I was looking at the RLC cohort list and realized I haven't shown you the regional infrastructure we're building for <b>Knotify</b> yet.</p>
                    
                    <p style="font-size: 16px; line-height: 1.6;">Since you're in the cohort, I'm opening up a few licensing slots so you can run this under your own brand in your market. I'd rather keep this within our group before it goes public.</p>
                    
                    <div style="margin: 35px 0;">
                        <a href="{CALENDLY_LINK}" style="background-color: #000000; color: #ffffff; padding: 14px 28px; text-decoration: none; font-size: 15px; font-weight: 600; border-radius: 4px; display: inline-block;">
                            Book a 10-min sync here →
                        </a>
                    </div>
                    
                    <p style="font-size: 16px; margin-bottom: 40px;">Best,<br>Yisehak</p>

                    <div style="border-top: 2px solid #000000; padding-top: 25px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td width="85" style="vertical-align: top;">
                                    <img src="cid:headshot" width="80" height="80" style="border-radius: 50%; display: block; border: 0; object-fit: cover;">
                                </td>
                                <td style="padding-left: 20px; vertical-align: middle;">
                                    <p style="margin: 0; font-size: 18px; font-weight: bold; color: #000000;">Yisehak Wondwossen</p>
                                    <p style="margin: 4px 0 0 0; font-size: 14px; color: #666666;">CEO & Growth Lead | KnotifyApp</p>
                                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #999999; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">DTA Cohort 1</p>
                                </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </body>
            </html>
            """
            msg.attach(MIMEText(html_body, 'html'))

            # --- CID ATTACHMENT (Headshot Only) ---
            with open("Assets/Isaac.JPG", 'rb') as f:
                img_head = MIMEImage(f.read())
                img_head.add_header('Content-ID', '<headshot>')
                msg.attach(img_head)

            server.send_message(msg)
            logging.info(f"✅ SUCCESS: Minimalist Circular UI sent to {TEST_RECIPIENT}")

    except Exception as e:
        logging.error(f"❌ ERROR: {e}")

if __name__ == "__main__":
    send_minimalist_circular_email()
