from django.contrib.sessions.models import Session
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def logout_previous_sessions(sender, request, user, **kwargs):
    logger.info(f"User {user.username} logged in. Checking for previous sessions.")
    # Obtén todas las sesiones activas del usuario
    user_sessions = Session.objects.filter(expire_date__gte=request.session.get_expiry_date())
    
    for session in user_sessions:
        data = session.get_decoded()
        # Cierra la sesión si pertenece al usuario actual
        if data.get('_auth_user_id') == str(user.id):
            logger.info(f"Logging out session {session.session_key} for user {user.username}.")
            session.delete()
