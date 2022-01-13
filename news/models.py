from django.db import models

class NCategory(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'N_category'


class NCategoryDetail(models.Model):
    cd_id = models.AutoField(primary_key=True)
    c = models.ForeignKey(NCategory, models.DO_NOTHING)
    cd_name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'N_category_detail'


class NContent(models.Model):
    nc_id = models.AutoField(primary_key=True)
    n = models.OneToOneField('News', models.DO_NOTHING, blank=True, null=True)
    n_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_content'


class NSummarization(models.Model):
    ns_id = models.AutoField(primary_key=True)
    n = models.OneToOneField('News', models.DO_NOTHING, blank=True, null=True)
    ns_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_summarization'


class News(models.Model):
    n_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Press', models.DO_NOTHING, blank=True, null=True)
    cd = models.ForeignKey(NCategoryDetail, models.DO_NOTHING, blank=True, null=True)
    n_title = models.CharField(max_length=1024)
    nd_img = models.CharField(max_length=1024, blank=True, null=True)
    n_input = models.DateTimeField(blank=True, null=True)
    o_link = models.CharField(unique=True, max_length=768, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'News'


class Press(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'Press'