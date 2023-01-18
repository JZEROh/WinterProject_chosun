from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES
import base64

def encrypt(ori,key):
    #패딩값
    BS = 16
    
    # 사이퍼에 키값 적용
    cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)
    # 패딩 길이를 바탕으로 암호화
    msg = cipher.encrypt(pad(ori.encode(), BS))
    # 인터넷 통신을 위한 BASE64 인코딩
    # 아스키 코드값은 7bit 엔코딩이기 때문에 1비트 처리방식이 달라서 여러가지 문제 발생
    # 우리는 인터넷 통신 안할꺼라 없어도됨
    crypt = base64.b64encode(msg)
    
    # json 형식 맞추기 위해 binary to utf
    crypt = crypt.decode('utf-8')
    return crypt

def decrypt(b64Crypt,key):
    #패딩값
    BS = 16
    cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)
    
    #BASE64 디코딩
    crypt = base64.b64decode(b64Crypt)
    
    # 사이퍼값으로 복호화
    decrypt = unpad(cipher.decrypt(crypt),BS)
    
    #binary 값에서 string 으로 변환
    decrypt = decrypt.decode('utf-8')
    return decrypt
