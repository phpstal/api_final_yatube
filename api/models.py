from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Заголовок', 
        max_length=200,
        help_text='Напишите название группы'
    )
    slug = models.SlugField(
        verbose_name='Слаг',         
        help_text=('Укажите адрес для страницы задачи. Используйте только '
                   'латиницу, цифры, дефисы и знаки подчёркивания')
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Напишите описание группы'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(  
        verbose_name='Текст сообщения', 
        help_text='Напишите ваш пост в это окно'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', 
        auto_now_add=True,
        help_text='Укажите дату написания поста'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True,         
        related_name='posts'
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User, null=True,
        on_delete=models.CASCADE,
        related_name='following'
    )