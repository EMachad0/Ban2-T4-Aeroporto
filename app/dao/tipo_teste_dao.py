from app.models import TipoTeste


def get_all():
    return TipoTeste.objects


def insert(**kwargs):
    TipoTeste(**kwargs).save()
