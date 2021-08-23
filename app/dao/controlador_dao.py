from app.models import Controlador


def get_all():
    return Controlador.objects


def insert(**kwargs):
    Controlador(kwargs).save()
