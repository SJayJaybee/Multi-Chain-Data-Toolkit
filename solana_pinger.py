import requests
import time
import json

print("[*] SYSTEM BOOT: Solana Network Speed Tester v1.0")
print("[*] Authenticated Developer: SJayJaybee")
print("-" * 50)

# We define the target endpoints (The client will watch you switch these live)
ENDPOINTS = {
    "Mainnet": "https://api.mainnet-beta.solana.com",
    "Devnet": "https://api.devnet.solana.com"
}

def ping_solana(network, url, iterations=5):
    print(f"[*] Target Lock: Solana {network} ({url})")
    print(f"[*] Initiating JSON-RPC handshake sequence...\n")
    time.sleep(1)

    # The exact payload required to ask the blockchain for its latest block
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getLatestBlockhash"
    })

    total_time = 0

    for i in range(iterations):
        try:
            # Start the stopwatch
            start_time = time.time()
            
            # Fire the payload at the blockchain
            response = requests.post(url, headers=headers, data=payload)
            
            # Stop the stopwatch
            end_time = time.time()
            
            if response.status_code == 200:
                # Calculate latency in milliseconds
                latency = int((end_time - start_time) * 1000)
                total_time += latency
                print(f"  [>] Ping {i+1}/5: Packet delivered. Finality speed: {latency}ms")
            else:
                print(f"  [!] Ping {i+1}/5: FAILED (Node Rate Limited)")
                
        except Exception as e:
             print(f"  [!] Ping {i+1}/5: CRITICAL CONNECTION ERROR")
        
        # Pause slightly between pings so the terminal output looks readable and dramatic
        time.sleep(0.8)

    # Calculate and display the final average
    avg_latency = total_time // iterations
    print("-" * 50)
    print(f"[*] DIAGNOSTIC COMPLETE")
    print(f"[*] Average Network Latency: {avg_latency}ms")
    
    if avg_latency < 600:
        print("[*] Status: OPTIMAL (Network is flying)")
    elif avg_latency < 1500:
        print("[*] Status: DEGRADED (Standard congestion)")
    else:
        print("[*] Status: CRITICAL (Heavy chain lag detected)")
    print("-" * 50)

def main():
    # ---------------------------------------------------------
    # THE LIVE TWEAK: Change "Mainnet" to "Devnet" while recording
    # ---------------------------------------------------------
    TARGET_NETWORK = "Mainnet" 
    
    url = ENDPOINTS.get(TARGET_NETWORK)
    ping_solana(TARGET_NETWORK, url)

if __name__ == "__main__":
    main()
