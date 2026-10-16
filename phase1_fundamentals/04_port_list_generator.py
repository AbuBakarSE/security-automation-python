ports = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP",
    445: "SMB"
}

for key, value in ports.items():
    print(f"{key} : {value}")
