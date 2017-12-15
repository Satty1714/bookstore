from django.db import models
from db.base_model import BaseModel
from users.models import User
from books.models import Books

# Create your models here.
class Comments(BaseModel):
    show = models.BooleanField(default=True,verbose_name='显示评论')
    content = models.CharField(max_length=1000,verbose_name='评论内容')
    user = models.ForeignKey('users.User',verbose_name='用户id',default='')
    book = models.ForeignKey('books.Books',verbose_name='书籍id')

    class Meta:
        db_table = 's_comments'