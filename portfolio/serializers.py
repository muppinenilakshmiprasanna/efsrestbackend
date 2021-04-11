from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Investment, Stock, MutualFunds


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
            model = Customer
            fields = ('pk','name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'cell_phone')


class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
            model = Investment
            fields = ('pk','customer','cust_number', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')


class StockSerializer(serializers.ModelSerializer):

    class Meta:
            model = Stock
            fields = ('pk','customer', 'cust_number', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')


class FundSerializer(serializers.ModelSerializer):

    class Meta:
            model = MutualFunds
            fields = ('pk','customer', 'cust_number','symbol', 'name','description', 'purchase_price', 'purchase_date','recent_value', 'recent_date')


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password','password2')

