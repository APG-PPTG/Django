from django.contrib import admin
from testapp.models import Student, Teacher, Person, Employee, Manager, Parent1, Parent2, Child
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollNo', 'marks']

admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['subject', 'salary']

admin.site.register(Teacher, TeacherAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display=['name', 'age']

admin.site.register(Person, PersonAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno', 'esal']

admin.site.register(Employee, EmployeeAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display=['exp', 'team_size']

admin.site.register(Manager, ManagerAdmin)

class Parent1Admin(admin.ModelAdmin):
    list_display= ['f1', 'f2']

admin.site.register(Parent1, Parent1Admin)

class Parent2Admin(admin.ModelAdmin):
    list_display=['f3', 'f4']

admin.site.register(Parent2, Parent2Admin)

class ChildAmin(admin.ModelAdmin):
    list_display=['f5', 'f6']

admin.site.register(Child, ChildAmin)
