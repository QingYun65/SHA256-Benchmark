# SHA256-Benchmark
主要测试单线程1s内大概能够进行多少次SHA-256  

基于pycryptodome、hashlib库 
测试思路：随机生成50000个128Byte的数据并进行Hash，求平均值，计算1s内Hash次数
