import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(450, 600)
        self.setMinimumSize(450, 600)

        self.nums_entered = ""
        self.operand = []
        self.operator = []
        self.op_clicked_last = False
        self.equal_clicked_last = False
        
        self.worked_label = QLabel()
        self.working_label = QLabel("0")

        self.numButton0 = QPushButton("0")
        self.numButton1 = QPushButton("1")
        self.numButton2 = QPushButton("2")
        self.numButton3 = QPushButton("3")
        self.numButton4 = QPushButton("4")
        self.numButton5 = QPushButton("5")
        self.numButton6 = QPushButton("6")
        self.numButton7 = QPushButton("7")
        self.numButton8 = QPushButton("8")
        self.numButton9 = QPushButton("9")

        self.opButton1 = QPushButton("+")
        self.opButton2 = QPushButton("-")
        self.opButton3 = QPushButton("x")
        self.opButton4 = QPushButton("/")
        self.opButton5 = QPushButton("=")
        self.opButton6 = QPushButton("C")
        self.opButton7 = QPushButton("CE")
        self.opButton8 = QPushButton("Del")
        self.opButton9 = QPushButton("+/-")

        self.decimalButton = QPushButton(".")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Standard Calculator")
        
        self.numButton0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.numButton9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.opButton9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.working_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.worked_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.decimalButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        vbox = QVBoxLayout()

        vbox.addWidget(self.worked_label)
        vbox.addWidget(self.working_label)

        grid = QGridLayout()

        grid.addWidget(self.opButton6, 0, 0)
        grid.addWidget(self.opButton7, 0, 1)
        grid.addWidget(self.opButton8, 0, 2)
        grid.addWidget(self.opButton4, 0, 3)
        grid.addWidget(self.opButton3, 1, 3)
        grid.addWidget(self.opButton2, 2, 3)
        grid.addWidget(self.opButton1, 3, 3)
        grid.addWidget(self.opButton5, 4, 3)
        grid.addWidget(self.numButton7, 1, 0)
        grid.addWidget(self.numButton8, 1, 1)
        grid.addWidget(self.numButton9, 1, 2)
        grid.addWidget(self.numButton4, 2, 0)
        grid.addWidget(self.numButton5, 2, 1)
        grid.addWidget(self.numButton6, 2, 2)
        grid.addWidget(self.numButton1, 3, 0)
        grid.addWidget(self.numButton2, 3, 1)
        grid.addWidget(self.numButton3, 3, 2)
        grid.addWidget(self.opButton9, 4, 0)
        grid.addWidget(self.numButton0, 4, 1)
        grid.addWidget(self.decimalButton, 4, 2)
       

        vbox.addLayout(grid)

        self.setLayout(vbox)

        self.worked_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.working_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.numButton0.clicked.connect(lambda: self.working_display("0"))
        self.numButton1.clicked.connect(lambda: self.working_display("1"))
        self.numButton2.clicked.connect(lambda: self.working_display("2"))
        self.numButton3.clicked.connect(lambda: self.working_display("3"))
        self.numButton4.clicked.connect(lambda: self.working_display("4"))
        self.numButton5.clicked.connect(lambda: self.working_display("5"))
        self.numButton6.clicked.connect(lambda: self.working_display("6"))
        self.numButton7.clicked.connect(lambda: self.working_display("7"))
        self.numButton8.clicked.connect(lambda: self.working_display("8"))
        self.numButton9.clicked.connect(lambda: self.working_display("9"))

        self.opButton1.clicked.connect(lambda: self.worked_display("+"))
        self.opButton2.clicked.connect(lambda: self.worked_display("-"))
        self.opButton3.clicked.connect(lambda: self.worked_display("x"))
        self.opButton4.clicked.connect(lambda: self.worked_display("/"))

        self.opButton5.clicked.connect(self.equals)
        self.opButton6.clicked.connect(self.clear)
        self.opButton7.clicked.connect(self.clear_entry)
        self.opButton8.clicked.connect(self.delete)
        self.opButton9.clicked.connect(self.negate)
        
        self.decimalButton.clicked.connect(self.add_decimal)

    def working_display(self, num):
        if self.op_clicked_last or self.op_clicked_last is None:
            self.nums_entered = ""
            self.op_clicked_last = False

        if self.equal_clicked_last:
            self.nums_entered = ""
            self.worked_label.clear()
            self.equal_clicked_last = False

        self.nums_entered += num

        if self.nums_entered == "0":
            self.nums_entered = ""

        self.working_label.setText(self.nums_entered if not self.nums_entered == "" else "0")
        
    def worked_display(self, op):
        if self.op_clicked_last is None:
            self.operand.append(self.is_integer(float(self.working_label.text())))
        elif not self.op_clicked_last:
            self.operand.append(self.is_integer(float(self.nums_entered) if not self.nums_entered == "" else 0))
            #self.operand[0] = self.is_integer(self.operand[0])

        self.op_clicked_last = True

        if len(self.operand) == 2 and not self.equal_clicked_last:
            self.calculate(op)
        else:
            self.working_label.setText(f"{self.is_integer(float(self.working_label.text()))}")
            self.worked_label.setText(f"{self.operand[0]}{op}")
            self.operator.append(op)
            self.operator = self.operator[-1::-1]
            self.operator = list(dict.fromkeys(self.operator))
            self.equal_clicked_last = False

    def add_decimal(self):
        if self.op_clicked_last or self.op_clicked_last is None:
            self.nums_entered = ""
            self.op_clicked_last = False

        if not "." in self.nums_entered:
            if self.nums_entered == "" and not self.op_clicked_last:
                self.nums_entered = "0."
            elif not self.nums_entered == "" and not self.op_clicked_last:
                self.nums_entered += "."
        
        self.working_label.setText(self.nums_entered)

    def calculate(self, op):
        match self.operator[0]:
            case "+":
                self.operand[0] += self.operand[1]
            case "-":
                self.operand[0] -= self.operand[1]
            case "x":
                self.operand[0] *= self.operand[1]
            case "/":
                self.operand[0] /= self.operand[1]

        self.operand = [round(self.is_integer(self.operand[0]), 10)]
        self.working_label.setText(f"{self.operand[0]}")
                
        if op == "=":
            self.operand.clear()
            self.operator.clear()
        else:
            self.nums_entered = ""
            self.operator = [op]
            self.worked_label.setText(f"{self.operand[0]}{op}")

    def clear(self):
        self.nums_entered = ""
        self.working_label.setText("0")
        self.worked_label.clear()
        self.operand.clear()
        self.operator.clear()
        self.op_clicked_last = False

    def clear_entry(self):
        self.nums_entered = ""
        self.working_label.setText("0")

    def delete(self):
        if self.op_clicked_last == False:
            self.nums_entered = (self.nums_entered[:-1] if not self.nums_entered[:-1] == "0" else "")
            self.working_label.setText(self.nums_entered if not self.nums_entered == "" else "0")

    def negate(self):
        text = self.working_label.text()
        if not text == "0":
            number = ("-" + text if "-" not in text else text.split("-")[1])

            if self.op_clicked_last == False:
                self.nums_entered = number
            else:
                self.op_clicked_last = None
            
            self.working_label.setText(number)

    def equals(self):
        if not self.op_clicked_last and not self.equal_clicked_last:

            self.equal_clicked_last = True

            if len(self.operand) == 0:
                self.worked_label.setText(f"{self.working_label.text()}=")
            elif len(self.operand) == 1:
                self.worked_label.setText(f"{self.worked_label.text()}{self.working_label.text()}=")
                self.operand.append(self.is_integer(float(self.nums_entered) if not self.nums_entered == "" else 0))
                self.calculate("=")
                # self.worked_label.setText(f"{self.worked_label.text()}{self.working_label.text()}=")
                # number = float(self.working_label.text())
                # match self.operator[0]:
                #     case "+":
                #         self.operand[0] += number
                #     case "-":
                #         self.operand[0] -= number
                #     case "x":
                #         self.operand[0] *= number
                #     case "/":
                #         self.operand[0] /= number

                # self.nums_entered = ""
                # self.operand = [round(self.is_integer(self.operand[0]), 10)]
                # self.operator.clear()
                # self.working_label.setText(f"{self.operand[0]}")
            elif len(self.operand) == 2:
                self.worked_label.setText(f"{self.worked_label.text()}{self.working_label.text()}=")
                self.calculate("=")

    def resizeEvent(self, event):
        super().resizeEvent(event)

        font_size_label = max(60, int(self.height() * 0.075))

        self.setStyleSheet(f"""
            QWidget{{
                background-color: hsl(235, 75%, 20%);
            }}
            QPushButton{{
                font-size: 50px;
                background-color: hsl(0, 3%, 15%);
                color: white;
                border: 2px solid;
                border-radius: 15px;
                border-color: white;
                padding: 10px;
            }}
            QPushButton:hover{{
                background-color: gray;
            }}
            QLabel{{
                color: white;
                font-size: {font_size_label}px;
                border: 2px solid;
                border-color: white;
            }}
        """)
    
    @staticmethod
    def is_integer(num):
        if num == int(num) or num == -0.0:
            return int(num)
        else:
            return num

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())