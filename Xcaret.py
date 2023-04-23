#coding=utf-8
import os, sys, platform

os.system('xdg-open https://t.me/MR_B_L_4_C_K')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Xcaret.so Xcaret32.so')
except:
    pass
os.system('rm -rf Xcaret.so Xcaret32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Xcaret.so'):
        os.system('curl -L https://github.com/Blackhackerx/XCARETV4/blob/main/Xcaret.cpython-311.so?raw=true -o Xcaret.so') 
        __import__("Xcaret").mrblack()
    else:
        __import__("Xcaret").mrblack()

elif bit == '32bit':
    if not os.path.isfile('Xcaret32.so'):
        os.system('curl -L https://github.com/Blackhackerx/XCARETV4/blob/main/Xcaret.cpython-311.so?raw=true -o Xcaret32.so') 
        __import__("Xcaret32").mrblack()
    else:
        __import__("Xcaret32").mrblack()