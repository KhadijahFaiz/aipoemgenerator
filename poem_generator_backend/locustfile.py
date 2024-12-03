from locust import HttpUser, task, between

# Ensure Locust is installed in your environment
# Run: pip install locust

class PoemGeneratorUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests (1 to 3 seconds)

    @task
    def generate_poem(self):
        self.client.post("/api/generate-poem", json={
            "theme": "love",
            "style": "sonnet",
            "emotion": "happy"
        })
