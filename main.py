import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from models import VotingModel
from gui import Ui_MainWindow

class VotingApp(QMainWindow):
    def __init__(self):
        """Initialize the VotingApp and set up UI."""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = VotingModel()

        self.ui.btn_submit_vote.clicked.connect(self.submit_vote)

    def submit_vote(self):
        """Handle vote submission."""
        voter_id = self.ui.line_edit_id.text().strip()
        candidate = None

        if not voter_id.isdigit():
            self.show_message("Error", "Please enter a valid numeric ID!", "error")
            return

        if self.ui.radio_jane.isChecked():
            candidate = "Jane"
        elif self.ui.radio_john.isChecked():
            candidate = "John"

        if not voter_id:
            self.show_message("Error", "Please enter a valid ID!", "error")
            return

        if not candidate:
            self.show_message("Error", "Please select a candidate!", "error")
            return

        if self.model.has_already_voted(voter_id):
            self.show_message("Error", "You have already voted!", "error")
            return

        self.model.record_vote(voter_id, candidate)

        self.show_message("Success", "Your vote has been recorded!", "info")
        self.model.clear_fields()  # Clear input fields

    def show_message(self, title, message, message_type):
        """Display an informational/error message."""
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)

        if message_type == "error":
            msg.setIcon(QMessageBox.Icon.Critical)
        else:
            msg.setIcon(QMessageBox.Icon.Information)

        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec())





