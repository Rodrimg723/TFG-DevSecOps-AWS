import urllib.request
import threading

def attack():
    for i in range(100):
        try:
            req = urllib.request.Request(f"http://34.230.92.122/admin_panel_test_{i}.php", headers={'User-Agent': 'Nikto/2.1.6'})
            urllib.request.urlopen(req, timeout=2)
        except Exception:
            pass

threads = []
for _ in range(25):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Attack finished")
