from django.contrib import admin
from appstudent.models import Register, Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["fullname", "email", "marks_inter", "is_verified"]
    search_fields = ["fullname"]
    ordering = ["marks_inter"]


class RegisterAdmin(admin.ModelAdmin):
    list_display = ["fullname", "email", "department", "mobile"]
    search_fields = ["fullname"]


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Register, RegisterAdmin)
