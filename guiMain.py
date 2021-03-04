from SearchInQuran import *
from gui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Window(QtWidgets.QDialog):
    resList = []
    soraNames = ['a','b','c']
    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.soraNames)
        #self.ui.comboBox.currentIndexChanged.connect(self.selectionChange)
        self.ui.pushButton.clicked.connect(self.doSearch)
        self.ui.listView.clicked.connect(self.listclicked)
        
    def doSearch(self):
        u = self.ui.textEdit.text()
        ob = SearchInQuran()
        res = ob.searchInAllSouar(u)

        countRes = 0
        self.resList = []
        itemX = []
        for i in res:
                countRes=countRes+len(i[2])
                tmp0 = str(i[0])
                tmp1 = str(i[1])
                for j in i[2]:
                    for k, l in j.items():
                        tmp2 = str(k)
                        tmp3 = str(l)
                        itemX = [tmp0,tmp1, tmp2, tmp3]
                        self.resList.append(itemX); 
        
        model = QtGui.QStandardItemModel()
        model.clear()
        
        for f in self.resList:
            tmp = QtGui.QStandardItem(str(f[1]) + " : " + str(f[2]))
            model.appendRow(tmp)
               
        
        self.ui.listView.setModel(model)
        
        if countRes == 0:
            self.ui.label_3.setText(str(countRes))
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle('Error')
            mb.setText('لا يوجد نتائج')
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec()
        else:
            self.ui.label_3.setText(str(countRes))
            self.ui.label_5.setText(str(res[0][0]))
            self.ui.plainTextEdit.setPlainText(self.resList[0][3])

        '''
        self.ui.label_7.setText(w[0])
        self.ui.label_9.setText("")
        '''
    def listclicked(self, item):
        indexResult = int(item.row())
        self.ui.plainTextEdit.setPlainText(self.resList[indexResult][3])
        self.ui.label_5.setText(self.resList[indexResult][0])

'''
    def selectionchange(self,i):
      print "Items in the list are :"
		
      for count in range(self.cb.count()):
         print self.cb.itemText(count)
      print "Current index",i,"selection changed ",self.cb.currentText()
        
'''

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
