from django.apps import AppConfig


class ChequeConfig(AppConfig):
    name = 'cheque'

    def ready(self):
        import cheque.signals
