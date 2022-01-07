import time

from core import AstroApi

archived_count = len(AstroApi.get_archived_ports())
status = f'ОБНОВИТЬ АРХИВ ({archived_count} шт.)'
