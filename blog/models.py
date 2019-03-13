from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # �ٸ� �𵨿� ���� ��ũ�� �ǹ��մϴ�.
    title = models.CharField(max_length=200) # ���� ���� ���ѵ� �ؽ�Ʈ�� ������ �� ����մϴ�. �� ������ ª�� ���ڿ� ������ ������ �� ����մϴ�.
    text = models.TextField()                # ���� ���� ������ ���� �� �ؽ�Ʈ�� ���� �Ӽ��Դϴ�. ��α� �������� ��� ������?
    created_date = models.DateTimeField(
            default=timezone.now)            # ��¥�� �ð��� �ǹ��մϴ�.
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
