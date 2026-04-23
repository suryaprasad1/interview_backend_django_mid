from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from interview.order.models import Order
from rest_framework.generics import ListAPIView
from django.utils.dateparse import parse_date


class DeactivateOrderView(APIView):

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        order.is_active = False
        order.save(update_fields=["is_active"])

        return Response(
            {"message": "Order deactivated successfully"},
            status=status.HTTP_200_OK
        )


#Return orders that fall between a given start date and embargo date
class OrderEmbargoFilterView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()

        start = self.request.query_params.get("start")
        end = self.request.query_params.get("end")

        if start:
            start_date = parse_date(start)
            if start_date:
                queryset = queryset.filter(start_date__gte=start_date)

        if end:
            end_date = parse_date(end)
            if end_date:
                queryset = queryset.filter(embargo_date__lte=end_date)

        return queryset

#List all tags for a given order
class OrderTagsView(APIView):

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        tags = order.tags.all()
        serializer = OrderTagSerializer(tags, many=True)

        return Response(serializer.data)
#List all orders linked to a given tag
class TagOrdersView(APIView):

    def get(self, request, pk):
        tag = get_object_or_404(OrderTag, pk=pk)

        orders = tag.orders.all()  # reverse relation
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)
