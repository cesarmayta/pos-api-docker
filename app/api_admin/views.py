from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,JSONParser


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from api.models import (
    Mesa,Categoria,Plato
)

from api.serializers import (
    MesaSerializer,CategoriaSerializer,
    PlatoSerializer
)

class MesaViewSet(viewsets.ModelViewSet):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class PlatoViewSet(viewsets.ModelViewSet):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    
######## subir archivos a cloudinary
import cloudinary.uploader

class UploadPlatoImagenView(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    parser_classes = (
        MultiPartParser,
        JSONParser
    )
    
    @staticmethod
    def post(request):
        file = request.data.get('plato_img')
        
        upload_data = cloudinary.uploader.upload(file)
        
        context = {
            'status':True,
            'content':upload_data
        }
        
        return Response(context,status=201)