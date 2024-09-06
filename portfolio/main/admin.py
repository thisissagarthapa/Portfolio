from django.contrib import admin
from .models import Info
from .models import Project
# from .models import About
# from .models import SocialMedia
# Register your models here.
@admin.register(Info)

class AdminInfo(admin.ModelAdmin):
    list_display=['id','name','email','phoneno','emailsub','message']
 
 
@admin.register(Project)   
class AdminProjects(admin.ModelAdmin):
    list_display=['id','image','title', 'desc','link']


