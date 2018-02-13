import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QMessageBox,
    QTextEdit, QGridLayout, QApplication, QDesktopWidget, QMainWindow)
from PyQt5.QtCore import Qt

class Chat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        self.chatView = QTextEdit()
        self.chatView.setReadOnly(True)
        self.messageEdit = QLineEdit()
        self.messageEdit.returnPressed.connect(self.enterPressed)

        grid = QGridLayout(mainWidget)
        grid.setSpacing(10)

        grid.addWidget(self.chatView, 1, 0, 3, 0)
        grid.addWidget(self.messageEdit, 4, 0)

        self.resize(250, 300)
        self.setWindowTitle('Chat')
        self.statusBar().showMessage('Ready')
        self.show()

    def showEvent(self, e):
        self.messageEdit.setFocus()

    def enterPressed(self):
        textBuf = self.chatView.toPlainText()
        self.chatView.setText(textBuf + self.messageEdit.text())
        # QMessageBox.question(self, 'Message', self.messageEdit.text(), QMessageBox.Ok)
        self.messageEdit.setText('')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    newChat = Chat()
    sys.exit(app.exec_())