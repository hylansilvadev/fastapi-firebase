from fastapi import FastAPI

from app.core.firebase import FirebaseFactory 

from .core.config import settings

app = FastAPI(**settings.FASTAPI_CONFIG_ARGS)

firebase = FirebaseFactory(settings.FIREBASE_CREDENTIALS)
