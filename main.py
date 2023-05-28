from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys

# Library for downloading YouTube
from pytube import YouTube


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("MainUI.ui", self)

        # What happens if the user presses the download button
        self.pushButton.clicked.connect(self.DownloadVideo)

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
                pass
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
