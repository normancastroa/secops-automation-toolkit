#Author: Norman Castro A
#Description: Retrieves a json file from a URL and turns it into a  csv


import csv
import requests


#loccaText
localtext = 'oaKUlqUG.txt'

#URL testing and data stracting and formating
url2 = "https://www.cloudflare.com/ips-v4"
url= "https://www.dan.me.uk/torlist/?exit"
response = requests.get(url, timeout=10)
responseText = response.text.splitlines()


print("\nResponse Type:")
print(type(response))
print("\nResponseText Body:")
print(responseText)
print("\nResponseText Type:")
print(type(responseText))

#Create the CSV file
with open('tor.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=' ')

    for line in responseText:
        writer.writerow(line)
        
"""
if __name__=="__main__":
    url = "https://www.dan.me.uk/torlist/?exit"
    scrape_data(url)
"""
