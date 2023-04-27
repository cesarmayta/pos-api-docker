from rest_framework import serializers
from datetime import date

from .models import (
    Mesa,Categoria,Plato,
    Pedido,PedidoPlato
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
        
class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        #representation['time'] = date.today()
        representation['plato_img'] = instance.plato_img.url
        return representation
    
class CategoriaPlatosSerializer(serializers.ModelSerializer):
    Platos = PlatoSerializer(many=True,read_only=True)
    class Meta:
        model = Categoria
        fields = ['categoria_id','categoria_nom','Platos']
        
""" serializer para registro de pedidos """
class PedidoPlatoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fields = ['plato_id','pedidoplato_cant']
        
class PedidoSerializerPOST(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializerPOST(many=True)
    
    class Meta:
        model = Pedido
        fields = ['pedido_fech','pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos']
        
    def create(self,validated_data):
        lista_pedido_plato = validated_data.pop('pedidoplatos')
        pedido = Pedido.objects.create(**validated_data)
        for obj_pedido_plato in lista_pedido_plato:
            PedidoPlato.objects.create(pedido_id=pedido,**obj_pedido_plato)
        return pedido
    
""" para retorno de pedidos """
class PedidoPlatoSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fields = ['pedidoplato_id','pedidoplato_cant','pedido_id','plato_id']
        
class PedidoSerializerGET(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializerGET(many=True,read_only=True)
    
    class Meta:
        model = Pedido
        fields = ['pedido_id','pedido_fech','pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos']