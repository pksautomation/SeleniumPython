class PetData:
    def __init__(self, pet_id, name, status="available", category=None, tags=None, photo_urls=None):
        self.pet_id = pet_id
        self.name = name
        self.status = status
        self.category = category or {"id": 1, "name": "dogs"}
        self.tags = tags or []
        self.photo_urls = photo_urls or ["https://example.com/photo.jpg"]

    def to_payload(self):
        return {
            "id": self.pet_id,
            "name": self.name,
            "status": self.status,
            "category": self.category,
            "tags": self.tags,
            "photoUrls": self.photo_urls,
        }
