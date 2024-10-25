
def ping_latency(host, n=10):
    """
    This function takes a hostname or IP address as input,
    performs `n` ping commands, and returns the latency average.

    You can assume that the host parameter is a valid hostname or IP address.

    Hint:
    Import and use python builtin subprocess module

    :param host: str - Hostname or IP address to ping
    :return: float - Average latency in milliseconds
    """
    return None


if __name__ == '__main__':
    average_latency = ping_latency('google.com')
    print(f"Average Latency of 10 pings: {average_latency} ms")

    average_latency = ping_latency('google.com', n=3)
    print(f"Average Latency of 3 pings: {average_latency} ms")
