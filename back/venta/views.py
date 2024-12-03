from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# SDK de Mercado Pago
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK(
    "APP_USR-936168452210572-061619-f651358d6e63a47ac60b46fe256f4e2d-582661966")


class ReferenceMPView(APIView):
    def post(self, request, format=None):
        items = request.data.get("items")
        newlist = [{"unit_price": float(x.pop(
            "precio")), "title": x.pop(
            "nombre"), "quantity": x.pop(
            "cantidad"), **x} if "precio" and "cantidad" and "nombre" in x else x for x in items]
        infoClient = request.data.get("client")
       # Crea un ítem en la preferencia
        if items:
            preference_data = {
                "items": newlist
            }
            preference = sdk.preference().create(preference_data)
            print(preference)
            if preference['status'] == 400:

                return Response(status=status.HTTP_404_NOT_FOUND)
            response = preference["response"]
            return Response({"init_point": response["init_point"]})
        return Response(status=status.HTTP_404_NOT_FOUND)
