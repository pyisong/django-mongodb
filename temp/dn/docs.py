# -*- coding:utf-8 -*-

from mongoengine import (connect, Document, StringField,
                         URLField, ListField,
                         EmbeddedDocument, EmbeddedDocumentField)

from djangotoolbox.fields import ListField

connect('test')


# 先定义名为Profile的EmbeddedDocument
class Profile(EmbeddedDocument):
    gender = StringField()
    location = StringField()


class User(Document):
    username = StringField(required=True)
    website = URLField()
    tags = ListField(StringField(max_length=16))
    # 添加到User
    profile = EmbeddedDocumentField(Profile)
