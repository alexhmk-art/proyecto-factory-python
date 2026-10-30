from .base import Notificacion


class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"Enviando Email a {destinatario}: {mensaje}")


class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"Enviando SMS a {destinatario}: {mensaje}")


class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"Enviando Push a {destinatario}: {mensaje}")


class NotificacionWhatsApp(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"Enviando WhatsApp a {destinatario}: {mensaje}")