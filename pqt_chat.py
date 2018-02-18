import obyasnitelnaya

import sys
from PyQt5.QtWidgets import (qApp, QWidget, QLabel, QLineEdit, QMessageBox,
    QTextEdit, QGridLayout, QApplication, QDesktopWidget, QMainWindow, QAction, QPushButton)
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QIcon, QTextCursor, QCloseEvent

import chat_config

class Chat(QMainWindow):
    def __init__(self, x_size=550, y_size=450, title='Chat'):
        super().__init__()

        self._mainWidget = QWidget()
        self.setCentralWidget(self._mainWidget)

        self.chatView = QTextEdit()
        self.chatView.setReadOnly(True)

        self.messageEdit = QTextEdit()
        #self.messageEdit.returnPressed.connect(self.enterPressed)

        btnSendMess = QPushButton('Send', self)
        btnSendMess.clicked.connect(lambda: self._do_action('button', 'Send'))

        action_textBold = self._connect_action(QIcon(chat_config.text_bold_icon), 'Bold', '', 'Bold text',
                                               lambda: self._do_action('text', 'b'))
        action_textBias = self._connect_action(QIcon(chat_config.text_bias_icon), 'Bias', '', 'Bold text',
                                               lambda: self._do_action('text', 'i'))
        action_textUnder = self._connect_action(QIcon(chat_config.text_underline_icon), 'Under','', 'Bold text',
                                               lambda: self._do_action('text', 'u'))

        action_exit     = self._connect_action(QIcon(chat_config.app_exit_icon),  '&Exit', 'Ctrl+Q', 'Exit app', self.close)

        # В macOS почему-то при добавлении меню, окно приложения перестает центрироваться(
        # В Windows же все Ok
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(action_exit)

        self.toolbar = self.addToolBar('Main')
        self.toolbar.addAction(action_textBold)
        self.toolbar.addAction(action_textBias)
        self.toolbar.addAction(action_textUnder)
        self.toolbar.addSeparator()
        self.toolbar.addAction(action_exit)

        grid = QGridLayout(self._mainWidget)
        grid.setSpacing(10)
        grid.addWidget(self.chatView, 1, 0, 3, 0)
        grid.addWidget(self.messageEdit, 4, 0)
        grid.addWidget(btnSendMess, 5, 0)

        self.resize(x_size, y_size)
        self.setWindowTitle(title)
        self.statusBar().showMessage('Ready')
        self.show()

    def _connect_action(self, icon, menu_key, short_cut, tip, func_connect):
        _connect = QAction(icon, menu_key, self)
        _connect.setShortcut(short_cut)
        _connect.setStatusTip(tip)
        _connect.triggered.connect(func_connect)
        return _connect

    def _do_action(self, kind, v):
        if kind == 'text':
            selected_text = self.messageEdit.textCursor().selectedText()
            self.messageEdit.textCursor().insertHtml('<{t}>{text}</{t}>'.format(text=selected_text, t=v))
        if kind == 'smile':
            pass
        if kind == 'button':
            if v == 'Send':
                #textBuf = self.chatView.toHtml()
                self.chatView.append(self.messageEdit.toHtml())
                # self.messageEdit.textCursor().select(QTextCursor.Document)
                # self.messageEdit.textCursor().removeSelectedText()
                self.messageEdit.selectAll()
                # self.messageEdit.cut()
                self.messageEdit.clear()

    def showEvent(self, e):
        self.messageEdit.setFocus()

    # def enterPressed(self):
    #     textBuf = self.chatView.toPlainText()
    #     self.chatView.setText(textBuf + self.messageEdit.text())
    #     QMessageBox.question(self, 'Message', self.messageEdit.text(), QMessageBox.Ok)
    #     self.messageEdit.setText('')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    newChat = Chat()
    sys.exit(app.exec_())