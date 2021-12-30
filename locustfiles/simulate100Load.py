import logging
import random
from locust import HttpUser, between, tag, task

#Defining the class name
class MHUser(HttpUser):
    #Defining the wait time of 5-10 secs( Applied only on task)
    wait_time = between(5, 10)
    #Using the on_start method to get the list values before test executio
    #Defining the tag name for the API
    @tag("TAG NAME ", "heavy")
    #Defininig the task
    @task(1)
    def simulate_MessageHandler(self):
        #Using with to validate the response
        with self.client.get("END POINTS",
                              json=
                              {"query": random.choice(self.messageHandler)}
                , catch_response=True) as response:
                #Assertion for the status code
                assert response.status_code is 200 , "Unexpected response code:"+str(response.status_code)
                assert response.json['error'] is 'Fail'