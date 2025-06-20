from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    CATEGORY_CHOICES = [
        ('general', '一般諮詢'),
        ('quote', '報價詢問'),
        ('other', '其他'),
    ]

    GENDER_CHOICES = [
        ('mr', '先生'),
        ('ms', '小姐'),
    ]

    # id 是 Django 默认自动添加的主键，可省略
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, blank=True)  # 非必填
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
     # ✅ 新增：是否已聯絡
    contacted = models.BooleanField(default=False, verbose_name="是否已聯絡")

    # ✅ 新增：聯絡情況備註
    contact_note = models.TextField(blank=True, verbose_name="聯絡情況")

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
