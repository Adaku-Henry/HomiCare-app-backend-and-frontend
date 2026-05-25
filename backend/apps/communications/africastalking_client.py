# africastalking_client.py
from django.conf import settings

def get_at_instance():
    """
    Lazy initialization of Africa's Talking SDK.
    Prevents Render crash during startup/import time.
    """
    import africastalking

    # Initialize only when function is actually used
    africastalking.initialize(
        getattr(settings, "AFRICASTALKING_USERNAME", None),
        getattr(settings, "AFRICASTALKING_API_KEY", None)
    )

    return africastalking


def ussd_callback(request):
    try:
        at = get_at_instance()

        # Example: safe access to services
        sms = at.SMS

        # TODO: your logic here
        # sms.send(...)

        return at

    except Exception as e:
        # Prevent Render crash due to external API issues
        print(f"AfricasTalking error: {e}")
        return None