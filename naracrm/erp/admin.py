from django.contrib import admin
from .models import Team, Task, Checklist, Comment

class TaskInline(admin.TabularInline):
    model = Task

class ChecklistInline(admin.TabularInline):
    model = Checklist
    
class CommentInline(admin.TabularInline):
    model = Comment

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'aciklama', 'team_leader', 'created_at']

class TaskAdmin(admin.ModelAdmin):
    inlines = [ChecklistInline,CommentInline]
    list_display = ['title', 'aciklama', 'team', 'atayan', 'atanan', 'completed', 'created_at']
    list_filter = ['team', 'atayan', 'atanan', 'completed']
    
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ['title','is_completed']
    list_filter = ['title','is_completed']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['title','yazar']
    list_filter = ['yazar']

admin.site.register(Team, TeamAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(Comment, CommentAdmin)