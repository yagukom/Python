#来自于https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
#编辑时间:2021-1-26 15:20
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is a placeholder text")#用于字体居中
    w.setAlignment(Qt.AlignCenter)
    #使用类似于CSS的QSS进行样式表渲染
    w.setStyleSheet("""
        background-color:black;
        color:white;
        font-family:Titillium;
        font-size:18px;
        """)
    w.show()
    sys.exit(app.exec_())
