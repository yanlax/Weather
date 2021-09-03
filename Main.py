from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Weather import Ui_Form
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import sys

app = QApplication(sys.argv)
Form =  QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def Weather():
	try:
		config_dict = get_default_config()
		config_dict['language'] = 'ru'
		City = ui.lineEdit.text()
		owm = OWM('9fc22c64d559207ef7be7fa2e2d5fa5e')
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place( City )
		w = observation.weather
		temp=w.temperature('celsius')["temp"]
		status=w.detailed_status
		wind=w.wind()

		ui.label_3.setText(' В городе ' + City + ' сейчас: ' + status +"\n" f' Температура: {temp}' +"\n" f' Ветер: {wind}')
	except:
		ui.label_3.setText(' Город не найден ')




ui.pushButton.clicked.connect( Weather )









sys.exit(app.exec_())
