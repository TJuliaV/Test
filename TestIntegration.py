import OVIntegration
import json

with open('PasswordFile.json', "rb") as PFile:
    passwordData = json.loads(PFile.read().decode('utf-8'))

user = passwordData["UserName"]
password = passwordData["Password"]
site = passwordData["URL"]
trackorType = passwordData["TrackorType"]
trackorKey = passwordData["TrackorKey"]

with open('ihub_process_id', "rb") as PFile:
    processId = PFile.read().decode('utf-8')

integrationOV = OVIntegration.OVIntegration(url=site, userName=user, password=password, trackorType=trackorType, trackorKey=trackorKey, processId = processId)
