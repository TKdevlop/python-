import sys
from PyQt5 import*

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle('pyQt Tuts')

window.show()
sys.exit(app.exec_())
