# Assignment: 49
# Write a program to define a function which takes IP address as parameter.
# The function will verify if the IP address is valid or not.
# The function has to return True if the IP address is valid otherwise False.
# xxx.xxx.xxx.xxx (<0 to 255>. (<0 to 255>(<0 to 255>(<0 to 255>)
# 126.126.126.126 => True  255.255.255.255
# 300.1.1.1             => False

def validate_ip_addr(ip_addr):
    ip_pts = ip_addr.split(".")
    # First verify if IP address has four parts
    if len(ip_pts) == 4:
        # If yes, check if each part has digits or not
        for ip_pt in ip_pts:
            if ip_pt.isnumeric():
                if not (int(ip_pt) >=0 and int(ip_pt) < 256):
                    break
            else:
                break
        else:
            return True
        # control here means ip address is invalid
        return False
    else:
        return False


ret = validate_ip_addr("123.12.13.123")
if ret:
    print("Given IP address is valid.")
else:
    print("Given IP address is not valid.")
