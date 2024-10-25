import subprocess
import re


def ping_latency(host, n=10):
    """
    This function pings the host `n` times and returns the average latency in milliseconds.

    :param host: str - Hostname or IP address to ping
    :param n: int - Number of pings
    :return: float - Average latency in milliseconds
    """
    # Define the ping command based on OS type
    command = ["ping", "-c", str(n), host]

    try:
        # Execute the ping command and capture the output
        output = subprocess.check_output(command, universal_newlines=True)

        # Use regex to find all latency values in the output
        latencies = re.findall(r'time=(\d+\.\d+)', output)
        latencies = [float(latency) for latency in latencies]

        # Calculate the average latency
        average_latency = sum(latencies) / len(latencies) if latencies else None
        return average_latency

    except subprocess.CalledProcessError as e:
        print(f"Ping failed: {e}")
        return None


if __name__ == '__main__':
    average_latency = ping_latency('google.com')
    print(f"Average Latency of 10 pings: {average_latency} ms")

    average_latency = ping_latency('google.com', n=3)
    print(f"Average Latency of 3 pings: {average_latency} ms")
