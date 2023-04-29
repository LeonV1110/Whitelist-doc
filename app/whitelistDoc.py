import pymysql
import configparser

#Read in config file and set global variables
config = configparser.ConfigParser()
config.read('config.ini')
DATABASEUSER = config['DATABASE']['DATABASE_USERNAME']
DATABASEPSW = config['DATABASE']['DATABASE_PASSWORD']
DATABASEHOST = config['DATABASE']['DATABASE_HOST']
DATABASENAME = config['DATABASE']['DATABASE_NAME']


def connect_database() -> pymysql.connections.Connection:
    connection = pymysql.connect(host=DATABASEHOST, user = DATABASEUSER, password= DATABASEPSW, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, database=DATABASENAME)
    return connection

def excecute_query(sql: str, vars: tuple = None, format: int = 3):
    with connect_database() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, vars)
            if format == 1: result = cursor.fetchone()
            elif format == 2: result = cursor.fetchall()
        connection.commit()
    if format == 3: return
    elif bool(result):
        return result
    else: return

def create_doc():
    f = open("WhitelistDoc.txt", "w")
    
    whitelist_lines = get_whitelist_lines()
    permission_lines = get_permission_lines()
    lines = permission_lines + whitelist_lines

    for line in lines:
        f.write(line)
    f.close
    return

def create_doc_string():
    res = ""
    setuplines = get_setup_lines()
    whitelist_lines = get_whitelist_lines()
    permission_lines = get_permission_lines()
    lines = setuplines + permission_lines + whitelist_lines
    for line in lines:
        res += line
    return res

def create_new_line(steam64ID, TPFID, role):
    line = "Admin=" + str(steam64ID) + ":" + str(role) + " //" + str(TPFID) + " - added by TPFbot \n"
    return line

def get_whitelist_lines():
    sql = "select player.steam64ID, player.TPFID from `player` join `whitelist` on player.TPFID= whitelist.TPFID"
    whitelists = excecute_query(sql, None, 2)
    if whitelists is None: return ""
    lines = []
    for whitelist in whitelists:
        line = create_new_line(whitelist['steam64ID'], whitelist['TPFID'], 'whitelist')
        lines.append(line)
    return lines

def get_permission_lines():
    sql = "select player.steam64ID, player.TPFID, permission.permission from `player` join `permission` on player.TPFID= permission.TPFID order by permission.permission;"
    permissions = excecute_query(sql, None, 2)
    if permissions is None: return ""
    lines = []
    for perm in permissions:
        line = create_new_line(perm['steam64ID'], perm['TPFID'], perm['permission'])
        lines.append(line)
    return lines

def get_setup_lines():
    
    whitelist = "group=whitelist:reserve \n"
    mvp = "group=MVP:reserve \n"
    creator = "group=creator:balance,reserve,teamchange \n"
    admin="group=admin:reserve \n"
    seniorAdmin="group=senior:reserve \n"
    dadmin="group=dadmin:reserve \n"
    junior="group=junior:reserve \n"
    
    return [whitelist, mvp, creator, admin, seniorAdmin, dadmin, junior]