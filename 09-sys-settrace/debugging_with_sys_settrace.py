import socket

# Enable this for debugging exceptions
import sys


def trace_exceptions(frame, event, arg):
    if event == "exception":
        exc_type, exc_value, exc_traceback = arg
        file_path = frame.f_code.co_filename

        if "debugging_with_sys_settrace" in file_path:
            print(f"Exception caught: {exc_type.__name__}: {exc_value}")
            print(f"  File: {frame.f_code.co_filename}")
            print(f"  Function: {frame.f_code.co_name}")
            print(f"  Line: {frame.f_lineno}")

    return trace_exceptions


sys.settrace(trace_exceptions)


def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        # silently swallow exception
        return None


def get_service_ip(hostname):
    return resolve_hostname(hostname)


def fetch_data(hostname):
    ip = get_service_ip(hostname)
    # silently continue even if ip is None
    return {"ip": ip, "data": [1, 2, 3]}


def aggregate_info(hostnames):
    results = []
    for host in hostnames:
        info = fetch_data(host)
        results.append(info)
    return results


servers = ["example.com", "nonexistent.domain", "python.org"]
server_info = aggregate_info(servers)

# subtle failure here: expecting ip to be a string
for info in server_info:
    # Wrong str here...
    ip = str(info["ip"])
    # fails silently until this line
    octets = ip.split(".")
    print(f"{ip} first octet: {octets[0]}")
