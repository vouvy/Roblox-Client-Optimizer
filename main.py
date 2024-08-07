import subprocess
def ping_test(host, packet_size):
    try:
        result = subprocess.run(
            ["ping", host, "-f", "-l", str(packet_size)],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout
        if "Packet needs to be fragmented but DF set" in output:
            return False
        return True
    except subprocess.TimeoutExpired:
        return False
def find_optimal_mtu(host):
    max_mtu = 1472
    min_mtu = 1000
    optimal_mtu = min_mtu
    for mtu in range(max_mtu, min_mtu, -1):
        if ping_test(host, mtu):
            optimal_mtu = mtu
            break
    return optimal_mtu
if __name__ == "__main__":
    host = "roblox.com"
    optimal_mtu = find_optimal_mtu(host)
    print(f"The optimal MTU size is: {optimal_mtu} bytes")