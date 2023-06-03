from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QKeySequence

# Library for downloading YouTube
from pytube import YouTube


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("MainUI.ui", self)

        # What happens if the user presses the download button and presses commandLinkButton
        self.pushButton.clicked.connect(self.DownloadVideo)
        # self.pushButton.setShortcut(QKeySequence(Qt.Key_Enter))
        self.commandLinkButton.clicked.connect(self.open_link)
        #self.commandLinkButton.setShortcut(QKeySequence(Qt.Key_I))

    def DownloadVideo(self):
        try:
            # If the radio button is selected
            if self.radioButton.isChecked() == True:
                url = self.lineEdit.text()
                exit_path = self.lineEdit_2.text()
                video = YouTube(url)
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=exit_path)

            # If the audio only radio button is selected
            if self.radioButton_2.isChecked() == True:
                url = self.lineEdit.text()
                exit_path = self.lineEdit_2.text()
                video = YouTube(url)
                stream = video.streams.get_audio_only()
                stream.download(output_path=exit_path)
            # Otherwise, if nothing happens

            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText(
                    "لطفا تمامی فیلد هار پر نمایید و فرمت فایل خود را انتخاب نمایید!")
                msgBox.setWindowTitle("خطا")
                msgBox.setStandardButtons(QMessageBox.Ok)
                # Add this line to prevent closing the application after showing the warning message box.
                msgBox.exec_()
        except Exception as e:
            print(e)

    def open_link (self):
        try:
            webbrowser = open_link
            webbrowser.open_new("https://github.com/iMaHdI78")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()

