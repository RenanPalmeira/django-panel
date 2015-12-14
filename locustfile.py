from __future__ import unicode_literals

from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def api(self):
        self.client.get("/api/")

class WebsiteUser(HttpLocust):
	host = "http://127.0.0.1:8000/en"
	task_set = UserBehavior
	min_wait=5000
	max_wait=9000