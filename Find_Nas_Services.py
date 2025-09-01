# =============================================================================
# BUSCADOR DE SERVIDORES NAS - v9.0 (Estable)
# =============================================================================
import socket
import ipaddress
import threading
from queue import Queue
import os
from smbprotocol.connection import Connection
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect

# --- CONFIGURACIÓN ---
USERNAME = "user"
PASSWORD = "1234"
SHARE_NAME = "ConfigServer"
NETWORK = "192.168.101.0/24"
PORT = 445
NUM_THREADS_SCAN = 50  # Hilos para el escaneo rápido de puertos
NUM_THREADS_VERIFY = 10   # Hilos para la verificación SMB

# --- Variables Globales ---
queue = Queue()
open_ports = []

def port_scan(port):
    """Escanea un puerto en una IP de la cola."""
    while not queue.empty():
        ip = queue.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect((str(ip), port))
                print(f"  [+] Puerto {port} abierto en: {ip}")
                open_ports.append(ip)
            except (socket.timeout, ConnectionRefusedError):
                pass
        queue.task_done()

def verify_smb_connection(ip, verified_servers_list):
    """Intenta una conexión SMB completa a una IP."""
    print(f"🔎 Verificando conexión SMB en {ip}...")
    conn, session, tree = None, None, None
    try:
        conn = Connection(os.urandom(16), str(ip), port=PORT)
        conn.connect(timeout=5)
        session = Session(conn, USERNAME, PASSWORD)
        session.connect()
        tree = TreeConnect(session, fr"\\{ip}\{SHARE_NAME}")
        tree.connect()
        
        print(f"  ✅ Conexión SMB exitosa en {ip}.")
        verified_servers_list.append({'ip': str(ip)})

    except Exception as e:
        print(f"  ❌ Fallo la conexión SMB en {ip}. Razón: {e}")
    finally:
        if tree:
            try:
                tree.disconnect()
            except:
                pass
        if session:
            try:
                session.disconnect()
            except:
                pass
        if conn:
            try:
                conn.disconnect()
            except:
                pass

def buscar_servidores():
    """Función principal que orquesta el escaneo y la verificación."""
    print("\n=================")
    print("--- Iniciando Búsqueda de Servidores NAS v9.0 ---")
    
    # --- PASO 1: Escaneo Rápido de Puertos ---
    print(f"\n[1] Escaneando la red {NETWORK} en busca de puertos abiertos...")
    global open_ports
    open_ports = []
    
    try:
        network = ipaddress.IPv4Network(NETWORK)
    except ValueError:
        print(f"  ❌ Rango de red no válido: {NETWORK}")
        return []

    for ip in network.hosts():
        queue.put(ip)
    
    threads = []
    for _ in range(NUM_THREADS_SCAN):
        thread = threading.Thread(target=port_scan, args=(PORT,))
        thread.start()
        threads.append(thread)
    
    queue.join()
    
    print(f"\n  -> Escaneo rápido finalizado. {len(open_ports)} puertos abiertos encontrados.")

    if not open_ports:
        print("\n--- 🏁 Escaneo de Detección Finalizado 🏁 ---")
        print("No se encontraron dispositivos con el puerto 445 abierto.")
        return []

    # --- PASO 2: Verificación de Credenciales SMB ---
    print(f"\n[2] Verificando credenciales en los {len(open_ports)} dispositivos encontrados...")
    verified_servers = []
    
    threads = []
    for ip in open_ports:
        thread = threading.Thread(target=verify_smb_connection, args=(ip, verified_servers))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    print("\n--- 🏁 Escaneo de Detección Finalizado 🏁 ---")
    if verified_servers:
        print(f"Se encontraron {len(verified_servers)} servidores potenciales listos para ser analizados por el gestor:")
        for server in verified_servers:
            print(f"  - IP: {server['ip']}")
    else:
        print("No se pudo autenticar en ninguno de los dispositivos encontrados.")
        
    return verified_servers

if __name__ == '__main__':
    buscar_servidores()
