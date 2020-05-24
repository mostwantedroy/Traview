from django.db import models

# Create your models here.

from urllib.parse import urlparse
from django.core.files import File
from utils.file import download, get_buffer_ext

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
            super.save()

class Review(models.Model):
    #여행장소 하나당 리뷰가 0개부터 2개 이상이므로,
    attraction = models.ForeignKey(Attraction, on_delete = models.CASCADE)
    #리뷰 내용은 TextField로
    content = models.TextField()
