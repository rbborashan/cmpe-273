"""
    Ryan Borashan

    CMPE 273

    2/16/17 
"""

import psutil
import collections

processes = []
pids = []

for ps in psutil.net_connections(kind='tcp'):

    if (ps.laddr and ps.raddr):
        pid = str(ps.pid)
        laddr = "%s@%s" % (ps.laddr)
        raddr = "%s@%s" % (ps.raddr)
        status = ps.status
        processes.append((pid, laddr, raddr, status))
        pids.append(pid)

counts = collections.Counter(pids)
sorted_pids = sorted(pids, key=counts.get, reverse=True)

processes.sort(key=lambda (pid, laddr, raddr, status): sorted_pids.index(pid))


print ("\"pid\",\"laddr\",\"raddr\",\"status\"")

for process in processes:
    print ("\"" + process[0] + "\",\"" + process[1] + "\",\""
                + process[2] + "\",\"" + process[3] + "\"")
