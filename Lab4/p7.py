import os

def dincvindicti(path):
    dict = {
        "full_path": "",
        "file_size": "",
        "file_extension": "",
        "can_read": "",
        "can_write": ""
    }
    dict.update({"full_path": os.path.abspath(path), "file_size": os.path.getsize(path), "file_extension": os.path.splitext(path)[1][1:], "can_read": os.access(path, os.R_OK), "can_write": os.access(path, os.W_OK)})
    return dict

if __name__=="__main__":
    print(dincvindicti("C:/Users/aursu/Desktop/pitt/ceva.txt"))