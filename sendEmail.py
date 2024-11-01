import smtplib, ssl


smtpServer = 'smtp.gmail.com'
port = 465

nguoiGui = 'hoadambutxinh@gmail.com'
mk = "seztdjfrcdbcykvp"
# matKhau = input('Mat Khau: ')
context = ssl.create_default_context()
# daniel.relentlessnightlife@hotmail.com
nguoiNhan = "jubilanthibi@gmail.com"
# input('Gui cho: ')
chuDe = "hey! thief"
# input('Chu De: ')
noidung = "have a nice day"
# input('Tin Nhan: ')

tinNhan = """Subject: {}
To: {}
{}
 """.format(chuDe, nguoiNhan, noidung)
n = 2
so = 0
while n > 1:
    with smtplib.SMTP_SSL(smtpServer, port,context=context) as goiServer:
        goiServer.login(nguoiGui, mk)
        goiServer.sendmail(nguoiGui, nguoiNhan, tinNhan)
        so += 1
        print(f'Gui Thanh Cong! {so} lan')
        
    n -= 1

# after 82 times send, SMTPServerDisconnected with error at line 27