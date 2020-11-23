import requests
import re

#Download page
response = requests.get(url)
response.raise_for_status() #if error it will stop the program

#Search for package's status
status = re.search(r'(<td width="100%" colspan="3" style="color: darkorange; font-size: 17px;"><center><b>)(.*)(</b></center></td>)', response.text)
print(status[2])
