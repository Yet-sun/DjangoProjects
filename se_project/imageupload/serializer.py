from rest_framework import serializers
from .models import Guest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('username', 'password')


class UserManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'name', 'sex', 'age')


class UserSignSerializer(serializers.Serializer):
    "用户序列化器"
    name = serializers.CharField()
    sex = serializers.CharField()
    age = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    # id = serializers.IntegerField()

    def create(self, validated_data):
        '''新建'''
        user = Guest.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        '''更新，instance为要更新是对象示实例'''
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        # instance.id = validated_data.get('id', instance.id)
        instance.age = validated_data.get('age', instance.age)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.save()
        return instance
