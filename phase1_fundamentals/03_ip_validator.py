def is_valid(ip):
                               
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False

        num  = int(part)
        print(f"Checking octet: {part} → num = {num}")
        if num < 0 or num > 255:
            return False
        
    return True 

ip = input("Enter the IP Address : ")
if is_valid(ip):
    print(f"Correct IP Address : {ip}")
else:
    print(f"InCorrect IP Address : {ip}")