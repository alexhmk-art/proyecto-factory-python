from .base import Notificacion
from .servicios import (
    NotificacionEmail,
    NotificacionSMS,
    NotificacionPush,
    NotificacionWhatsApp
)


class NotificacionFactory:

    @staticmethod
    def crear_notificacion(canal: str) -> Notificacion:
        if canal == "email":
            return NotificacionEmail()
        elif canal == "sms":
            return NotificacionSMS()
        elif canal == "push":
            return NotificacionPush()
        elif canal == "whatsapp":
            return NotificacionWhatsApp()
        else:
            raise ValueError(f"Canal de notificacion no soportado: {canal}")