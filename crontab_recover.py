# Set which user's crontab do you wanna restore
usr = "ubuntu"

crontab = []

for line in open('crontab_log.txt', 'r'):
    if "({}) CMD".format(usr) in line:
        a,b,c = line.split("(")
        cmd = c[:-2]    # Remove last ) and \n

        hour = line.split(" ")
        h,m,s = hour[2].split(":")
        
        crontab.append("{0} {1} * * * {2}".format(m,h,cmd)) #Append Time and Command
        
crontab_cmd = set(crontab)   # Remove duplicates

with open("recovered_crontab.txt","w") as f:
    for item in crontab_cmd:
        f.write("%s\n" % item)