import requests
import json
from datetime import datetime

class apiHandler:
    
    #--Function that will make GET calls, takes the variable 'code'. When calling this function pass an integer value for code. i.e: apiGet(100)
    def apiGet(code): 
        url = "https://jsonplaceholder.typicode.com/todos/" + str(code) #this is a  string, then we parse the variable code from int to str so we can concat both strings
        apiResponse = requests.get(url) #makes the call and saves the response into the apiResponse object

    #STEP 1
        if code == 99:
            apiResponse = apiResponse.json()["title"]
            return apiResponse
            #print ("Title for code "+ str(code) + " is: '"+ titleGet +"'")
    #STEP 2    
        elif code == 100:
            #STEP 2.a
            timestamp=datetime.now() #getting the current time
            timestamp=timestamp.strftime("%d/%m/%Y %H:%M:%S ").strip()#giving the desired format, then removing empty spaces with strip()
            apiResponse=apiResponse.text #inserting the text of the response into a variable
            apiResponse=apiResponse[:1]+"\n"+"  "+'"time": '+'\"'+timestamp+'\",'+apiResponse[1:] #Giving json object some format and inserting the timestamp into it
            return apiResponse

        else:
            apiResponse = apiResponse.json()["title"]
            #print ("Title for code "+ str(code) + " is: '"+ titleGet +"'")
            return apiResponse
                    
        

    #STEP 3
    def apiPost():
        url = "https://jsonplaceholder.typicode.com/posts"
        #STEP 3.a, 3.b and 3.c
        posting = {"userId":500, "title":"Security Interview Post", "body":"This is an insertion with a known API"} #This is the object we will pass to the requests.post method 
        postResponse = requests.post('https://jsonplaceholder.typicode.com/posts',data=posting)
        #STEP 4
        apiResponse = '('+str(postResponse.json()["id"]) +','+ str(postResponse.status_code)+',"'+postResponse.headers["X-Powered-By"]+'")'
        #STEP 5
        return apiResponse

    #STEP 6
    def apiDelete(deleteId):
        url = "https://jsonplaceholder.typicode.com/posts/"+str(deleteId)
        delStatus=requests.delete(url)
        apiResponse = "Delete Status: "+str(delStatus.status_code)+", X-Content-Type-Options: "+delStatus.headers["X-Content-Type-Options"]
        return apiResponse








    

