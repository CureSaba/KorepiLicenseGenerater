import generator 
import argparse

parser = argparse.ArgumentParser(description="Generate a license txt file from the excel file containing the key")

parser.add_argument('FileName', help='This is the name of the excel file, by default it is set to a.xlsx', default="a.xlsx")
parser.add_argument('-i', '--install', default=None, help="Install dependencies using pip, please specify only for the first time")

args = parser.parse_args()
if args.install is not None:
    import subprocess
    try:
        subprocess.check_call('python3 -m pip install -r requirments.txt', shell=True)
    except:
        print("pip install failed")
ins=generator(args.FileName)
ins.main()