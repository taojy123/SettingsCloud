# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class SettingScript(models.Model):

    name = models.CharField(max_length=255, verbose_name='名称', unique=True)
    keys = models.TextField(blank=True, verbose_name='查看密钥', help_text='可配置多个,每个一行,留空表示不需要密钥就可查看')
    language = models.CharField(max_length=100, blank=True, verbose_name='脚本语言', default='python')
    content = models.TextField(blank=True, verbose_name='脚本内容', default="EXAMPLE_KEY = 'ABC'")

    def __unicode__(self):
        return self.name

    @property
    def key_list(self):
        keys = self.keys.strip()
        if not keys:
            return []
        return keys.splitlines()

    class Meta:
        verbose_name = '配置脚本'
        verbose_name_plural = '配置脚本'
