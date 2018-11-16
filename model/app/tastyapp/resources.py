from tastypie.resources import Resource, ModelResource
from tastyapp.models import Person
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization



class PersonResource(ModelResource):
    
    class Meta:
        queryset = Person.objects.all()
        image = fields.FileField(attribute="image", null=True, blank=True)  
        resource_name = 'person'
        # Add it here.
        #authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()
        #authentication = BasicAuthentication()
        #resource_name = 'auth/user'
        #excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        #authorization = DjangoAuthorization()
   