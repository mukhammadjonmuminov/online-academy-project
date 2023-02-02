from django.db import models

class Status:
    class Roles(models.TextChoices):
        DRAFT = 'df', 'Draft'
        PUBLISHED = 'pb', 'Published'

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='app/teachers/images/')
    degree = models.CharField(max_length=255)
    date_birth = models.DateTimeField()
    work_company = models.CharField(max_length=100)
    work_company_logo = models.ImageField(upload_to='app/teachers/work_company_logo/')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name

class Task(models.Model):

    class Difficulty(models.TextChoices):
        EASY = 'e', 'Easy'
        MEDIUM = 'm', 'Medium'
        HARD = 'h', 'Hard'

    question = models.TextField()
    difficulty = models.CharField(max_length=1, choices=Difficulty.choices, default=Difficulty.EASY)
    status = models.CharField(max_length=2, choices=Status.Roles.choices, default=Status.Roles.PUBLISHED)

    def __str__(self):
        return self.id

class LessonPart(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    video = models.FileField(upload_to='app/lesson_part/videos/')
    status = models.CharField(max_length=2, choices=Status.Roles.choices, default=Status.Roles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Lesson Part'
        verbose_name_plural = 'Lesson Parts'

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    part = models.ManyToManyField(LessonPart, blank=True)
    task = models.ManyToManyField(Task, blank=True)
    presentation_file = models.FileField(upload_to='app/lesson/presentation_file/', blank=True)
    support_downloads = models.FileField(upload_to='app/lesson/support_downloads/', blank=True)
    status = models.CharField(max_length=2, choices=Status.Roles.choices, default=Status.Roles.PUBLISHED)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    lessons = models.ManyToManyField(Lesson)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField()
    support_day = models.PositiveIntegerField(default=45)
    members = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.Roles.choices, default=Status.Roles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return self.title

class Course(models.Model):
    class Roles(models.TextChoices):
        ON = 'on', 'Online'
        OFF = 'off', 'Offline'

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    modules = models.ManyToManyField(Module, blank=True)
    education_type = models.CharField(max_length=3, choices=Roles.choices, default=Roles.ON)
    created = models.DateField(auto_now_add=True)
    members = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.Roles.choices, default=Status.Roles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    @staticmethod
    def get_objects():
        return Course.objects.order_by('id')

    def __str__(self):
        return self.title


class Speciality(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    courses = models.ManyToManyField(Course)
    members = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.Roles.choices, default=Status.Roles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialitys'

    # @staticmethod
    # def get_objects():
    #     return Speciality.objects.order_by('id')

    def __str__(self):
        return self.title