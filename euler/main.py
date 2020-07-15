import sys, app, PyQt5


def main():
    application = PyQt5.QtWidgets.QApplication(sys.argv)
    window = app.MainApp()
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()
