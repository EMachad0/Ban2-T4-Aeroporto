from app.models import Teste


def get_all():
    return Teste.objects


def insert(**kwargs):
    Teste(**kwargs).save()
