from rest_framework import serializers
from .models import PersonaModel


class PersonasSerializer(serializers.ModelSerializer):
    # Si el serializador es correspondiente a un modelo, debemos pasar informacion a su metadata indicando a que modelo corresponde
    class Meta:
        # model => indica en que modelo se tiene que basar para traer toda su configuracion (que serian las columnas y tipos de datos) para que al momento de serializar (formatear) lo convierta al tipo de dato
        model = PersonaModel
        # field > indica que columnas (atributos) va a utilizar de ese modelo este serializador '__all__', sin embargo si queremos que solamente use determinadas columnas, seria asi ['personaNombre','personaCorreo,]
        fields = '__all__'
