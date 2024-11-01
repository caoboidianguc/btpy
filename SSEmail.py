import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.mail.yahoo.com"
sender_email = "cao_boi_dia_nguc@yahoo.com.vn" 
receiver_email = "daniel.relentlessnightlife@hotmail.com" 
password = "lkakniyabugyeceh"
message = """\
Subject: Hi there

This message is sent from prey."""
n = 400
so = 0
while n > 1:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        so += 1
        print(f"xong lan thu {so}")
    n -= 1