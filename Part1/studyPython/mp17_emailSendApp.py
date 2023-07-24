# 이메일 보내기 앱
# 메일에서는 SMTP 사용
import smtplib # Simple Mail Transfer Protocol 메일 전송 프로토콜
from email.mime.text import MIMEText # Multipurpose Internet Mail Extensions

send_email = 'sta97@naver.com'
send_pass = ''
# 2단계 인증 걸어놓으면 전송X

recv_email = 'sta9007@gmail.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587 # 포트번호

text = '''메일 내용입니다. 긴급입니다.
조심하세요. 빨리 연락주세요!'''

msg = MIMEText(text)
msg['Subject'] = '메일 제목입니다'
msg['From'] = send_email # 보내는 메일
msg['To'] = recv_email # 받는 메일
print(msg.as_string())

mail = smtplib.SMTP(smtp_name, smtp_port) # SMTP 객체생성
mail.starttls() # 전송계층 보안시작
mail.login(send_email, send_pass)
mail.sendmail(send_email, recv_email, msg=msg.as_string())
mail.quit()
print('전송완료!')