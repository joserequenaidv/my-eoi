from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
app.setApplicationName("PyNotepad")
editor = QPlainTextEdit()
window = QMainWindow()
window.setWindowTitle("PyNotepad")
window.setCentralWidget(editor)

#FILE
file_menu = window.menuBar().addMenu("&File")
#Open file
def show_open_dialog():
    filename, _ = QFileDialog.getOpenFileName(window, 'Open file', '/home/joserequenaidv')
    if filename:
        file_contents = open(filename, 'r').read()
        editor.setPlainText(file_contents)

open_action = QAction("&Open file...")
open_action.triggered.connect(show_open_dialog)
open_action.setShortcut(QKeySequence.Open)
file_menu.addAction(open_action)

#Save as
def show_save_dialog():
    global file_path
    filename, _ = QFileDialog.getSaveFileName(window, 'Save as...')
    if filename:
        file_path = filename
        save()

save_action = QAction("&Save as...")
save_action.triggered.connect(show_save_dialog)
file_menu.addAction(save_action)

#Save
def auto_save():
    global file_path
    if file_path == None:
        show_save_dialog()
    else:
        with open(filename, 'w') as f:
                f.write(editor.toPlainText())
   
save_action = QAction("&Save as...")
save_action.triggered.connect(show_save_dialog)
file_menu.addAction(save_action)


#Close app
close_action = QAction("&Close")
close_action.triggered.connect(window.close)
file_menu.addAction(close_action)

#ABOUT
def show_about_dialog():
    text = """
        <center>
        <h1>PyNotepad</h1>
            &#8291;
            <img src="shield.png" width=100 heigth=100>
        </center>
        <p>Version 0.0.1</p>
    """
    QMessageBox.about(window, "About PyNotepad", text)

help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
about_action.triggered.connect(show_about_dialog)
help_menu.addAction(about_action)

window.show()
app.exec()
