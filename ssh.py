import paramiko
from config import HOSTNAME, SSH_PORT

def sshStatus(user, pw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    try:
        ssh.connect(HOSTNAME, SSH_PORT, username=user, password=pw)
    except:
        return False
    else:
        return True

def RamFree(user, pw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    try:
        ssh.connect(HOSTNAME, SSH_PORT, username=user, password=pw)
    except:
        return 'NA'
    else:
        cmd = "free | awk '/buffers\/cache/{print $4/($3+$4) * 100.0;}'"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        output = stdout.readlines()
        return float(output[0])

def cpuUsage(user, pw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    try:
        ssh.connect(HOSTNAME, SSH_PORT, username=user, password=pw)
    except:
        return 'NA'
    else:
        cmd = "top -b -n 10 -d.2 | grep 'Cpu' |  awk 'NR==3{ print($2)}'"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        output = stdout.readlines()
        return float(output[0])
