import requests as req
import sys

inp = str(sys.argv[1])
resp = req.get(inp)
new_path = r"C:/Users/Alexey/PycharmProjects/pythonProject/web1.txt"

new_doc = open(new_path,'w')
new_doc.write(resp.text)
new_doc.close()