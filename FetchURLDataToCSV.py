import csv
import requests

def fecthBuildCsv(url):
    #URL testing and data stracting and formating
    response = requests.get(url, timeout=10)
    responseText = response.text.splitlines()

    #Create the CSV file
    with open('tor.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ')

        for line in responseText:
            writer.writerow(line)
        
if __name__=="__main__":
    url = "https://www.dan.me.uk/torlist/?exit"
    fecthBuildCsv(url)

