from mysite.cms.models import Menu
from mysite import settings
from mysite.catalog.models import Region
from mysite.cms.models import Article, News

def mysite(request):

      return {
           #'TOP_ARTICLES': Article.objects.filter(status=3).order_by('sort')[:4],
           'TEMP_VAR': 'TMP variable from context proccessor'
      }
