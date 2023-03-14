from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    aciklama = models.TextField()
    members = models.ManyToManyField(User, related_name='teams')
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams',verbose_name='Team Leader')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    aciklama = models.TextField()
    STATUS_CHOICES = (
        ('Beklemede', 'Beklemede'),
        ('Baslamadi', 'Baslamadi'),
        ('Devam Ediyor', 'Devam Ediyor'),
        ('Tamamlandi', 'Tamamlandi'),
        ('Suresi Gecti', 'Suresi Gecti'),
        ('Ek Sure Talep Ediliyor', 'Ek Sure Talep Ediliyor')
    )
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Beklemede',verbose_name='Durum')
    URGENCY_CHOICES = (
        ('primary', 'Normal'),
        ('warning', 'Acil'),
        ('danger', 'Kritik')
    )
    aciliyet = models.CharField(max_length=25, choices=URGENCY_CHOICES, default='primary', verbose_name='Aciliyet')
    ek = models.FileField(blank=True,null=True,verbose_name='Dosya Eki')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tasks')
    atayan = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    atanan = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned_to')
    baslangic = models.DateField(verbose_name='baslangic')
    bitis = models.DateField(verbose_name='bitis')
    completed = models.BooleanField(default=False)
    completed_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Checklist(models.Model):
    title = models.TextField()
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='Checklist')
    is_completed = models.BooleanField(default=False,verbose_name='Tamamlandi')
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    title = models.TextField()
    yazar = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title