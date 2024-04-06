from django.db import models
from django.conf import settings


class Person(models.Model):
    """ Model representing a person """

    # Fields
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    email = models.EmailField()
    is_driver = models.BooleanField(default=False)
    address = models.ForeignKey("Address", on_delete=models.RESTRICT, null=True)
    company = models.ForeignKey("Company", on_delete=models.RESTRICT, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.SET_NULL, null=True,
                                blank=True)


    # Methods
    def __str__(self):
        """ String for representing this Person Object """
        return self.name


class Address(models.Model):
    """ Model representing an address """

    # Fields
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)


    # Methods
    def __str__(self):
        """ String for representing this Address object """
        return f"{self.street}\n{self.city}\n{self.province},{self.postal_code}\n{self.city}"


class Company(models.Model):
    """ Model representing a company """

    # Fields
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, null=True)


    # Methods
    def __str__(self):
        """ String for representing this Company Object """
        return self.name


class CarpoolGroup(models.Model):
    """ Model representing a group of Person objects carpooling together """

    # Fields
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(Person, related_name="carpoolgroup_member_set")
                                            # pass a relevant related_name
                                            # (Person.carpoolgroup_member_set will
                                            # be the reverse accessor)
    driver = models.ForeignKey(Person, on_delete=models.RESTRICT, null=False, 
                                related_name="carpoolgroup_driver_set")
                                    # pass a relevant related_name
                                    # (Person.carpoolgroup_driver_set will
                                    # be the reverse accessor)

    
    # Methods
    def __str__(self):
        """ String for representing this CarpoolGroup object """
        return self.name
