from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import User



class CommentManager(models.Manager):
    # Comment操作に関する処理を追加
    def create_comment(self, user_name, message, topic_id, image=None):
        comment = self.model(
            user_name=user_name,
            message=message,
            image=image
        )
        comment.topic = Topic.objects.get(id=topic_id)
        comment.no = self.filter(topic_id=topic_id).count() + 1
        comment.save()

class CategoryManager(models.Manager):
    # Category操作に関する処理を追加
    pass

class VoteManager(models.Manager):
    def create_vote(self, ip_address, comment_id):
        vote = self.model(
            ip_address=ip_address,
            comment_id = comment_id
        )
        try:
            vote.save()
        except:
            return False
        return True

class Category(models.Model):
    name = models.CharField(
        'カテゴリー名',
        max_length=50,
    )
    url_code = models.CharField(
        'URLコード',
        max_length=50,
        null=True,
        blank=False,
        unique=True,
    )
    sort=models.IntegerField(
        verbose_name='ソート',
        default=0,
    )
    objects = CategoryManager()

    def __str__(self):
        return self.name

class Topic(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        null=True,
        blank=True,
    )
    user_name = models.CharField(
        'お名前',
        max_length=30,
        null=True,
        blank=False,
    )
    title = models.CharField(
        'タイトル',
        max_length=255,
        null = False,
        blank = False,
    )
    message = models.TextField(
        verbose_name='本文',
        null=True,
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリー',
        on_delete=models.PROTECT,
        null=True,
        blank=False,
    )
    reference_book_name = models.CharField(
        '参考書名',
        max_length=30,
        null=True,
        blank=False,
    )
    reference_book_page = models.IntegerField(
        verbose_name='ページ',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name= '画像アップロード',
        upload_to = 'images/',
        null = True,
        blank = True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )
    objects = ()

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )
    no = models.IntegerField(
        default=0,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        null=True,
        blank=True,
    )
    user_name = models.CharField(
        'お名前',
        max_length=30,
        null=True,
        blank=False,
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
    )
    message = models.TextField(
        verbose_name='投稿内容'
    )
    image = models.ImageField(
        verbose_name='投稿画像',
        validators=[FileExtensionValidator(['jpg', 'png'])],
        upload_to='images/%Y/%m/%d/',
        null=True,
        blank=True,
    )
    pub_flg = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    objects = CommentManager()

    def __str__(self):
        return '{}-{}'.format(self.topic.title, self.no)

class Vote(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=True,
    )
    ip_address = models.CharField(
        'IPアドレス',
        max_length=50,
    )

    objects = VoteManager()

    def __str__(self):
        return '{}-{}'.format(self.comment.topic.title, self.comment.no)