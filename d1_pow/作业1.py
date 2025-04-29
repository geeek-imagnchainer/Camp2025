import hashlib
import time
start_time=time.time()
nicheng="404789456"
nonce=0
proof_of_work=0

while(proof_of_work==0):
    nonce+=1
    nonce_string=str(nonce)
    if hashlib.sha256((nonce_string+nicheng).encode()).hexdigest()[0:4]=="0000":
        proof_of_work=1
print("哈希值是",hashlib.sha256((nonce_string+nicheng).encode()).hexdigest())
print("哈希内容是",nonce_string+nicheng)
end_time=time.time()
print("运行时间：", end_time - start_time, "秒")