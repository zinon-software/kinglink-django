from django.db.models import fields
from rest_framework import serializers

from account.models import Account, Avatar, Profile


class RegistrationSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'يجب أن تتطابق كلمات المرور.'})
		account.set_password(password)
		account.save()
		return account


class ProfileUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name','description','avatar']

class AvatarSerializers(serializers.ModelSerializer):
	class Meta:
		model = Avatar
		fields = '__all__'



class AccountSerializers(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = '__all__'