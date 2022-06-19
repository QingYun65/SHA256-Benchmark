from Crypto.Hash import SHA256
import time,os
import hashlib

def digest(data):
    # 填充
    pad_num = 64 - (len(data) + 1 & 0x3f)
    data += b'\x80' + (len(data) << 3).to_bytes(pad_num if pad_num >= 8 else pad_num + 64, 'big')
    V, B = V0, array('L', data)
    B.byteswap()
    # 迭代压缩
    for i in range(0, len(B), 16):
        V = CF(V, B[i:i+16])
    V = array('L', V)
    V.byteswap()
    return V.tobytes()

def SHA_256_test():
    print('SHA-256 benchmark测试：')
    long_data=os.urandom(128)
    print("消息长度 %d B 单位:微秒"%(len(long_data)))
    time_1=time.perf_counter()
    SHA256.new(long_data).digest()
    time_2=time.perf_counter()
    print("Crypto-SHA256\t",(time_2-time_1)*1000000)

def SHA_256_test1():
    print('SHA-256 benchmark测试：')
    count=10000
    long_data=[os.urandom(128) for i in range (count)]
    print("消息长度 128 B                   单位:微秒")
    time_1=time.perf_counter()
    for i in range(count):
        SHA256.new(long_data[i]).digest()
    time_2=time.perf_counter()
    avg_time=(time_2-time_1)*1000000/count
    print("Crypto-SHA_256平均hash时间\t",avg_time)
    print("1s 能够进行%d次SHA-256"%(1000000/avg_time))

def SHA_256_test2():
    count=10000
    long_data=[os.urandom(128) for i in range (count)]
    print("消息长度 128 B                   单位:微秒")
    time_1=time.perf_counter()
    for i in range(count):
        hashlib.sha256(long_data[i])
    time_2=time.perf_counter()
    avg_time=(time_2-time_1)*1000000/count
    print("Crypto-SHA_256平均hash时间\t",avg_time)
    print("1s 能够进行%d次SHA-256"%(1000000/avg_time))

if __name__=="__main__":
    SHA_256_test1()
    SHA_256_test2()
