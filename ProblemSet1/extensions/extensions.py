file = input("File name: ").strip().lower()

period = file.rfind(".")
ext = file[period:len(file)]

if period  == -1:
    print ("application/octet-stream")
elif ext== ".bin":
    print ("application/octet-stream")
elif ext == ".jpg":
    print("image/jpeg")
elif ext == ".pdf":
    print("application/pdf ")
elif ext == ".gif":
    print("image/gif")
elif ext == ".jpeg":
    print("image/jpeg")
elif ext == ".png":
    print("image/png")
elif ext == ".txt":
    print("text/plain")
elif ext == ".zip":
    print("application/zip")