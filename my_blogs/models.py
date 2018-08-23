from django.db import models

# Create your models here.
class Topic_1(models.Model):
    """个人博客的大类1"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topics1'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry_1(models.Model):
    """大类1下的文章列表"""
    topic_1 = models.ForeignKey(Topic_1, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries1'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."


class Topic_2(models.Model):
    """个人博客的大类1"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topics2'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry_2(models.Model):
    """大类1下的文章列表"""
    topic_2 = models.ForeignKey(Topic_2, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries2'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."


class Topic_3(models.Model):
    """个人博客的大类1"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topics3'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry_3(models.Model):
    """大类1下的文章列表"""
    topic_3 = models.ForeignKey(Topic_3, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries3'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."


class Topic_4(models.Model):
    """个人博客的大类1"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topics4'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry_4(models.Model):
    """大类1下的文章列表"""
    topic_4 = models.ForeignKey(Topic_4, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries4'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."





