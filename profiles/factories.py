from random import choice

from factory import Factory, SubFactory, Faker
from factory.django import DjangoModelFactory
from .models import Profile, Bio
from countries.models import Country

country_list = list(Country.objects.all())  


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        kwargs['country'] = choice(country_list)  # Select a random country from the cached list
        return super()._create(model_class, *args, **kwargs)
    
    iqama = Faker('random_number', digits=16)
    national_id = Faker('random_number', digits=16)
    passport = Faker('random_number', digits=16)
    first_name = Faker('first_name')
    second_name = Faker('last_name')
    third_name = Faker('last_name')
    last_name = Faker('last_name')
    email = Faker('email')
    phone = Faker('phone_number')
    gender = Faker('random_element', elements=('M', 'F', 'U'))
    is_active = Faker('boolean')


class BioFactory(DjangoModelFactory):
    class Meta:
        model = Bio
    
    profile = SubFactory(ProfileFactory)
    bio = Faker('text', max_nb_chars=100)
    address1 = Faker('building_number')
    address2 = Faker('street_address')
    city = Faker('city')
    extra_data = {}

