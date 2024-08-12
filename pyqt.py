import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLineEdit,QVBoxLayout,QWidget,QLabel

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 200)
        self.num1 = QLineEdit()
        self.num2 = QLineEdit()
        self.result = QLabel("Result: ")
        layout = QVBoxLayout()
        layout.addWidget(self.num1)
        layout.addWidget(self.num2)
        layout.addWidget(self.result)
        layout.addWidget(QPushButton("Add", clicked=self.add))
        layout.addWidget(QPushButton("Subtract", clicked=self.subtract))
        layout.addWidget(QPushButton("Multiply", clicked=self.multiply))
        layout.addWidget(QPushButton("Divide", clicked=self.divide))
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def add(self):
        self.calculate('+')
    def subtract(self):
        self.calculate('-')
    def multiply(self):
        self.calculate('*')
    def divide(self):
        self.calculate('/')
    def calculate(self, operation):
        try:
            n1 = float(self.num1.text())
            n2 = float(self.num2.text())
            if operation == '+':
                res = n1 + n2
            elif operation == '-':
                res = n1 - n2
            elif operation == '*':
                res = n1 * n2
            elif operation == '/':
                res = "Error (Division by zero)" if n2 == 0 else n1 / n2
            self.result.setText("Result: " + str(res))
        except ValueError:
            self.result.setText("Error (Invalid input)")
app = QApplication(sys.argv)
calc = Calc()
calc.show()
sys.exit(app.exec_())

