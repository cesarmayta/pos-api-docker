from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Mesa,Categoria,Plato,
    Pedido,PedidoPlato
)

from .serializers import (
    MesaSerializer,
    CategoriaSerializer,
    PlatoSerializer,
    CategoriaPlatosSerializer,
    PedidoSerializerPOST,
    PedidoPlatoSerializerPOST,
    PedidoSerializerGET
)

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'content':'servidor activo'
        }
        
        return Response(context)

class MesaView(APIView):
    
    def get(self,request):
        data = Mesa.objects.all()
        serData = MesaSerializer(data,many=True)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)
    
class CategoriaView(APIView):
    
    def get(self,request):
        data = Categoria.objects.all()
        serData = CategoriaSerializer(data,many=True)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)
    
class PlatoView(APIView):
    
    def get(self,request):
        data = Plato.objects.all()
        serData = PlatoSerializer(data,many=True)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)
    

class CategoriaPlatosView(APIView):
    
    def get(self,request,categoria_id):
        data = Categoria.objects.get(pk=categoria_id)
        serData = CategoriaPlatosSerializer(data)
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)
    
class PedidoView(APIView):
    
    def get(self,request):
        data = Pedido.objects.all()
        serData = PedidoSerializerGET(data,many=True)
        
        context = {
            'ok':True,
            'pedidos':serData.data
        }
        
        return Response(context)
    
    def post(self,request):
        serData = PedidoSerializerPOST(data=request.data)
        serData.is_valid(raise_exception=True)
        serData.save()
        
        context = {
            'ok':True,
            'content':serData.data
        }
        
        return Response(context)