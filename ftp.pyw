form ftblib import FTP #import FTP protocal from ftblib

ftp=FTP("domainname")
ftp.login(user="username",passwd="password")
ftp.cwd("/specficdomain-or-location/")


def grapFile():
    filename="fileName.txt"
    localfile= open(filename,"wb")#
    ftp.retrbinary("RETR" + filename,localfile.write,1024)#retervive filename with localfile
    # spedd of file
    ftp.quit()
    localfile.close()# to close actual file

def placeFile():
    filename="fileName.txt"
    ftp.storbinary("STOR" +filename, open(filename,"rb"))
    ftp.quit()
