import os
def changedir():
    req_path=input("Enter the path to change the working dir: ")
    print("current working directory : ", os.getcwd())
    try:
        os.chdir(req_path)
        print("new working directory :" ,os.getcwd())
    except NotADirectoryError:
        print("Enter a valid Directory")
    except FileNotFoundError:
        print("The system cannot find the file specified")
    except Exception as e:
        print(e)
if __name__=="__main__":
    changedir()
    