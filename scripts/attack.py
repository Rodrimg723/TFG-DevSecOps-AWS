import sys
import urllib.request
import threading

def attack(target_host, target_ip):
    for i in range(100):
        try:
            # Simulamos peticiones maliciosas con User-Agent de Nikto
            url = f"http://{target_ip}/dvwa/login.php?p={i}"
            req = urllib.request.Request(url)
            req.add_header('Host', target_host)
            req.add_header('User-Agent', 'Nikto/2.1.6')
            urllib.request.urlopen(req, timeout=2)
        except Exception:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python attack.py <IP_PUBLICA> [HOST_NIP_IO]")
        sys.exit(1)
        
    ip = sys.argv[1]
    host = sys.argv[2] if len(sys.argv) > 2 else f"{ip}.nip.io"
    
    print(f"Iniciando escaneo simulado contra {ip} (Host: {host})...")
    threads = []
    for _ in range(30):
        t = threading.Thread(target=attack, args=(host, ip))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        
    print("Ataque de prueba finalizado. Comprueba si tu IP ha sido bloqueada (HTTP 403) o revisa Grafana.")
