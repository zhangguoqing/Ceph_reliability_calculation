# Ceph_reliability_calculation
Ceph存储可靠性的计算（几个9？）

按照文章[1]中的公式所写的简单计算Ceph集群可靠性的python代码，可根据实际的Ceph部署架构情况调整程序参数及变量来评估可靠性。
[1]  http://blog.csdn.net/xiaoquqi/article/details/43055031#0-tsina-1-70142-397232819ff9a47a7b7e80a40613cfe1
[2]  https://www.oschina.net/question/12_223909

sudo pip install numpy scipy
python crc.py

不太确定是否正确的值：M = comb(rack, R) * math.pow(osd_each_rack, R)
根据论文中的定义，Copyset is a set that stores all of the copies of a chunk.在Ceph环境中一般每个副本（总共3个副本）都位于不同的rack上，故Copyset总数M应为comb(rack, R) * math.pow(osd_each_rack, R)，这样计算不知是否正确。
