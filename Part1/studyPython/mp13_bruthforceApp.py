# 암호해제 앱 (무차별 대입공격)
import itertools
import time
import zipfile

passqd_string = '0123456789' # 패스워드에 영문자도 들어있으면
# passqd_string = '0123456789abcdefghijk....xyzABCDEF....XYZ'

file = zipfile.ZipFile('./studyPython/password.zip')
isFind = False # 암호를 찾았는지

for i in range(4, 5):
    attempts = itertools.product(passqd_string, repeat=i)
    for attempt in attempts:
        try_pass = ''.join(attempt)
        print(try_pass)
        # time.sleep(0.05)
        try:
            file.extractall(pwd=try_pass.encode(encoding='utf-8'))
            print(f'암호는 {try_pass} 입니다.')
            isFind = True; break
        except:
            pass

    if isFind == True: break
