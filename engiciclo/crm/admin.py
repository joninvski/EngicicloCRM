from crm.models import Poster
from django.contrib import admin
from django import forms
from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import AdminTextInputWidget
from django.db import models

import datetime

admin.site.register(Poster)
