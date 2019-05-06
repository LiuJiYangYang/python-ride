# 键值对         字典     dict

# Jan->January
# Mar->March

monthConversions={
    "Jan":"January",      # 0:"January"
    "Feb":"February",     # 1:"February"
    "Mar":"March",        # 2:"March"
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
# print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Nvc"))    # None
print(monthConversions.get("Luv","Not a valid Key"))    # 没有返回Not a valid Key














