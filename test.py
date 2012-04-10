#!/usr/bin/python
# Using Python Image Library (PIL)
# Download at http://www.pythonware.com/products/pil/]

import epub
import sys
import math
import os
import base64
import time
import subprocess
from PyQt4 import QtCore, QtGui, QtNetwork
from windowUi import Ui_MainWindow
from StringIO import StringIO
from PIL import Image


class Main(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.progname = "iOS2M"
        self.version = "1.0"
        self.author = "Stunjelly eBook Services"
        self.setWindowTitle(self.progname + " " + self.version + " - " + self.author)
        self.workingdir = ""
        epub.EpubFile
        self.ui.btnopen.clicked.connect(self.GetEPUBsFromFolder)
        self.ui.btnabout.clicked.connect(self.AboutDialog)
        self.ui.btnfix.clicked.connect(self.FixEPUBs)
        self.ui.treeWidget.setColumnWidth(0, 230)
        self.warningcolor = QtGui.QColor("yellow")
        self.okcolor = QtGui.QColor("green")
        self.errorcolor = QtGui.QColor("red")
        self.filesToFix = []
        
        self.DirEpub = ""
        
    def FixEPUBs(self):
        self.ui.btnopen.setEnabled(False)
        self.ui.btnabout.setEnabled(False)
        self.ui.btnfix.setEnabled(False)
        if len(self.filesToFix) > 0:
            for path, treeItem in self.filesToFix:
                test = epub.EpubFile(path)
                for item in test.opf.manifest:
                    if str.startswith(str(item.mimetype), "image"):
                        fakefile = StringIO(item.read())
                        img = Image.open(fakefile)
                        if self.testImage(img):
                            area = 1980000
                            width, height = img.size
                            resize = math.sqrt(area)/math.sqrt(width*height)
                            width = math.floor(width*resize)
                            height = math.floor(height*resize)
                            img.resize((int(width), int(height)), Image.ANTIALIAS)
                            #this is borked need to rework the epub module
                            #item.write(img.tostring())
                            print "writing "+item.archloc+" to "+path
        else:
            QtGui.QMessageBox.information(self
            , "No Files To Fix"
            , "Please select a folder first"
            , QtGui.QMessageBox.Ok)
        
        self.ui.btnopen.setEnabled(True)
        self.ui.btnabout.setEnabled(True)
        self.ui.btnfix.setEnabled(True)
    
    def AboutDialog(self):
        QtGui.QMessageBox.about(self,
                          "About " + self.progname,
                          self.progname + " " + self.version +"\n\nApple iBooks will reject any submitted EPUB to the iBookstore which doesn't meet it's criteria. This application was developed to fix EPUBs whose images pixel count exceed 2 million.\n\nIf you come across any bugs or issues with this software you can email us directly at mail@stunjelly.com\n\nCoded by Edward Knowles and Nic West of " + self.author + ".")
        
    def testImage(self, img):        
        width, height = img.size
        if width*height > 2000000:
            return True
        else:
            return False
         
    def AddEpubToList(self, epubsfolder):
        self.ui.btnopen.setEnabled(False)
        self.ui.btnabout.setEnabled(False)
        self.ui.btnfix.setEnabled(False)
        TotalImagesFix = 0
        TotalImagesFound = 0
        EpubsAffected = 0
        FilesScanned = 0
        starttime = int(time.time())
        for root, subFolders, files in os.walk(str(epubsfolder)):
            for file in files:
                fname = file
                ebook = QtGui.QTreeWidgetItem()
                if fname.endswith("epub") and not os.path.isdir(fname):
                    FilesScanned = FilesScanned + 1
                    fullfile = os.path.join(root, fname)
                    images = 0
                    images_corrected = 0
                    ebook.setText(0, fname)
                    self.ui.statusbar.showMessage("Checking " + fname + "...")
                    print "Checking " + fname + "..."
                    try:
                        test = epub.EpubFile(fullfile)
                        for item in test.opf.manifest:
                            if str.startswith(str(item.mimetype), "image"):
                                images = images+1
                                img = Image.open(StringIO(item.read()))
                                if self.testImage(img):
                                    images_corrected = images_corrected+1
                    except:
                        images_corrected = -1        
                    ebook.setText(2, str(images))
                    ebook.setText(3, str(images_corrected))
                    if images_corrected == 0:
                        ebook.setText(1, "OK")
                        ebook.setTextColor(1, self.okcolor)
                    elif images_corrected == -1:
                        ebook.setText(1, "ERROR")
                        ebook.setTextColor(1, self.errorcolor)
                    else:
                        EpubsAffected = EpubsAffected + 1
                        ebook.setText(1, "Warnings")
                        ebook.setTextColor(1, self.warningcolor)
                        self.filesToFix.append((fullfile, ebook))
                    epubsize = os.path.getsize(fullfile)
                    nicesize = self.prettySize(epubsize)
                    ebook.setText(4, nicesize)
                    TotalImagesFound = TotalImagesFound + images
                    TotalImagesFix = TotalImagesFix + images_corrected
                self.ui.treeWidget.addTopLevelItem(ebook)
                self.ui.treeWidget.repaint()
            
        endtime = int(time.time())
        timetaken = endtime - starttime
        displaytime = self.ConversionDuration(timetaken)
        self.ui.statusbar.showMessage("")
        QtGui.QMessageBox.information(self
            , "Report"
            , "EPUBs Scanned:\t" + str(FilesScanned) + "\nImages Found:\t\t" + str(TotalImagesFound) + "\nImages Over Limit:\t" + str(TotalImagesFix) + "\nEPUBs Affected:\t" + str(EpubsAffected) + "\n\nTime Taken:\t" + displaytime
            , QtGui.QMessageBox.Ok)
        
        self.ui.btnopen.setEnabled(True)
        self.ui.btnabout.setEnabled(True)
        self.ui.btnfix.setEnabled(True)

    def ConversionDuration(self, seconds):
        seconds = int(seconds)
        hours = seconds / 3600
        seconds -= 3600*hours
        minutes = seconds / 60
        seconds -= 60*minutes
        output = ""
        if int(hours) == 0:
            print ""
        else:
            output = str(int(hours)) + "h "
        if int(minutes) == 0:
            print ""
        else:
            output = output + str(int(minutes)) + "m "
        if int(seconds) == 0:
            print ""
        else:
            output = output + str(int(seconds)) + "s "
        return output

    def GetEPUBsFromFolder(self):
        #On button press, open file dialog
        epubsfolder = QtGui.QFileDialog.getExistingDirectory(self, "Choose folder containing EPUBS", 
                "",
                QtGui.QFileDialog.ShowDirsOnly
                | QtGui.QFileDialog.DontResolveSymlinks)
        if epubsfolder == "":
            print "User cancelled file dialog."
        else:
            self.workingdir = epubsfolder
            self.DirEpub = epubsfolder
            return self.AddEpubToList(epubsfolder)

    def prettySize(self, size):
        suffixes = [("B",2**10), ("K",2**20), ("MB",2**30), ("GB",2**40), ("T",2**50)]
        for suf, lim in suffixes:
            if size > lim:
                continue
            else:
                rounded = round(size/float(lim/2**10),2).__str__()
                return rounded + " " + suf
        
def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()