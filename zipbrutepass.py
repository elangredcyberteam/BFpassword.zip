# code by ?
import zipfile
zip = raw_input("masukan nama zip: ")
passfile = raw_input("masukan list pass: ")
zfile = zipfile.ZipFile(zip)
passfile = open(passfile, "r")
for password in passfile.readlines():
    password = password.strip("\n").strip("\r")
    try:
        zfile.extractall(pwd=password)
        print (" password di temukan [ " + password + " ] ")
    except Exception, e:
       print ("mencoba : " + password +'')
