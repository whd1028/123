from rest_framework import serializers
from .models import N_summarization, News

#Json 데이터로 보냄
class TodoSerializers(serializers.ModelSerializer):
    class Meta: # DB 사용 클래스 
        model = N_summarization # 모델의 DB 테이블
        field = ('ns_id', 'n', 'ns_content',) # 테이블 컬럼

class NewsSerializers(serializers.ModelSerializer):
    class Meta: # DB 사용 클래스 
        model = News # 모델의 DB 테이블
        field = ('n_title',) # 테이블 컬럼
