from tokenize import TokenError
from rest_framework import viewsets
from .models import DailyRecord
from .serializers import DailyRecordSerializer, RegisterSerializer
from .filters import DialyRecordFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class DialyRecordViewSet(viewsets.ModelViewSet):
    queryset = DailyRecord.objects.all().order_by('point')
    serializer_class = DailyRecordSerializer
    filterset_class = DialyRecordFilter
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = [AllowAny] # For testing

class AuthViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    # Create a new user and return JWT tokens
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 'user created',
                'user': {'id': user.id, 'username': user.username},
                 'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Behave same as TokenObtainPairView 
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Blacklist the refresh token on logout
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'status': 'user logged out'}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response(
                {"error": f"Token error: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)