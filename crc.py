# -*- coding: utf-8 -*-
# pip install numpy scipy

import math
import numpy as np
from scipy.special import comb

# Constant Define
# Annualized failure rate
AFR = 0.017
# Hours of in one year
T = 24 * 365
# Number of duplicate
R = 3

# Variable Define
# The total number of OSDs in the ceph cluster.
osd_total_n = 72
# The number of racks in the ceph cluster.
rack  = 3
# The number of nodes in one rack.
each_rack_nodes = 24
# The number of OSDs in one node.
osd_each_node = 1
# The number of OSDs in one rack.
osd_each_rack = each_rack_nodes * osd_each_node

if osd_total_n != rack * osd_each_rack:
    print "OSDs are not right deployed in racks."

# The capacity of each disk(osd) by GB.
each_disk_capacity = 1000
# The usage of each disk(osd).
each_disk_usage = 0.75
# The write rage of each disk(osd) by MB/s.
write_rate = 50

# 1 Failures in Time by AFR.
FIT = AFR / T
# 2 Possibility of OSD #1 Failure.
P1 = 1 - (1 / (np.e**(FIT * osd_total_n * T)))
# Recovery Time by s.
Tr =  (each_disk_capacity * each_disk_usage * 1024) / (write_rate * (osd_each_rack - 1))
# 3 Possibility of OSD #2 Failure during Recovery.
P2 = 1 - (1 / (np.e**(FIT * (osd_total_n - 1) * (Tr / 3600))))
# 4 Possibility of OSD #3 Failure during Recovery.
P3 = 1 - (1 / (np.e**(FIT * (osd_total_n - 2) * (Tr / 3600))))
# 5 Possibility of Arbitrary Replica OSDs Failure.
Pr = P1 * P2 * P3
# Copy Sets
M = math.pow(osd_each_rack, R)
C = comb(osd_total_n, R)
# 6 Possibility of Copy Set Failure.
P = Pr * M / C

Nines = 1 - P
print Nines
