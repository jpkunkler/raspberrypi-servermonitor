from mcstatus import MinecraftServer as ms
from config import MC_HOST

def mcStatus(ports):
    try:
        for port in ports:
            server = ms(MC_HOST, port)
            server.ping()
    except:
        return False
    else:
        return True

def mcPlayers(ports):
    try:
        count = 0
        for port in ports:
            server = ms(MC_HOST, port)
            status = server.status()
            players = status.players.online
            count += players
    except:
        return 0
    else:
        return count
