import smtplib, ssl


smtpServer = 'smtp.gmail.com'
port = 465

nguoiGui = 'hoadambutxinh@gmail.com'
matKhau = input('Mat Khau: ')
context = ssl.create_default_context()

nguoiNhan = input('Gui cho: ')
chuDe = input('Chu De: ')
noidung = input('Tin Nhan: ')

tinNhan = """Subject: {}
To: {}
{}
 """.format(chuDe, nguoiNhan, noidung)

with smtplib.SMTP_SSL(smtpServer, port,context=context) as goiServer:
    goiServer.login(nguoiGui, matKhau)
    goiServer.sendmail(nguoiGui, nguoiNhan, tinNhan)
    print('Gui Thanh Cong! <--(*_*)-->')
