import firebase_admin
from firebase_admin import credentials, firestore, storage


class FirebaseFactory:
    def __init__(self, settings) -> None:
        self.settings = settings
        self._initialize_credentials()

    def _initialize_credentials(self):
        try:
            self.credential = credentials.Certificate(self.settings)
            firebase_admin.initialize_app(self.credential)
        except Exception as e:
            print(f"Error initializing Firebase credentials: {e}")
            self.credential = None

    @property
    def firestore_client(self):
        if not self.credential:
            raise ValueError("Firebase credentials not initialized")
        return firestore.client()
    
    @property
    def storage_client(self):
        if not self.credential:
            raise ValueError("Firebase credentials not initialized")
        return storage.bucket()