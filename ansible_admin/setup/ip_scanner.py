import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from ansible_admin.constants import START_IP, END_IP, OUTPUT_FILE

def ping(ip):
    try:
        subprocess.check_output(["ping", "-c", "1", "-W", "1", str(ip)], stderr=subprocess.DEVNULL)
        return str(ip)
    except subprocess.CalledProcessError:
        return None

def scan_ip_range(start_ip, end_ip, output_file):
    ip_range = list(ipaddress.summarize_address_range(
        ipaddress.IPv4Address(start_ip),
        ipaddress.IPv4Address(end_ip)
    ))

    total_ips = sum(network.num_addresses for network in ip_range)
    active_hosts = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for network in ip_range:
            futures.extend([executor.submit(ping, ip) for ip in network])

        with tqdm(total=total_ips, desc="Scanning", unit="IP") as pbar:
            for future in as_completed(futures):
                result = future.result()
                if result:
                    active_hosts.append(result)
                pbar.update(1)

    with open(output_file, "w") as f:
        f.write("[ActiveHosts]\n")
        for ip in active_hosts:
            f.write(f"{ip}\n")

    print(f"\nScan complete. {len(active_hosts)} active hosts found and written to {output_file}")

if __name__ == "__main__":
    scan_ip_range(START_IP, END_IP, OUTPUT_FILE)
