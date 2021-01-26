#来自于https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()

    w = QLabel("lalala")#Widget()
    w.setAlignment(Qt.AlignCenter)#用于字体居中
    with open("QT2Style.qss", "r") as f:#使用类似于加载外置css文件的方式加载qss样式表
        _style = f.read()
        app.setStyleSheet(_style)
    w.show()
    
    sys.exit(app.exec_())
