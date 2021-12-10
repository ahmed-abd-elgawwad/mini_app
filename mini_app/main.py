# first import the libiraries
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from os.path import splitext
from os import path
import sys
# the pytesseract module
import pytesseract as pt
# connect the modlue with the engine form the computer [ note the path migth change depending on you location]
pt.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract"
# the following line take 
FORM_CLASS,_ =loadUiType(path.join(path.dirname(__file__),"gui.ui"))
class MainApp(QMainWindow,FORM_CLASS):
    def __init__(self,parent =None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui_settings()
        self.buttons()
    # handling the ui settings
    def ui_settings(self):
        # set the size of the window
        self.setFixedSize(525,425)
        # the program title
        self.setWindowTitle("Get the text")
    # hindeling button and connecting them
    def buttons(self):
        # connect the select button with the function so that when cliking it it will run the function
        self.select.clicked.connect(self.browse)
        # connect the select button with the function so that when cliking it it will run the function and get the text into the text space
        self.extract.clicked.connect(self.get_text)
    # function to browse and select the location of the image
    def browse(self):
        # to start form the current directory
        directory = './'
        # only choose image with (png,jpj,gif) extension
        filter_mask = "PNG/JPG/JIF files (*.png *.jpg *.gif)"
        # to show the location window and get the location
        self.file_location= QFileDialog.getOpenFileName(None,"open file",directory,filter_mask)
        # splittext -> function to split the location into name and extension
        file_name,extension = splitext(self.file_location[0])
        # only get the name of the image
        self.si_name=file_name.split("/")[-1].replace(extension," ")
        # the extention of the image
        self.si_extension = extension
        self.lineEdit.setText(f"{self.si_name}{self.si_extension}")
        
    def get_text(self):
        try:
            # get the text of the image by setting the location of the image
            self.content=pt.image_to_string(self.file_location[0])
            # put the text we extract into the texeara
            self.textEdit.setText(self.content)
        except:
            QMessageBox.warning(self, "Error", "there is some errors.fix later")
# to run the program
def main():
    app =QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__=="__main__":
    main()