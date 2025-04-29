import rsa
import hashlib
(public_key, private_key) = rsa.newkeys(2048)
message = '40478945691084'
message_hash = hashlib.sha256(message.encode()).digest()
signature = rsa.sign(message_hash, private_key, 'SHA-256')
try:
    rsa.verify(message_hash, signature, public_key)
    print("签名验证成功")
except rsa.VerificationError:
    print("签名验证失败")
