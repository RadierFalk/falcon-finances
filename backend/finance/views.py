from rest_framework import viewsets
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer
from finance.mixins import CompanyQuerySetMixin, CompanyCreateMixin


class CategoryViewSet(
    CompanyQuerySetMixin,
    CompanyCreateMixin,
    viewsets.ModelViewSet
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionViewSet(
    CompanyQuerySetMixin,
    CompanyCreateMixin,
    viewsets.ModelViewSet
):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
