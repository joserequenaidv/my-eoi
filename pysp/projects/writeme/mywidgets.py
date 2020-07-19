import os
from os.path import expanduser, isdir
import sys

from markdown2 import Markdown
from PyQt5.QtCore import QDir, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *

from settings import *


# ====================================================
# MAIN WINDOW
# ====================================================

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.resize(SCREEN_WIDTH, SCREEN_HEIGHT) # Screen size
        self.setWindowTitle(APP_TITLE) # Screen title
        self.home = expanduser(DEFAULT_DIR) # Default directory

        # Editor Viewer
        self.raw_editor = QPlainTextEdit() # CREATION of Editor Viewer
        self.raw_editor.document().setDefaultFont(QFont(APP_FONT)) # Set FONT of Editor Viewer
        self.setCentralWidget(self.raw_editor) # Set Editor Viewer on the center of the APP
        #self.raw_editor.textChanged.connect(self.check_is_modified)

        # Main Menu
        self.create_menu_bar() # CREATION of APP Menu Bar

        # Tree Viewer
        self.treeview = MyTreeView(self) # CREATION of Tree Viewer

        # MarkDown Viewer
        self.web_engine = MyWebEngineView(self) # CREATION of MarkDown Viewer
        self.addDockWidget(Qt.RightDockWidgetArea, self.web_engine.web_dockwidget)

    def ask_for_confirmation(self):
        answer = QMessageBox.question(self,
                                      "Confirm",
                                      "You have unsaved changes. Are you sure you want to exit?",
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                                      )
        return answer

    def check_is_modified(self):
        if self.raw_editor.document().isModified():
            answer = self.ask_for_confirmation()
            if answer == QMessageBox.Save:
                if not self.save():
                    return
            elif answer == QMessageBox.Cancel:
                return
        return True

    def close_event(self, e):
        if not self.raw_editor.document().isModified():
            return
        answer = self.ask_for_confirmation()
        if answer == QMessageBox.Save:
            if not self.save():
                e.ignore()
        elif answer == QMessageBox.Cancel:
            e.ignore()

    def create_menu_bar(self):
        self.menu_bar = self.menuBar()

        self.file_menu = self.menu_bar.addMenu(FILE_TITLE)
        self.file_path = None

        self.new_action = QAction(NEWDOC_TITLE)
        self.new_action.triggered.connect(self.new_document)
        self.new_action.setShortcut(QKeySequence.New)
        self.file_menu.addAction(self.new_action)

        self.open_action = QAction(OPEN_TITLE)
        self.open_action.triggered.connect(self.show_open_dialog)
        self.open_action.setShortcut(QKeySequence.Open)
        self.file_menu.addAction(self.open_action)

        self.save_action = QAction(SAVE_TITLE)
        self.save_action.triggered.connect(self.save)
        self.save_action.setShortcut(QKeySequence.Save)
        self.file_menu.addAction(self.save_action)

        self.close_action = QAction(CLOSE_TITLE)
        self.close_action.triggered.connect(self.close_event)
        self.close_action.setShortcut(QKeySequence.Quit)
        self.file_menu.addAction(self.close_action)

        self.about_action = QAction("&About")
        self.about_action.triggered.connect(self.show_about_dialog)

        self.help_menu = self.menuBar().addMenu("&Help")
        self.help_menu.addAction(self.about_action)

# To my future self: SORRY FOR THE MESS hehe :D
# ===============================================
#   edit_menu = self.menu_bar.addMenu("&Edit")
#   cut_action = QAction("&Cut")
###cut_action.triggered.connect()
#   edit_menu.addAction(cut_action)
#   copy_action = QAction("&Copy")
###copy_action.triggered.connect()
#   edit_menu.addAction(copy_action)
#   paste_action = QAction("&Paste")
###paste_action.triggered.connect()
#   edit_menu.addAction(paste_action)
# View
#   self.view_menu = self.menu_bar.addMenu("&View")
# ==============================================

    def new_document(self):
        if self.check_is_modified() == True:
            self.raw_editor.clear()
            self.web_engine.md_to_html()
            self.file_path = None

    def open_db_click(self, index):
        path = self.treeView.model.filePath(index)
        if os.path.isfile(path):
            self.open_file(path)

    def save(self):
        if self.file_path is None:
            return self.show_save_dialog()
        else:
            with open(self.file_path, 'w') as f:
                f.write(self.raw_editor.toPlainText())
            self.raw_editor.document().setModified(False)
            return True

    def show_about_dialog(self):
        text = """
            <center>
                <h1>Writeme Editor</h1><br/>
                <img src=images/logo.png width=300 height=300>
            </center>
            <p>Version 0.0.1</p>
        """
        QMessageBox.about(self, "About WRITEME", text)

    def show_open_dialog(self):
        if self.check_is_modified() == True:
            filename, _ = QFileDialog.getOpenFileName(self, "Open...")
            if filename:
                file_contents = ""
                with open(filename, "r") as f:
                    file_contents = f.read()
                self.raw_editor.setPlainText(file_contents)
                self.file_path = filename
                self.web_engine.md_to_html()

    def show_save_dialog(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save as...')
        if filename:
            self.file_path = filename
            self.save()
            return True
        return False

# ====================================================
# TREE VIEW
# ====================================================
class MyTreeView(QTreeView):
    def __init__(self, main):
        super().__init__()
        self.path = expanduser(DEFAULT_DIR)
        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)

        self.main = main

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))
        self.tree.setSortingEnabled(True)

        self.tree_dockwidget = QDockWidget("File Explorer", self)
        self.tree_dockwidget.setWidget(self.tree)
        self.tree_dockwidget.setAllowedAreas(Qt.LeftDockWidgetArea)
        main.addDockWidget(Qt.LeftDockWidgetArea, self.tree_dockwidget)
        self.tree.doubleClicked.connect(self.open_file_in_tree)

    def open_file_in_tree(self, main):
        if self.main.check_is_modified() == True:
            index = self.tree.currentIndex()
            filename = self.model.filePath(index)
            isDirectory = isdir(filename)
            if isDirectory == True:
                return
            else:
                file_contents = ""
                with open(filename, "r") as f:
                    file_contents = f.read()
                self.main.raw_editor.setPlainText(file_contents)
                main.file_path = filename
                self.main.web_engine.md_to_html()

# ====================================================
# MARKDOWN VIEWER :P (thanks to Álex)
# ====================================================

class MyWebEngineView(QWebEngineView):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.view = QWebEngineView()
        self.update_button(main, parent=QAction)
        # To-do: --> self.auto_update

        self.web_dockwidget = QDockWidget(MDV_TITLE, self)
        self.web_dockwidget.setWidget(self.view)
        self.web_dockwidget.setAllowedAreas(Qt.RightDockWidgetArea)
        self.web_dockwidget.setMinimumWidth(MDV_MINIMUM_WIDTH)

    def update_button(self, main, parent):
        update_button = QPushButton(main)
        update_button.setText("Update")
        update_button.setShortcut(QKeySequence.Refresh)
        update_button.clicked.connect(self.md_to_html)
        main.menuBar().setCornerWidget(update_button, corner=Qt.TopRightCorner)

    def md_to_html(self):
        md = Markdown()
        raw_text = self.main.raw_editor.toPlainText()
        content = md.convert(raw_text)
        self.view.setHtml(content)
