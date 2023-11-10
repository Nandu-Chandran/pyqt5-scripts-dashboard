import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton,QFileDialog
import subprocess


class MenuDescriptionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Tab widget for menu items and descriptions
        tab_widget = QTabWidget()

        # Create tabs for menu items
        merge_tab = QWidget()
        combine_tab = QWidget()
        insert_tab = QWidget()
        delete_tab = QWidget()

        # Add menu items as tabs
        tab_widget.addTab(merge_tab, "Merge")
        tab_widget.addTab(combine_tab, "Combine")
        tab_widget.addTab(insert_tab, "Insert")
        tab_widget.addTab(delete_tab, "Delete")

        # Create description labels and run buttons for each tab
        self.merge_description = QLabel("Combines the selected items into one.")
        self.merge_file_button_1 = QPushButton("Select File 1")
        self.merge_file_button_1.clicked.connect(self.browse_file_1)

        self.merge_file_button_2 = QPushButton("Select File 2")
        self.merge_file_button_2.clicked.connect(self.browse_file_2)
        self.display_selected_files = QLabel("Selected Files:")

        self.merge_run_button = QPushButton("Run Merge")
        self.merge_run_button.clicked.connect(lambda: self.run_script("Merge"))

        self.combine_description = QLabel("Merges two or more elements into a single element.")
        self.combine_run_button = QPushButton("Run Combine")
        self.combine_run_button.clicked.connect(lambda: self.run_script("Combine"))

        self.insert_description = QLabel("Adds an item into the current selection.")
        self.insert_run_button = QPushButton("Run Insert")
        self.insert_run_button.clicked.connect(lambda: self.run_script("Insert"))

        self.delete_description = QLabel("Removes the selected item from the list.")
        self.delete_run_button = QPushButton("Run Delete")
        self.delete_run_button.clicked.connect(lambda: self.run_script("Delete"))

        # Add descriptions and run buttons to respective tabs
        merge_tab.layout = QVBoxLayout()
        merge_tab.layout.addWidget(self.merge_description)
        merge_tab.layout.addWidget(self.merge_file_button_1)
        merge_tab.layout.addWidget(self.merge_file_button_2)
        merge_tab.layout.addWidget(self.display_selected_files)
        merge_tab.layout.addWidget(self.merge_run_button)
        merge_tab.setLayout(merge_tab.layout)

        combine_tab.layout = QVBoxLayout()
        combine_tab.layout.addWidget(self.combine_description)
        combine_tab.layout.addWidget(self.combine_run_button)
        combine_tab.setLayout(combine_tab.layout)

        insert_tab.layout = QVBoxLayout()
        insert_tab.layout.addWidget(self.insert_description)
        insert_tab.layout.addWidget(self.insert_run_button)
        insert_tab.setLayout(insert_tab.layout)

        delete_tab.layout = QVBoxLayout()
        delete_tab.layout.addWidget(self.delete_description)
        delete_tab.layout.addWidget(self.delete_run_button)
        delete_tab.setLayout(delete_tab.layout)

        # Add the tab widget to the main layout
        layout.addWidget(tab_widget)
        self.setLayout(layout)
        self.setWindowTitle('Menu Description')

    def run_script(self, action):
        # Perform actions based on the selected menu item
        if action == "Merge":
            # Run merge script or function
            print("Running Merge action")
            result = subprocess.run(["python", "excel-merge.py"], text=True, capture_output=True)
            if result:
                print("Merge completed")
        elif action == "Combine":
            # Run combine script or function
            print("Running Combine action")
        elif action == "Insert":
            # Run insert script or function
            print("Running Insert action")
        elif action == "Delete":
            # Run delete script or function
            print("Running Delete action")

    def browse_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.AnyFile)
        dlg.setNameFilter("Text files (*.txt)")
        filenames = []
		
        if dlg.exec():
            filenames = dlg.selectedFiles()
            print("Selected file:", filenames[0])

    def browse_file_1(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("All Files (*.*)")

        if file_dialog.exec():
            self.selected_file_1 = file_dialog.selectedFiles()[0]
            self.update_display()

    def browse_file_2(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("All Files (*.*)")

        if file_dialog.exec():
            self.selected_file_2 = file_dialog.selectedFiles()[0]
            self.update_display()
    
    def update_display(self):
        self.display_selected_files.setText(f"Selected Files:\nFile 1: {self.selected_file_1}\nFile 2: {self.selected_file_2}")
        
def main():
    app = QApplication(sys.argv)
    widget = MenuDescriptionWidget()
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
