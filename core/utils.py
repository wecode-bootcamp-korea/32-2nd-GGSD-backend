import jwt, json

from django.conf import settings
from django.http import JsonResponse

from users.models import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, settings.SECRET_KEY, algorithms = settings.ALGORITHM)
            request.user = User.objects.get(id=payload['id'])
        
        except jwt.InvalidSignatureError:
            return JsonResponse({'MESSAGE' : 'INVALID_SIGNATURE'}, status=401)
        
        except jwt.DecodeError:
            return JsonResponse({'MESSAGE' : 'INVALID_PAYLOAD'}, status=401)
        
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=400)
        
        return func(self, request, *args, **kwargs)
    return wrapper