from rest_framework import serializers

from .models import User_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = ('CustomerId','Age', 'Location','Device','Income','Balance','Products')

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = ('Income')
def create(self, validated_data):
        return User_data.objects.create(**validated_data)
    
def update(self, instance, validated_data):
    instance.Income = validated_data.get('Income', instance.Income)
    instance.save()
    return instance
