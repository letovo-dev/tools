from basic_server import BasicServer

check_list = {
    "home_pc": BasicServer(ip="192.168.2.15", ping=True, name="home pc", log=False),
    "letovo_secrets_server": BasicServer(ip="91.203.232.173", port=5001, get=True, name="secrets server"), 
    "letovo_wiki_server": BasicServer(ip="91.203.232.173", get=True, name="wiki")
} 
    
