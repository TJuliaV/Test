import requests
import json

from requests.auth import HTTPBasicAuth

class OVIntegration(object):

    def __init__(self, url="", userName="", password="", trackorType="", trackorKey="", processId=""):

        if url != None and userName != None and password != None and trackorType != None and trackorKey != None and processId != None:
            self.processId = processId
            self.url = url
            self.auth = HTTPBasicAuth(userName, password)
            self.trackorType = trackorType
            self.trackorKey = trackorKey
            self.headers = {'Content-type':'application/json','Content-Encoding':'utf-8'}
            self.start_integration()

    def start_integration(self):

        self.trackorId = ""
        allTrackor = self.search_trackor()

        for trackor in allTrackor:
            self.trackorId = trackor['TRACKOR_ID']

        if self.trackorId == "":
            self.trackorId = self.add_trackor()
            self.add_log("test-integration: trackor created", "test-integration: trackor with trackor_key '" + str(self.trackorKey) + "' created", "Info")
        else:
            self.add_log("test-integration: trackor found", "test-integration: trackor with trackor_key '" + str(self.trackorKey) + "' found", "Info")


    def search_trackor(self):
        try:
            url = self.url + "/api/v3/trackor_types/" + str(self.trackorType) + "/trackors?Trackor_key=%22" + str(self.trackorKey) + "%22"
            answer = requests.get(url, headers=self.headers, auth=self.auth)
            response = answer.json()
            return response
        except Exception as e:
            return ""

    def add_trackor(self):
        url = self.url + "/api/v3/trackor_types/" + str(self.trackorType) + "/trackors"
        data = {
            "fields": {
                "TRACKOR_KEY": str(self.trackorKey)
            }
        }
        answer = requests.post(url, headers=self.headers, data=json.dumps(data), auth=self.auth)
        response = answer.json()
        return response['TRACKOR_ID']

    def add_log(self, message, description, log_level_name):
        url = self.url + "/api/v3/integrations/runs/logs/" + str(self.processId) + "/logs"
        data = {
            "message": message,
            "description": description,
            "log_level_name": log_level_name
        }
        requests.post(url, headers=self.headers, data=json.dumps(data), auth=self.auth)
