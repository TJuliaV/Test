# test-integration
Test Integration searches for Trackor by Trackor Type and Trackor Key specified in the settings file. 
If the Trackor is not found - creates a new Trackor.

Integration Test consist of two python files, TestIntegration.py and OVIntegration.py.
OVIntegration.py contains methods for working with API. IntegrationTest.py is python script for executing the integration. 

PasswordFile.json should be in integration directory. PasswordFile.json contains login, password, url, trackorType and trackorKey for 

Integration Test retrieves Process Id from ihub_process_id file for adding logs. ihub_process_id is put into integration directory at each integration run.

## Requirements
- Python 3
- Requests - library for python (http://docs.python-requests.org/en/master/)

## Usage
Create new integration with the following fields: 
- Integration Name: Test Integration
- Command: python3 ./TestIntegration.py
- Repository: https://github.com/ov-integrations/test-integration
- Settings File:  PasswordFile.json

PasswordFile.json

```json
{
  "UserName":"amoiseenko",
  "Password":"***",
  "URL":"http://localhost:8080",
  "TrackorType" : "TrackorType",
  "TrackorKey" : "TrackorKey"
}
```
