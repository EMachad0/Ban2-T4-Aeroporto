from app.models import Aviao


def get_all():
    return Aviao.objects


def insert(**kwargs):
    Aviao(**kwargs).save()
