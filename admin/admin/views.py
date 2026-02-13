from rest_framework.views import APIView
from rest_framework.response import Response
import random

class UserAPIView(APIView):
    def get(self, _):
        return Response({
            'id': random.randint(1, 10)
        })