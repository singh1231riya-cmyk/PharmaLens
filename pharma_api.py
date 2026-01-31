import requests

class PharmaAPI:
    def __init__(self, limit=10):
        self.url = "https://api.fda.gov/drug/event.json"
        self.limit = limit

    def fetch_top_adverse(self):
        response = requests.get(f"{self.url}?limit={self.limit}")
        if response.status_code != 200:
            print("API error")
            return

        data = response.json()
        print("\nTop drugs from OpenFDA:")
        for item in data.get("results", []):
            try:
                drug = item["patient"]["drug"][0]["medicinalproduct"]
                reactions = len(item["patient"]["reaction"])
                print(f"{drug}: {reactions} reactions")
            except KeyError:
                continue