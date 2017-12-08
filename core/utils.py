import secrets
import string


def generate_token():
    BYTES = 32
    return secrets.token_hex(BYTES)


def serialize_instance(serializer, instance):
    return serializer(instance).data
