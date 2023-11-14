
from modulos import *

from funçoes import *

from tela_nivel_1 import *

from tela_nivel_2 import *

aplicacao()

#http://localhost/phpmyadmin/index.php?route=/sql&db=dbcentral&table=pessoas&pos=0
#cor verde escuro(#006666)
#cor azul escuro(#003366)
#site de cores (http://webcalc.com.br/Utilitarios/form/rgb_hex)

#conxao  #conn = pyodbc.connect(DRIVER="SQL Server",host='192.168.3.232\\SQLEXPRESS',database='central_tec',User = 'appcentraltec',Password = 'central')
#  pyinstaller --noconsole --name="CenTec" --icon="icon.ico" --add-data="icon.ico;." --onefile .\dbcentec.py .\modulos.py .\funçoes.py .\tela_nivel_1.py .\tela_nivel_2.py
#pyinstaller --name="CenTec" --icon="icon.ico" --add-data="icon.ico;." --onefile .\dbcentec.py .\modulos.py .\funçoes.py .\tela_nivel_1.py .\tela_nivel_2.py