from app.models import Modelo


def insert(**kwargs):
    Modelo(**kwargs).save()
