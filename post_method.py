import requests

head = {"Accept": "text/plan", "Content-Type": "application/json"}

response_payload = {
  "id": 101,
  "title": "Pytest ",
  "dueDate": "2025-01-14T05:40:46.645Z",
  "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",
                         headers=head, json=response_payload)

print(response.status_code)
print(response.json())

assert response.status_code == 200