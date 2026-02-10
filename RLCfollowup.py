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
    ("Colleague", "hazaba19@gmail.com"), ("Colleague", "abdirisak.gelle@gmail.com"), 
    ("Colleague", "abdullahi@mtii.edu.so"), ("Colleague", "abunajk@gmail.com"), 
    ("Colleague", "abelngengele@gmail.com"), ("Colleague", "gaellrop@gmail.com"),
    ("Colleague", "adelaidejachi33@gmail.com"), ("Colleague", "advaxe.mucatcha@gmail.com"), 
    ("Colleague", "ches7alex@gmail.com"), ("Isaac", "yitzakwondwosen@gmail.com"), 
    ("Colleague", "megdad.elfaki@gmail.com"), ("Colleague", "alphonsebyembao8@gmail.com"),
    ("Colleague", "mnuwayo@gmail.com"), ("Colleague", "ansasirajanet19@gmail.com"), 
    ("Colleague", "a.said@mediaconvergency.co.tz"), ("Colleague", "nukuriardinemartine@gmail.com"), 
    ("Colleague", "assilaabdallah@gmail.com"), ("Colleague", "mulukluka22@gmail.com"),
    ("Colleague", "joycegerold0@gmail.com"), ("Colleague", "atukundamartha911@gmail.com"), 
    ("Colleague", "violadut20@gmail.com"), ("Colleague", "bamlakfellekecc@gmail.com"), 
    ("Colleague", "barnabaosman1916@gmail.com"), ("Colleague", "bekagetnet@gmail.com"),
    ("Colleague", "betelhemghere21@gmail.com"), ("Colleague", "btabbynamwone@gmail.com"), 
    ("Colleague", "aterchan54@gmail.com"), ("Colleague", "chemustojoel@gmail.com"), 
    ("Colleague", "jeankarani@gmail.com"), ("Colleague", "collinsyogoh@gmail.com"),
    ("Colleague", "ellairadukunda06@gmail.com"), ("Colleague", "bida@bidathomas.me"), 
    ("Colleague", "jimmyezra15@gmail.com"), ("Colleague", "erickmnyali14@gmail.com"), 
    ("Colleague", "esayasyohannes12@gmail.com"), ("Colleague", "esta@medpack.co.tz"),
    ("Colleague", "fabrisioyibrah@gmail.com"), ("Colleague", "fevenalemu2008@gmail.com"), 
    ("Colleague", "gloriahtirot@gmail.com"), ("Colleague", "21gracedavid@gmail.com"), 
    ("Colleague", "graceknamatende@gmail.com"), ("Colleague", "isaacmuhumuza881@gmail.com"),
    ("Colleague", "israelasfaw7@gmail.com"), ("Colleague", "jamesmayenmachiek@gmail.com"), 
    ("Colleague", "jescamagashi101@gmail.com"), ("Colleague", "umujoie2002@gmail.com"), 
    ("Colleague", "fallkadidja20@gmail.com"), ("Colleague", "elishakakanyero5@gmail.com"),
    ("Colleague", "kalohissen@gmail.com"), ("Colleague", "keitesiaisha@gmail.com"), 
    ("Colleague", "l9chambiri@gmail.com"), ("Colleague", "lucytomeka@gmail.com"), 
    ("Colleague", "lnnjoroge@dtbafrica.com"), ("Colleague", "bereketlulia942@gmail.com"),
    ("Colleague", "kosgeylynet@gmail.com"), ("Colleague", "meklitmnot@gmail.com"),
    ("Magreth", "magrethdmkumbo@gmail.com"), ("Peace", "peacemasika8@gmail.com"),
    ("Mohamed", "mahamedkadir12@gmail.com"), ("Ezra", "mrezy45@gmail.com"),
    ("Prisca", "priscamukelenga006@gmail.com"), ("Munguzo", "joe604590@gmail.com"),
    ("EmpowerRise", "empowerrisehub@gmail.com"), ("Nahom", "nahomkilng@gmail.com"),
    ("Trudy", "trudyvanitah@gmail.com"), ("Shakirah", "nakalemashakirah6@gmail.com"),
    ("Nancy", "ishimwenancysabrina1@gmail.com"), ("Nancy", "nancygakii25@gmail.com"),
    ("Natnael", "natnaeldechasa78@gmail.com"), ("Venuste", "ndayivenuste11@gmail.com"),
    ("Ruth", "zzindarutz@gmail.com"), ("Ratifa", "ratifaniringiyimana79@gmail.com"),
    ("Ruth", "nibitangaruth0@gmail.com"), ("Ann", "njukiann4@gmail.com"),
    ("Noella", "dushakenoella@gmail.com"), ("Nyuon", "nyuonlual7@gmail.com"),
    ("Paul", "pauln5816@gmail.com"), ("Racheal", "rachealmonic5@gmail.com"),
    ("Rodney", "rodney.omondi254@gmail.com"), ("HARUUN", "yakarimu.2024@gmail.com"),
    ("Salim", "salimseleman722@gmail.com"), ("Samson", "kukusaeed1996@gmail.com"),
    ("Selamawit", "selamsun7@gmail.com"), ("AFRICAN", "africa.com.et@gmail.com"),
    ("Shamid", "mukalushamid@gmail.com"), ("Sijin", "sijin.tuony@nobilisplus.ch"),
    ("Simon", "simon.ntugi@gmail.com"), ("Soliana", "habteabsoliana@gmail.com"),
    ("Ivan", "iuwadukunze@gmail.com"), ("Ibrahim", "ibrahim@zati.africa"),
    ("Wenslous", "wayneotemahegesa@gmail.com"), ("Nebiyu", "nebiyugirma19@gmail.com"),
    ("Tim", "timbambala6@gmail.com"), ("Tinbite", "dawittinbite22@gmail.com"),
    ("Xaviour", "alukuxaviour@gmail.com"), ("Zainab", "zeynoba00@gmail.com"),
    ("Zamzam", "zammc05@gmail.com")
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
