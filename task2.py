import re
def findemail(file):
    f = open(file)
    str = f.read()
    f.close()
    mail = re.findall(r'[\w.-]+@[\w.-]+\.?[\w]+?', str)
    print(mail)
findemail('tut.txt')