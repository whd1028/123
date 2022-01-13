from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

# select n_content from N_content nc inner join News n on nc.n_id = n.n_id where n.n_title = "여기어때 고객 이메일 유출..일괄 발송 설정때문, 사과공지"