from os.path import expanduser

import sys

from PyQt5.QtCore import Qt, QDir

from PyQt5.QtGui import (QFont,
                         QKeySequence,
                         QTextDocument,
                         QStandardItemModel)

from PyQt5.QtWidgets import (QAction,
                             QApplication,
                             QDirModel,
                             QDockWidget,
                             QFileDialog,
                             QFileSystemModel,
                             QListWidget,
                             QMainWindow,
                             QMessageBox,
                             QPlainTextEdit,
                             QTreeView,
                             QTreeWidget,
                             QTreeWidgetItem)

# ====================================================
# BEFORE CLOSING
# ====================================================

def ask_for_confirmation():
    answer = QMessageBox.question(window, "Hello?",
                "Hey, Andres. The teacher is saying goodbye to you. Are you sure you want to exit without replying?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
    return answer


# ====================================================
# TREE VIEW
# ====================================================

class PrjTreeModel(QStandardItemModel):
    def __init__(self, parent,data):
        super(PrjTreeModel, self).__init__(parent)
        self.items = datapd.DataFrame([['HHH','BBB','RRR']],columns=['UserId','ProjectId','Status'])
        self.refreshItems()

    def refreshItems(self):
        prjId = self.items['ProjectId']
        child = ['A','B','C']
        for i,row in prjId.iteritems():
            parent = QStandardItem(row)
            for j in child:
                parent.appendRow(QStandardItem(j))
            self.appendRow(parent)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if (role == Qt.DisplayRole) and (orientation == Qt.Horizontal) and (self.items is not None):
            return self.items['UserId'][0]
        else:
            return QStandardItemModel.headerData(self, section, orientation, role)

    def dClicked(self, index):
        item = index.model().itemFromIndex(index)
        if not item.data(Qt.UserRole + 1):
            item.setData(True, Qt.UserRole + 1)
            print('open txt file:', item.text())
        else:
            print('already double-clicked')

# ====================================================
# MAIN WINDOW
# ====================================================

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        dockWidget = QDockWidget('ANDRES NO ES UN BOT', self)

        self.home = expanduser("~")

        self.raw_editor = QPlainTextEdit()

        self.model = PrjTreeModel()
        self.tree = QTreeView()
        self.model.setRootPath(QDir.currentPath())
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.home))
        self.tree.show()
        #self.tree.doubleClicked.connect(self.open_list_item)
        #self.tree.setExpandsOnDoubleClick(False)
        self.tree.resizeColumnToContents(0)
        #self.tree.rootIsDecorated()
        #self.tree.isAnimated()
        self.tree.doubleClicked.connect(self.dClicked)

        dockWidget.setWidget(self.tree)
        dockWidget.setFloating(False)

        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)

    def open_list_item(self):
        self.raw_editor.setPlainText(QTreeView.setCurrentItem().text())

    def closeEvent(self, e):
        if not raw_editor.document().isModified():
            return
        answer = ask_for_confirmation()
        if answer == QMessageBox.Save:
            if not save():
                e.ignore()
        elif answer == QMessageBox.Cancel:
            e.ignore()


# ====================================================
# NEW DOCUMENT
# ====================================================

def new_document(self):
    global file_path
    if raw_editor.document().isModified():
        answer = ask_for_confirmation()
        if answer == QMessageBox.Save:
            if not save():
                return
        elif answer == QMessageBox.Cancel:
            return
    raw_editor.clear()
    file_path = None

# ====================================================
# OPEN FILE
# ====================================================

def show_open_dialog():
    global file_path
    filename, _ = QFileDialog.getOpenFileName(window, 'Open...')
    if filename:
        file_contents = ""
        with open(filename, 'r') as f:
            file_contents = f.read()
        raw_editor.setPlainText(file_contents)
        file_path = filename

# ====================================================
# SAVE FILE
# ====================================================

def save():
    if file_path is None:
        return show_save_dialog()
    else:
        with open(file_path, 'w') as f:
            f.write(editor.toPlainText())
        raw_editor.document().setModified(False)
        return True

def show_save_dialog():
    global file_path
    filename, _ = QFileDialog.getSaveFileName(window, 'Save as...')
    if filename:
        file_path = filename
        save()
        return True
    return False

# ====================================================
# ABOUT
# ====================================================

def show_about_dialog():
    text = """
        <center>
            <h1>Andres' life matters</h1><br/>
            <img src=logo.png width=200 height=200>
        </center>
        <p>Version 0.0.1</p>
    """
    QMessageBox.about(window, "About HOLASOYANDRESENQUEPUEDOAYUDARTE", text)

'''def show_treeview(self):
    if window.tree.isVisible == False:
        window.tree.setVisible(True)'''

if __name__ == '__main__':

    # ====================================================
    # SETTINGS
    # ====================================================

    app = QApplication(sys.argv)
    app.setApplicationName("HOLASOYANDRESENQUEPUEDOAYUDARTE")

    window = MyMainWindow()
    window.setWindowTitle("HOLASOYANDRESENQUEPUEDOAYUDARTE")

    raw_editor = QPlainTextEdit()
    raw_editor.document().setDefaultFont(QFont("monospace"))
    window.setCentralWidget(raw_editor)

    # ====================================================
    # MENU
    # ====================================================

    # ====================================================
    # File
    # ====================================================

    file_menu = window.menuBar().addMenu("&File")
    file_path = None

    new_action = QAction("&New document")
    new_action.triggered.connect(new_document)
    new_action.setShortcut(QKeySequence.New)
    file_menu.addAction(new_action)

    open_action = QAction("&Open file...")
    open_action.triggered.connect(show_open_dialog)
    open_action.setShortcut(QKeySequence.Open)
    file_menu.addAction(open_action)

    save_action = QAction("&Save")
    save_action.triggered.connect(save)
    save_action.setShortcut(QKeySequence.Save)
    file_menu.addAction(save_action)

    close_action = QAction("&Close")
    close_action.triggered.connect(window.close)
    close_action.setShortcut(QKeySequence.Quit)
    file_menu.addAction(close_action)

    # ====================================================
    # Edit
    # ====================================================

    edit_menu = window.menuBar().addMenu("&Edit")

    cut_action = QAction("&Cut")
    #cut_action.triggered.connect()
    edit_menu.addAction(cut_action)

    copy_action = QAction("&Copy")
    #copy_action.triggered.connect()
    edit_menu.addAction(copy_action)

    paste_action = QAction("&Paste")
    #paste_action.triggered.connect()
    edit_menu.addAction(paste_action)

    # ====================================================
    # View
    # ====================================================

    view_menu = window.menuBar().addMenu("&View")

    show_action = QAction("&Show")
    #show_action.triggered.connect(show_treeview)

    view_menu.addAction(show_action)

    # ====================================================
    # Help
    # ====================================================

    help_menu = window.menuBar().addMenu("&Help")

    about_action = QAction("&About")
    about_action.triggered.connect(show_about_dialog)
    help_menu.addAction(about_action)

    window.show()
    sys.exit(app.exec())
