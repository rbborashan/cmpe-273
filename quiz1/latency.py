"""
    Ryan Borashan
    CMPE 273
    2/2/16
"""
import subprocess

hosts=[["us-east-1",      "54.84.0.3",    0.0],
       ["us-east-2",      "52.15.55.0",   0.0],
       ["us-west-1",      "54.151.0.2",   0.0],
       ["us-west-2",      "52.88.0.2",    0.0],
       ["us-gov-west-1",  "52.222.9.163", 0.0],
       ["ca-central-1",   "52.60.50.0",   0.0],
       ["eu-west-1",      "52.19.0.2",    0.0],
       ["eu-central-1",   "54.93.32.2",   0.0],
       ["eu-west-2",      "52.56.34.0",   0.0],
       ["ap-northeast-1", "54.64.0.2",    0.0],
       ["ap-northeast-2", "52.79.52.64",  0.0],
       ["ap-southeast-1", "52.76.0.2",    0.0],
       ["ap-southeast-2", "54.66.0.2",    0.0],
       ["ap-south-1",     "52.66.66.2",   0.0],
       ["sa-east-1",      "54.240.16.0",  0.0]];

for i in range(0, 15):

    cmd = "ping -c 3 " + hosts[i][1] + "| tail -1 | awk -F \'/\' \'{print $5}\'";

    ping = subprocess.Popen(
        cmd, shell=True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = ping.communicate()

    hosts[i][2] = float(out);

hosts.sort(key = lambda lis: lis[2])

for i in range(0, 15):

    print str(i+1) + ". " + hosts[i][0] + " [" + hosts[i][1] + "] - " + str(hosts[i][2])
