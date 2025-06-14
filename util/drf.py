from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet


class AuthAPIView(APIView):
    permission_classes = (IsAuthenticated,)


class AuthGenericViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)
