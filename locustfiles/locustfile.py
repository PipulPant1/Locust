import logging
import random
from locust import HttpUser, between, tag, task

#Defining the class name
class MHUser(HttpUser):
    #Defining the wait time of 5-10 secs( Applied only on task)
    wait_time = between(5, 10)
    #Defining the host base URL
    host = "API BASE URL STRING"
    #Using the on_start method to get the list values before test execution
    def on_start(self):
        self.messageHandler = [
            "Can my employer require me to get vaccinated?",
            "Can my employer force me to come back to work",
            "What does covid czar do?",
            "can my employer cut my salary?",
        ]
    #Defining the tag name for the API
    @tag("TAG NAME", "heavy")
    #Defininig the task
    @task(1)
    def simulate_MessageHandler(self):
        #Using with to validate the response
        with self.client.post("API END POINTS",
                              json=
                              {"query": random.choice(self.messageHandler)}
                , catch_response=True) as response:
                #Assertion for the status code
                assert response.status_code is 200 , "Unexpected response code:"+str(response.status_code)
                assert response.json['error'] is 'Fail'