from django.contrib import admin
'''from myapp.models import person'''
from myapp.models import Blogs
from myapp.models import FAQ
from myapp.models import LatestNews
from myapp.models import SearchEngine
from myapp.models import user_register
from myapp.models import contact_us
from myapp.models import review
'''from myapp.models import UserChangePassword'''
from myapp.models import helpSupport


# Register your models here.

'''admin.site.register(person)'''
admin.site.register(Blogs)
admin.site.register(FAQ)
admin.site.register(LatestNews)
admin.site.register(SearchEngine)
admin.site.register(user_register)
admin.site.register(contact_us)
admin.site.register(review)
'''admin.site.register(UserChangePassword)'''
admin.site.register(helpSupport)


