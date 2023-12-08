from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QComboBox, QVBoxLayout, QLabel
import sys
from video_converter import VideoConverter
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QUrl
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.init_ui()

    def init_ui(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a combobox for conversion format
        conversion_formats = ["VP9", "VP8", "H.265", "AV1"]
        format_label = QLabel("Choose codec: ")
        self.format_combobox = QComboBox()
        self.format_combobox.addItems(conversion_formats)
        layout.addWidget(format_label)
        layout.addWidget(self.format_combobox)

        # Create a button
        button = QPushButton("Choose File", self)
        button.clicked.connect(self.choose_file)

        layout.addWidget(button)

        # Create a label to display the selected file path
        self.file_label = QLabel(self)
        layout.addWidget(self.file_label)


        #Create a button to start the conversion
        convert_button = QPushButton("Convert", self)
        convert_button.clicked.connect(self.convert_file)
        layout.addWidget(convert_button)

        # Create a label to display the final file path
        self.output_file_label = QLabel(self)
        layout.addWidget(self.output_file_label)

        # Create a loading animation
        self.gif_label = QLabel(self)
        self.movie = QMovie("loading.gif")
        self.gif_label.setMovie(self.movie)
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.movie.start()

        layout.addWidget(self.gif_label)

        self.gif_label.hide()

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("/home/albert/repos/SCAV-Albert_Santos/SP3/oh-yeah.mp3")))

        self.well_done_label = QLabel(self)
        self.movie_well_done = QMovie("well_done.gif")
        self.well_done_label.setMovie(self.movie_well_done)
        self.well_done_label.setAlignment(Qt.AlignCenter)
        self.movie_well_done.start()
        layout.addWidget(self.well_done_label)
        self.well_done_label.hide()

        # Set the window title
        self.setWindowTitle("Video Processor")

        # Set the window size
        self.resize(300, 150)
        
        # Set the window position
        self.move(300, 300)
        
        # Set the layout for the main window
        self.setLayout(layout)

    def choose_file(self):
        # Open a file dialog and get the selected file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName()

        # Get the selected conversion format
        # conversion_format = self.format_combobox.currentText()

        # Update the label text with the selected file path and conversion format
        self.file_label.setText("Selected File: " + file_path )
        self.well_done_label.hide()
        


    def convert_file(self):
        self.well_done_label.hide()

        # Get the selected file path
        file_path = self.file_label.text().split(": ")[1]
        vc = VideoConverter(file_path)

        # Get the selected conversion format
        conversion_format = self.format_combobox.currentText()

        # Create the output file path
        self.output_file_path = None

        # Create the conversion thread
        self.conversion_thread = ConversionThread(vc, conversion_format)
        self.conversion_thread.finished.connect(self.on_conversion_finished)

        # Start the conversion thread
        self.conversion_thread.start()

        # Show the loading animation
        self.show_loading_animation()


    def show_loading_animation(self):
        #
        self.gif_label.show()


    def on_conversion_finished(self, output_file_path):
        # Hide the loading animation
        self.hide_loading_animation()

        # Update the label text with the final file path
        self.output_file_label.setText("Final File: " + output_file_path)
        self.output_file_path = output_file_path
        self.well_done_label.show()



    def hide_loading_animation(self):
        self.gif_label.hide()

    def well_done_animation(self):
        self.well_done_label.show()
        self.mediaPlayer.play()





class ConversionThread(QThread):
    finished = pyqtSignal(str)
    def __init__(self, vc, conversion_format):
        super().__init__()
        self.vc = vc
        self.conversion_format = conversion_format

    def run(self):
        # Perform the conversion
        print("Converting the video...")
        output_file_path = self.vc.convert_codec(self.conversion_format)
        print("Done!")

        self.finished.emit( output_file_path)

def main():
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MyWindow()
    window.show()

    # Run the application
    app.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
