# Script para capitura de html de uma pagina
# Data: 20-07-2021
# Autor: Edson L. B. Filho
#
# Dependencias:
#     pip install requests
#     pip install beautifulsoup4
#
from urllib import request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url='http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'

try:
   def limpa_html (tags):
   #limpeza de marcações e espações
      return " ".join(tags.split()).replace('> <','><')

   opener = request.build_opener(request.HTTPCookieProcessor())
   req = opener.open(url)
   page = req.read()
#  Transforme a origem do site em string
   page = page.decode('utf-8')
   dados = limpa_html(page)
#  print(dados)
#  variavel para armazenar o html da pagina em object
   soup = BeautifulSoup(dados, 'html.parser')
#  Visualizando de forma mais estruturada
#  print(soup.prettify())

#  Iniciando trabalho com as tags
   print(soup.table.tr.th.text)

except HTTPError as e:
      print(e.status, e.reason)

except URLError as e:
      print(e.status, e.reason)



