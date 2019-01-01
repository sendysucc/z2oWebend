# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Promote)
admin.site.register(Game)
admin.site.register(GameRoom)
admin.site.register(ForbiddenIp)
admin.site.register(ForbiddenUser)
admin.site.register(LoginRecord)