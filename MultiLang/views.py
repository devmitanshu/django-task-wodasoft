from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from .models import *

# ===================================================
# Home page function to translate items as per current 
# application language and and send back to index.html page
# ===================================================
def home(request):
    data = {
        'aboutme_title': translate(item = 'aboutme_title'),
        'about': translate(item = 'about'),
        'skills_title': translate(item = 'skills_title'),
        'skills': translate(item = 'skills'),
        'ssc': translate(item = 'ssc'),
        'hsc': translate(item = 'hsc'),
        'grad': translate(item = 'grad'),
        'intern1': translate(item = 'intern1'),
        'intern1_about': translate(item = 'intern1_about'),
        'intern2': translate(item = 'intern2'),
        'intern2_about': translate(item = 'intern2_about'),
        'emagazine': translate(item = 'emagazine'),
        'pskills': translate(item = 'pskills'),
        'pskills_about': translate(item = 'pskills_about'),
        'contact': translate(item = 'contact'),
    }

    return render(request, 'index.html', data)
# ===================================================





# ===================================================
# Function translate item text by querying on model
# ===================================================
def translate(item):
    cur_language = get_language()
    try:
        trans_dict_name = 'translation__' + cur_language
        text = Article.objects.filter(item = item).values(trans_dict_name)

        if len(text) > 0:
            text = text[0][trans_dict_name]
        else:
            text = ''

    finally:
        activate(cur_language)
    return text

# ===================================================