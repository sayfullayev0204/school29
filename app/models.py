from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from urllib.parse import urlparse, parse_qs

class Yangiliklar(TranslatableModel):
    translations = TranslatedFields(
        sarlavha=models.CharField(max_length=255, verbose_name="Sarlavha"),
        matn=models.TextField(verbose_name="Matn"),
    )
    video = models.URLField(null=True, blank=True)
    main_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Asosiy rasm")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Sana")


    def get_embed_url(self):
        if "youtu.be" in self.video:
            video_id = self.video.split('/')[-1].split('?')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtube.com" in self.video:
            query = parse_qs(urlparse(self.video).query)
            video_id = query.get("v", [None])[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.video
    
    def __str__(self):
        return self.safe_translation_getter("sarlavha", any_language=True) or "No Title"
    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"

class Image(models.Model):
    article = models.ForeignKey(Yangiliklar, related_name='images', on_delete=models.CASCADE, verbose_name="Yangilik")
    image = models.ImageField(upload_to='images/', verbose_name="Qo'shimcha rasm")

    def __str__(self):
        return f"Image for {self.article.safe_translation_getter('sarlavha', any_language=True) or 'No Title'}"
    class Meta:
        verbose_name = "Rasmlar"
        verbose_name_plural = "Rasmlar"


class Olimpiada(models.Model):
    YEAR_CHOICE = (
        ('2025','2025'),
        ('2026','2026'),
        ('2027','2027'),
        ('2028','2028'),
        ('2029','2029'),
        ('2030','2030'),
    )
    Yil = models.CharField(max_length=20, choices=YEAR_CHOICE)
    Fan = models.CharField(max_length=200)
    Oqituvchi = models.CharField(max_length=200)
    CHOICE = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
    )
    Oquvchi = models.CharField(max_length=200)
    Sinf = models.CharField(max_length=20, choices=CHOICE)
    Orin = models.CharField(max_length=20)
    Ball = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Olimpiada"
        verbose_name_plural = "Olimpiada"