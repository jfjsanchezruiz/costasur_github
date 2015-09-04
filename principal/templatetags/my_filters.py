from django import template
from principal import lang_library

register = template.Library()

def getTotal(dlist, dfield):
   return sum(d[dfield] for d in dlist)

def getText(text,lang):
	return lang_library.getText(text,lang)

def cutText(text,params):
	ini = int(params.split(",")[0])
	fin = int(params.split(",")[1])

	if (params.split(",")[2] == "N"):
		return int(text[ini:fin])
	else:
		return text[ini:fin]

register.filter('getTotal', getTotal)
register.filter('getText', getText)
register.filter('cutText', cutText)