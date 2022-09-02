import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

# 03
director_list =\
    [
    {"name" : "봉준호", "debut": "1993-01-01", "country" : "KOR"},
    {"name" : "김한민", "debut": "1999-01-01", "country" : "KOR"},
    {"name" : "최동훈", "debut": "2004-01-01", "country" : "KOR"},
    {"name" : "이정재", "debut": "2022-01-01", "country" : "KOR"},
    {"name" : "이경규", "debut": "1992-01-01", "country" : "KOR"},
    {"name" : "한재림", "debut": "2005-01-01", "country" : "KOR"},
    {"name" : "Joseph Kosinski", "debut": "1999-01-01", "country" : "KOR"},
    {"name" : "김철수", "debut": "2022-01-01", "country" : "KOR"}
    ]

for i in range(len(director_list)):
    director = Director()
    director.name = director_list[i]["name"]
    director.debut = director_list[i]["debut"]
    director.country = director_list[i]["country"]
    director.save()

# 04
genre_list = ["액션", "드라마", "사극", "범죄", "스릴러", "SF", "무협", "첩보", "재난"]

for j in range(len(genre_list)):
    genre = Genre()
    genre.title = genre_list[j]

# 05
directors = Director.objects.all()

for director in directors:
    print(director.name, director.debut, director.country)

# 06
mr_bong = Director.objects.get(id = 1)
print(mr_bong.name, mr_bong.debut, mr_bong.country)

# 07
Director.objects.get(country = 'USA')

# 09
joseph = Director.objects.get(name = 'Joseph Kosinski')
joseph.country = 'USA'
joseph.save()

print(joseph.name, joseph.debut, joseph.country)

# 10
Director.objects.get(country = 'KOR')

# 12
directors = Director.objects.filter(country = 'KOR')

for director in directors:
    print(director.name, director.debut, director.country)

# 14
mr_kim = Director.objects.get(name = '김철수')
mr_kim.delete()