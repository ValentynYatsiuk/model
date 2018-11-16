from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastyapp.models import Person
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie.authentication import MultiAuthentication


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        #excludes = ['email', 'password', 'is_superuser']

        authentication =  ApiKeyAuthentication()
        

class PersonResource(ModelResource):
	#user = fields.ForeignKey(UserResource, 'user')
	class Meta:
		queryset = Person.objects.all()
		resource_name = 'person'
		authentication =  ApiKeyAuthentication()
