from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Tiempo de espera aleatorio entre cada petición por usuario (entre 1 y 3 segundos)
    wait_time = between(1, 3)

    @task(3)
    def view_homepage(self):
        # Simula una petición GET a la página principal de prueba
        self.client.get("/")

    @task(1)
    def view_api_endpoint(self):
        # Simula una petición GET a un endpoint de API de prueba
        self.client.get("/api/users?page=2")