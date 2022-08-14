from re import T
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import PIL
from PIL import Image
import os
import sys
import os
# os.chdir(sys._MEIPASS)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Zip It ©️ Ankur Sarkar 2022'
        self.left = 20
        self.top = 50
        self.imgWidth = 0
        self.compressWidth = 0
        self.statusBar().showMessage("")
        self.statusBar().setObjectName("status")
        self.width = 400
        self.height = 700
        self.setFixedSize(self.width, self.height)
        self.setObjectName("mainWindow")

        stylesheet = ""
        with open("styles.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # ............................. Introduction frame .....................................
        self.intro = QFrame(self)
        self.intro.setObjectName("intro")
        self.intro.move(50, 40)

        self.introText = QLabel(self.intro)
        self.introText.setText("Hello World!! This is Ankur Sarkar a 3rd Year\nUndergrad pursuing B.Tech in ECE from\nJIS College Of Engineering. This Project is\nabout a GUI File Compression Software that\nis able to reduce file size upto 90% of it's\nOriginal Size. The Compression Algorithm is\nbased on Huffman's Algorithm and whole\ncode is written using PYTHON and PyQT5")
        self.introText.setObjectName("introtext")
        self.introText.move(20, 20)

        # ............................. single compress frame .....................................
        self.single = QFrame(self)
        self.single.setObjectName("compress")
        self.single.move(50, 125 + 180)
        self.single.mousePressEvent = self.singleClicked

        self.singleText = QLabel(self.single)
        self.singleText.setText("Compress a Single Image")
        self.singleText.setObjectName("heading")
        self.singleText.move(40, 20)

        self.singleParaText = QLabel(self.single)
        self.singleParaText.setText("Click here to Compress a Single Image")
        self.singleParaText.setObjectName("para")
        self.singleParaText.move(25, 60)

        # ............................ batch compress frame .......................................
        self.batch = QFrame(self)
        self.batch.setObjectName("compress")
        self.batch.move(50, 325 + 180)
        self.batch.mousePressEvent = self.batchClicked

        self.batchText = QLabel(self.batch)
        self.batchText.setText("Compress Multiple Images")
        self.batchText.setObjectName("heading")
        self.batchText.move(35, 20)

        self.batchParaText = QLabel(self.batch)
        self.batchParaText.setText(
            "Click here to Compress Multiple Images")
        self.batchParaText.setObjectName("para")
        # self.batchParaText.wordWrap()
        self.batchParaText.move(20, 60)

        # ................................. single frame expanded .................................
        self.singleExpanded = QFrame(self)
        self.singleExpanded.setObjectName("expanded")
        self.singleExpanded.move(50, 125)
        self.singleExpanded.setVisible(False)

        self.singleExpandedText = QLabel(self.singleExpanded)
        self.singleExpandedText.setText("Single Compression Window")
        self.singleExpandedText.setObjectName("heading")
        self.singleExpandedText.move(45, 10)

        self.back = QLabel(self.singleExpanded)
        self.back.move(15, 8)
        self.back.setObjectName("back")
        self.back.setTextFormat(Qt.RichText)
        self.back.setText("&#8592;")
        self.back.mousePressEvent = self.arrow

        self.singleLabel = QLabel(self.singleExpanded)
        self.singleLabel.setText("Select Image Path")
        self.singleLabel.setObjectName("pathTxt")
        self.singleLabel.move(80, 60)

        self.imagePath = QLineEdit(self.singleExpanded)
        self.imagePath.setObjectName("path")
        self.imagePath.move(30, 105)

        self.btn = QPushButton(self.singleExpanded)
        self.btn.setText("Browse")
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.selectFile)
        self.btn.move(220, 105)

        self.singleQuality = QLabel(self.singleExpanded)
        self.singleQuality.setText("Choose Image Quality")
        self.singleQuality.setObjectName("pathTxt")
        self.singleQuality.move(65, 170)

        self.qualityPath = QLineEdit(self.singleExpanded)
        self.qualityPath.setObjectName("path")
        self.qualityPath.move(30, 210)

        self.combo = QComboBox(self.singleExpanded)
        self.combo.addItem("High")
        self.combo.addItem("Medium")
        self.combo.addItem("Low")
        self.combo.currentIndexChanged.connect(self.comboValue)
        self.combo.setObjectName("combo")
        self.combo.move(210, 210)

        self.compressbtn = QPushButton(self.singleExpanded)
        self.compressbtn.setText("Compress Image")
        self.compressbtn.setObjectName("compressBtn")
        self.compressbtn.clicked.connect(self.resizePic)
        self.compressbtn.move(61, 270)

        # ................................. batch frame expanded .................................
        self.batchExpanded = QFrame(self)
        self.batchExpanded.setObjectName("expanded")
        self.batchExpanded.move(50, 125)
        self.batchExpanded.setVisible(False)

        self.batchExpandedText = QLabel(self.batchExpanded)
        self.batchExpandedText.setText("Batch Compression Window")
        self.batchExpandedText.setObjectName("heading")
        self.batchExpandedText.move(45, 10)

        self.back2 = QLabel(self.batchExpanded)
        self.back2.move(15, 8)
        self.back2.setObjectName("back")
        self.back2.setTextFormat(Qt.RichText)
        self.back2.setText("&#8592;")
        self.back2.mousePressEvent = self.arrow

        self.sourceLabel = QLabel(self.batchExpanded)
        self.sourceLabel.setText("Select Source Directory")
        self.sourceLabel.setObjectName("pathTxt")
        self.sourceLabel.move(65, 50)

        self.srcimgPath = QLineEdit(self.batchExpanded)
        self.srcimgPath.setObjectName("path")
        self.srcimgPath.move(30, 95)

        self.sourceBtn = QPushButton(self.batchExpanded)
        self.sourceBtn.setText("Browse")
        self.sourceBtn.setObjectName("srcbtn")
        self.sourceBtn.clicked.connect(self.selectFolder)
        self.sourceBtn.move(220, 95)

        self.destLabel = QLabel(self.batchExpanded)
        self.destLabel.setText("Select Destination Directory")
        self.destLabel.setObjectName("pathTxt")
        self.destLabel.move(45, 140)

        self.dirimgPath = QLineEdit(self.batchExpanded)
        self.dirimgPath.setObjectName("path")
        self.dirimgPath.move(30, 180)

        self.destBtn = QPushButton(self.batchExpanded)
        self.destBtn.setText("Browse")
        self.destBtn.setObjectName("dirbtn")
        self.destBtn.clicked.connect(self.selectFolder)
        self.destBtn.move(220, 180)

        self.batchQuality = QLabel(self.batchExpanded)
        self.batchQuality.setText("Choose Image Quality")
        self.batchQuality.setObjectName("pathTxt")
        self.batchQuality.move(70, 230)

        self.batchqualityPath = QLineEdit(self.batchExpanded)
        self.batchqualityPath.setObjectName("path")
        self.batchqualityPath.move(30, 270)

        self.batchcombo = QComboBox(self.batchExpanded)
        self.batchcombo.addItem("High")
        self.batchcombo.addItem("Medium")
        self.batchcombo.addItem("Low")
        self.batchcombo.setObjectName("combo")
        self.batchcombo.currentIndexChanged.connect(self.comboValue)
        self.batchcombo.move(210, 270)

        self.batchCompressBtn = QPushButton(self.batchExpanded)
        self.batchCompressBtn.setText("Compress Image")
        self.batchCompressBtn.clicked.connect(self.resizeDir)
        self.batchCompressBtn.setObjectName("compressBtn")
        self.batchCompressBtn.move(61, 320)

        # ..........................................................................................
        self.show()

    def selectFile(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Choose a File", "", "All Files (*);;JPG Files (*.jpg);;PNG Files (*.png)")
        if fileName:
            # print(fileName)
            self.imagePath.setText(fileName)
            img = Image.open(fileName)
            self.imgWidth = img.width
            self.compressWidth = self.imgWidth
            self.qualityPath.setText(str(self.imgWidth))

    def selectFolder(self):
        folder = str(QFileDialog.getExistingDirectory(
            self, "Select the Folder"))
        if (self.sender().objectName() == "srcbtn"):  # if selected dir is src dir
            self.srcimgPath.setText(folder)
        else:                                         # if selected dir is dest dir
            self.dirimgPath.setText(folder)

        try:
            files = os.listdir(folder)
            self.statusBar().showMessage("")
            if (self.sender().objectName() == "srcbtn"):
                firstPic = folder + '/' + files[0]
                img = Image.open(firstPic)
                self.imgWidth = img.width
                self.compressWidth = self.imgWidth
                self.batchqualityPath.setText(str(self.imgWidth))
        except Exception as e:
            self.statusBar().showMessage("Error in Selecting Folder")

    def singleClicked(self, event):
        self.single.setVisible(False)
        self.batch.setVisible(False)
        self.singleExpanded.setVisible(True)
        self.batchExpanded.setVisible(False)
        self.intro.setVisible(False)

    def batchClicked(self, event):
        self.single.setVisible(False)
        self.batch.setVisible(False)
        self.singleExpanded.setVisible(False)
        self.batchExpanded.setVisible(True)
        self.intro.setVisible(False)

    def arrow(self, event):
        self.single.setVisible(True)
        self.batch.setVisible(True)
        self.singleExpanded.setVisible(False)
        self.batchExpanded.setVisible(False)
        self.intro.setVisible(True)

    def comboValue(self):
        if(self.combo.currentText() == "High"):
            self.qualityPath.setText(str(self.imgWidth))
            self.compressWidth = self.imgWidth
        if(self.combo.currentText() == "Medium"):
            self.qualityPath.setText(str(int(self.imgWidth/2)))
            self.compressWidth = int(self.imgWidth/2)
        if(self.combo.currentText() == "Low"):
            self.qualityPath.setText(str(int(self.imgWidth/4)))
            self.compressWidth = int(self.imgWidth/4)

        if(self.batchcombo.currentText() == "High"):
            self.batchqualityPath.setText(str(self.imgWidth))
            self.compressWidth = self.imgWidth
        if(self.batchcombo.currentText() == "Medium"):
            self.batchqualityPath.setText(str(int(self.imgWidth/2)))
            self.compressWidth = int(self.imgWidth/2)
        if(self.batchcombo.currentText() == "Low"):
            self.batchqualityPath.setText(str(int(self.imgWidth/4)))
            self.compressWidth = int(self.imgWidth/4)

    def resizePic(self):
        oldPic = self.imagePath.text()

        # if oldPic[-4:] != '.jpg' or oldPic[-4:] != '.png' or oldPic[-5:] != '.jpeg' or oldPic[-4:] != '.JPG' or oldPic[-4:] != '.PNG' or oldPic[-5:] != '.JPEG':
        #     self.statusBar().showMessage("Please choose a Valid Image")
        #     return

        # print(self.compressWidth)
        dir = oldPic.split("/")
        # print(dir)
        tmp = str(dir[-1:])
        tmp2 = str(tmp[2:-2])
        fileExtension = tmp2[-4:]
        newPicName = str(tmp[2:-6]) + "_compressed" + fileExtension
        # print(newPicName)
        newPicDir = ""  # new pic location
        for directory in dir[:-1]:
            newPicDir = newPicDir + directory + "/"
        # print("newPicDir: " + newPicDir)
        newPic = newPicDir + newPicName
        # print("newPic: " + newPic)

        # print("org width: " + str() +
        #       " AND compress width: " + str(self.compressWidth))

        try:
            self.compress(oldPic, newPic, int(self.qualityPath.text()))
            self.statusBar().showMessage("Image Compressed")
            orgImgSize = 1
            compressImgSize = 1
        except:
            self.statusBar().showMessage("Error in choosing an Image")

    def resizeDir(self):
        srcDir = self.srcimgPath.text()
        destDir = self.dirimgPath.text()
        files = os.listdir(srcDir)

        if srcDir == "" or destDir == "":
            self.statusBar().showMessage("Please choose both the Folders Folder")
            return

        i = 0
        for file in files:
            i += 1
            if file[-4:] == '.jpg' or file[-4:] == '.png' or file[-5:] == '.jpeg' or file[-4:] == '.JPG' or file[-4:] == '.PNG' or file[-5:] == '.JPEG':
                oldPic = srcDir + "/" + file
                newPic = destDir + "/" + file
                img = Image.open(oldPic)
                self.imgWidth = img.width
                self.batchqualityPath.setText(str(self.imgWidth))
                self.compress(oldPic, newPic, int(
                    self.batchqualityPath.text()))
                totalImg = len(files)
                count = i
                percentDone = int((count/totalImg)*100)
                self.statusBar().showMessage(str(percentDone) + "% Images Compressed")

            else:
                continue
        self.statusBar().showMessage("All images Compressed")

    # Compression Algorithm
    def compress(self, old_pic, new_pic, mywidth):
        try:
            img = Image.open(old_pic)
            wpercent = (mywidth/float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
            img.save(new_pic)
        except Exception as e:
            self.statusBar().showMessage("Error Message: " + e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
