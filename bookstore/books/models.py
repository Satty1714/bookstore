from django.db import models
from db.base_model import BaseModel
from books.enums import *
from tinymce.models import HTMLField

# Create your models here.
class BooksManager(models.Manager):

    def get_books_by_type(self,type_id,limit=None,sort='default'):
        '''根据商品类型id查询商品信息'''
        if sort == 'new':
            order_by = ('-create_time',)
        elif sort == 'hot':
            order_by = ('-sales',)
        elif sort == 'price':
            order_by = ('price',)
        else:
            order_by = ('-pk',)
        #查询数据
        books_li =self.filter(type_id=type_id).order_by(*order_by)
        #查询结果集的限制
        if limit:
            books_li = books_li[:limit]
        return books_li

    def get_books_by_id(self,book_id):
        '''根据商品的id获取商品信息-'''
        try:
            book = self.get(id=book_id)
        except self.model.DoesNotExist:
            #不存在商品信息
            book = None
        return book




class Books(BaseModel):
    '''商品模型类'''
    books_type_choices = ((k,v) for k,v in BOOK_TYPE.items())
    status_choices = ((k,v) for k,v in STATUS_CHOICE.items())
    type_id = models.SmallIntegerField(default=PYTHON,choices=books_type_choices,verbose_name='书籍种类')
    title = models.CharField(max_length=50,verbose_name='书籍名称')
    desc = models.CharField(max_length=50,verbose_name='书籍简介')
    price = models.IntegerField(default=0,verbose_name='书籍价格')
    detail = models.CharField(max_length=500,verbose_name='书籍详情')
    unit = models.CharField(max_length=5,verbose_name='书籍单位')
    sales = models.IntegerField(default=0,verbose_name='书籍销量')
    image = models.ImageField(upload_to='books',verbose_name='商品图片')
    status = models.SmallIntegerField(default=ONLINE,choices=status_choices,verbose_name='商品状态')
    details = HTMLField(default='')

    objects = BooksManager()


    class Meta:
        db_table = 's_book_info'
