import smtplib
import time
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- CREDENTIALS ---
SENDER_EMAIL = "*******"
SENDER_PASSWORD = "*******" 
CALENDLY_LINK = "https://calendly.com/d/cx9x-gdd-2kr/meeting"

# --- RECIPIENTS ---
# I have kept the "Colleague" name for the first 56 to ensure the script doesn't crash
recipients = [
   
]

def run_campaign():
    try:
        # Connect to Gmail/Workspace SMTP
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        print(f"📡 Connection established. Sending {len(recipients)} emails...")

        for name, email in recipients:
            msg = MIMEMultipart()
            msg['From'] = f"Yisehak W. <{SENDER_EMAIL}>"
            msg['To'] = email
            # World-class Subject Line
            msg['Subject'] = f"{name}, Knotify + Regional White Labeling?"

            html_body = f"""
            <html>
            <body style="font-family: 'Helvetica', sans-serif; line-height: 1.6; color: #000; background-color: #fff;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #eee;">
                    <p>Hi {name},</p>
                    <p>I’m circling back because I don’t want you to miss the <b>regional play</b> here.</p>
                    <p>While <b>Knotify</b> is launching in Ethiopia, the problem is identical across East Africa. For my Cohort 1 colleagues, I’m exploring <b>White-Label Licensing</b>—giving you the infrastructure to deploy under your own brand in other markets.</p>
                    <p>I’d love to show you the tech and discuss how this fits your regional goals.</p>
                    <div style="margin: 30px 0; text-align: center;">
                        <a href="{CALENDLY_LINK}" 
                           style="background-color: #000; color: #fff; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 4px; display: inline-block;">
                           Grab a 15-minute slot →
                        </a>
                    </div>
                    <p>Talk soon,<br><strong>Yisehak</strong><br>
                    <span style="font-size: 12px; color: #666;">Founder & CTO, Ndoto IT Solutions</span></p>
                </div>
            </body>
            </html>
            """
            msg.attach(MIMEText(html_body, 'html'))
            
            server.send_message(msg)
            print(f"✅ Success: {name} ({email})")
            
            # Anti-spam delay: 45 to 90 seconds
            time.sleep(random.randint(45, 90))

        server.quit()
        print("\n🏁 Campaign finished successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_campaign()
