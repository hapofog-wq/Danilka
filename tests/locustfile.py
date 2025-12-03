from locust import HttpUser, task, between
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class OpenBMCUser(HttpUser):
    host = "https://localhost:2443"
    wait_time = between(0.5, 2)

    @task(3)
    def get_root(self):
        self.client.get("/redfish/v1", auth=("root", "0penBmc"), verify=False, name="OpenBMC Root")

    @task(2)
    def get_system_info(self):
        self.client.get("/redfish/v1/Systems", auth=("root", "0penBmc"), verify=False, name="OpenBMC Systems")

    @task(1)
    def get_chassis_info(self):
        self.client.get("/redfish/v1/Chassis", auth=("root", "0penBmc"), verify=False, name="OpenBMC Chassis")

class ExternalAPIUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)

    @task(3)
    def get_posts(self):
        self.client.get("/posts", name="JSONPlaceholder /posts")
    
    @task(2)
    def get_comments(self):
        self.client.get("/comments", name="JSONPlaceholder /comments")
    
    @task(1)
    def get_users(self):
        self.client.get("/users", name="JSONPlaceholder /users")