from django.db import models

# Create your models here.

from urllib.parse import urlparse
from django.core.files import File
from utils.file import download, get_buffer_ext

'''
class Attraction(models.Model):
    #id는 TripAdvisor의 장소 id.
    id = models.IntegerField(primary_key = True)
    #name은 TripAdvisor의 관광장소의 이름.
    name = models.CharField(null = True, max_length = 200)
    # star는 트립어드바이저의 별점에 10을 곱한 수
    star = models.IntegerField()
    #cat1, 2는 TourAPI의 대분류, 중분류를 사용함.
    main = models.CharField(max_length = 100)
    middle = models.CharField(max_length = 100)
    #type은 TripAdvisor의 분류 타입을 사용함.
    type = models.CharField(max_length = 100)
    #url는
    url = models.URLField('', max_length = 400, blank = True)
    #image는 TourAPI에서 나오는 사진 or 개별적으로 구한 사진
    image = models.ImageField(upload_to = '', blank = True)
    # num은 리뷰의 개수
    num = models.IntegerField()

    def __str__(self):
        return self.name

    def set_image(self, *args, **kwargs):
        if self.url and not self.image:
            temp_file = download(self.url)
            file_name = '{urlparse}.{ext}'.format(
                urlparse = urlparse(self.url).path.split('/')[-1].split('.')[0],
                ext = get_buffer_ext(temp_file))
            self.image.save(file_name, File(temp_file))
            super().save()
        else:
            super().save()

class Review(models.Model):
    #여행장소 하나당 리뷰가 0개부터 2개 이상이므로,
    attraction = models.ForeignKey(Attraction, on_delete = models.CASCADE)
    #리뷰 내용은 TextField로
    content = models.TextField()
'''

class AttTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    star = models.IntegerField()
    num = models.IntegerField()
    type = models.ForeignKey('TypeTable', models.DO_NOTHING, db_column='type')
    address = models.TextField(blank=True, null=True)
    loid = models.IntegerField()
    location = models.IntegerField()
    url = models.TextField()
    image = models.ImageField(upload_to = '', blank = True, db_column = 'image')

    class Meta:
        managed = False
        db_table = 'att_table'

    def __str__(self) :
        return self.name

    def set_image(self, *args, **kwargs):
        if self.url and not self.image:
            temp_file = download(self.url)
            file_name = '{urlparse}.{ext}'.format(
                urlparse = urlparse(self.url).path.split('/')[-1].split('.')[0],
                ext = get_buffer_ext(temp_file))
            self.image.save(file_name, File(temp_file))
            super().save()
        else:
            super().save()

class ChoiceTable(models.Model):
    seq = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choice_table'

class ReviewTable(models.Model):
    ind = models.AutoField(primary_key=True)
    id = models.ForeignKey(AttTable, models.DO_NOTHING, db_column='id', blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    seq = models.ForeignKey('UserTable', models.DO_NOTHING, db_column='seq', blank=True, null=True)
    keyword1 = models.CharField(max_length=45, blank=True, null=True)
    keyword2 = models.CharField(max_length=45, blank=True, null=True)
    keyword3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_table'

class TypeTable(models.Model):
    type = models.CharField(primary_key=True, max_length=45)
    seq = models.IntegerField()
    main_type = models.TextField(blank=True, null=True)
    middle_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_table'
        unique_together = (('type', 'seq'),)


class UserTable(models.Model):
    seq = models.BigIntegerField(primary_key=True)
    user = models.CharField(max_length=50)
    age = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    pw = models.TextField(db_column='PW', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_table'
        unique_together = (('seq', 'user'),)

class KeywordTable(models.Model):
    keyword = models.IntegerField(primary_key=True)
    keyname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'keyword_table'

#not available models are written below

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
