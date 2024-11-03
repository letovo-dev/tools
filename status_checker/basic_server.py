import subprocess
import requests
from logger import get_logger

logger = get_logger(__name__)

class BasicServer():
    def __init__(self, ip: str, name: str, port: int = 80,url: str = "/", ping: bool = False, get: bool = False, expected_rest_status: int = 200, log: bool = True, protocol: str = "http://"):
        self.ip = ip
        self.log = True
        self.port = port
        self.name = name
        self.should_ping = ping
        self.should_get = get
        self.expected_rest_status = expected_rest_status
        self.url = url
        self.protocol = protocol
        self.state = False
            
    def ping(self) -> bool:
        try:
            subprocess.check_output(["ping", "-c", "1", self.ip])
            return True                      
        except subprocess.CalledProcessError:
            logger.warn(f"cant ping {self.name}")
            return False    
    
    def get(self) -> bool:
        req = requests.get(f"{self.protocol}{self.ip}:{self.port}{self.url}")
        if req.status_code != self.expected_rest_status:
            logger.warn(f"cant get from {self.name}, status = {req.status_code}, req = {self.protocol}{self.ip}:{self.port}{self.url}")
        return req.status_code == self.expected_rest_status
        
    def check(self) -> bool:
        state = True
        if self.should_ping:
            state *= self.ping()
        if self.should_get:
            state *= self.get()
        self.state = state
        if not state and self.log: 
            logger.error(f"{self.name} is down")
        
        return self.state     