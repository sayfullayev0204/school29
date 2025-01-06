from django.db import models

class Yangiliklar(models.Model):
    sarlavha=models.CharField(max_length=255, verbose_name="Sarlavha")
    matn=models.TextField(verbose_name="Matn")
    main_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Asosiy rasm")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    def __str__(self):
        return self.sarlavha
    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"

class Image(models.Model):
    article = models.ForeignKey(Yangiliklar, related_name='images', on_delete=models.CASCADE, verbose_name="Yangilik")
    image = models.ImageField(upload_to='images/', verbose_name="Qo'shimcha rasm")

    def __str__(self):
        return f"Image for {self.article.sarlavha or 'No Title'}"
    class Meta:
        verbose_name = "Rasmlar"
        verbose_name_plural = "Rasmlar"
