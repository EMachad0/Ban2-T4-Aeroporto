from app.models import Tecnico


def get_all():
    return Tecnico.objects


def insert(**kwargs):
    Tecnico(**kwargs).save()

