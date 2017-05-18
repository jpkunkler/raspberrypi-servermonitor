import ts3
from config import TS3_HOST, TS3_ADMIN, TS3_PW, TS3_QUERY_PORT

def ts3Status():
    try:
        conn = ts3.TS3Server(TS3_HOST, TS3_QUERY_PORT)
        conn.login(TS3_ADMIN, TS3_PW)
    except:
        print 'Connection Error'
        return False
    else:
        servers = conn.send_command("serverlist").data
        try:
            ids = []
            for server in servers:
                server['virtualserver_status'] == 'online'
        except:
            return False
        else:
            return True

def ts3Clients():
    try:
        conn = ts3.TS3Server(TS3_HOST, TS3_QUERY_PORT)
        conn.login(TS3_ADMIN, TS3_PW)
    except:
        return False
    else:
        servers = conn.send_command('serverlist').data
        ids = []
        for server in servers:
            sid = server['virtualserver_id']
            ids.append(sid)
        count = 0
        for id in ids:
            conn.use(id)
            clients = conn.send_command('clientlist').data
            count -= 1
            for client in clients:
                count += 1
        return count
