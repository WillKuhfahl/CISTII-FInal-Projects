from PyQt5.QtWidgets import *
from GPA_calculator import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

def letter_grade(grade: float):
    """
    Converts raw number grades to letter grades.
    :param grade: number grade input
    :return: outputs the converted letter grade based on the number input
    """
    float(grade)
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def grade_to_gpa(grade: float):
    """
    Converts raw number grades to their gpa equivalents.
    :param grade: number grade input
    :return: outputs the converted gpa score based on the number input
    """
    float(grade)
    if grade >= 90:
        return 4.0
    elif grade >= 80:
        return 3.0
    elif grade >= 70:
        return 2.0
    elif grade >= 60:
        return 1.0
    else:
        return 0.0


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.enterButton.clicked.connect(lambda: self.submit())
        self.clearButton.clicked.connect(lambda: self.clear())
        self.calculateButton.clicked.connect(lambda: self.calculate())

    def submit(self):
        """
        Deals with all the code that is run when the submit button is clicked. Reads the dropdown selection from
        the user and changes the appropriate labels accordingly.
        :return: returns nothing
        """
        print("The submit button was clicked!")
        menu_selection = (self.comboBox.currentText())
        if menu_selection == "1":
            self.infoLabel.setText("Please input 1 grade to be calculated and press the calculate button.")
            self.classLabel1.setText("Class 1:")
        elif menu_selection == "2":
            self.infoLabel.setText("Please input 2 grades to be calculated and press the calculate button.")
            self.classLabel1.setText("Class 1:")
            self.classLabel2.setText("Class 2:")
        elif menu_selection == "3":
            self.infoLabel.setText("Please input 3 grades to be calculated and press the calculate button.")
            self.classLabel1.setText("Class 1:")
            self.classLabel2.setText("Class 2:")
            self.classLabel3.setText("Class 3:")
        elif menu_selection == "4":
            self.infoLabel.setText("Please input 4 grades to be calculated and press the calculate button.")
            self.classLabel1.setText("Class 1:")
            self.classLabel2.setText("Class 2:")
            self.classLabel3.setText("Class 3:")
            self.classLabel4.setText("Class 4:")
        elif menu_selection == "5":
            self.infoLabel.setText("Please input 5 grades to be calculated and press the calculate button.")
            self.classLabel1.setText("Class 1:")
            self.classLabel2.setText("Class 2:")
            self.classLabel3.setText("Class 3:")
            self.classLabel4.setText("Class 4:")
            self.classLabel5.setText("Class 5:")
        elif menu_selection == "6":
            self.infoLabel.setText("Please input 6 grades to be calculated and press the calculate button.")
            self.classLabel1.setText("Class 1:")
            self.classLabel2.setText("Class 2:")
            self.classLabel3.setText("Class 3:")
            self.classLabel4.setText("Class 4:")
            self.classLabel5.setText("Class 5:")
            self.classLabel6.setText("Class 6:")
        elif menu_selection == "7":
            self.infoLabel.setText("Please input 7 grades to be calculated and press the calculate button.")
            self.classLabel1.setText("Class 1:")
            self.classLabel2.setText("Class 2:")
            self.classLabel3.setText("Class 3:")
            self.classLabel4.setText("Class 4:")
            self.classLabel5.setText("Class 5:")
            self.classLabel6.setText("Class 6:")
            self.classLabel7.setText("Class 7:")

    def calculate(self):
        """
        Calculates and outputs the gpa of the user depending on their menu selection choice.
        :return: returns nothing
        """
        menu_selection = (self.comboBox.currentText())
        print(menu_selection)
        if menu_selection == "1":
            grade1 = int(self.grade.text())
            self.letterGrade.setText(letter_grade(grade1))
            gpa = grade_to_gpa(grade1)
            self.infoLabel.setText(f'Your GPA is {gpa}. Press the clear button to use the calculator again.')
        elif menu_selection == "2":
            grade1 = int(self.grade.text())
            self.letterGrade.setText(letter_grade(grade1))
            grade2 = int(self.grade_2.text())
            self.letterGrade_2.setText(letter_grade(grade2))
            gpa = (grade_to_gpa(grade1) + grade_to_gpa(grade2))/2
            self.infoLabel.setText(f'Your GPA is {gpa:.2f}. Press the clear button to use the calculator again.')
        elif menu_selection == "3":
            grade1 = int(self.grade.text())
            self.letterGrade.setText(letter_grade(grade1))
            grade2 = int(self.grade_2.text())
            self.letterGrade_2.setText(letter_grade(grade2))
            grade3 = int(self.grade_3.text())
            self.letterGrade_3.setText(letter_grade(grade3))
            gpa = (grade_to_gpa(grade1) + grade_to_gpa(grade2) + grade_to_gpa(grade3))/3
            self.infoLabel.setText(f'Your GPA is {gpa:.2f}. Press the clear button to use the calculator again.')
        elif menu_selection == "4":
            grade1 = int(self.grade.text())
            self.letterGrade.setText(letter_grade(grade1))
            grade2 = int(self.grade_2.text())
            self.letterGrade_2.setText(letter_grade(grade2))
            grade3 = int(self.grade_3.text())
            self.letterGrade_3.setText(letter_grade(grade3))
            grade4 = int(self.grade_4.text())
            self.letterGrade_4.setText(letter_grade(grade4))
            gpa = (grade_to_gpa(grade1) + grade_to_gpa(grade2) + grade_to_gpa(grade3) + grade_to_gpa(grade4))/4
            self.infoLabel.setText(f'Your GPA is {gpa:.2f}. Press the clear button to use the calculator again.')
        elif menu_selection == "5":
            grade1 = int(self.grade.text())
            self.letterGrade.setText(letter_grade(grade1))
            grade2 = int(self.grade_2.text())
            self.letterGrade_2.setText(letter_grade(grade2))
            grade3 = int(self.grade_3.text())
            self.letterGrade_3.setText(letter_grade(grade3))
            grade4 = int(self.grade_4.text())
            self.letterGrade_4.setText(letter_grade(grade4))
            grade5 = int(self.grade_5.text())
            self.letterGrade_5.setText(letter_grade(grade5))
            gpa = (grade_to_gpa(grade1) + grade_to_gpa(grade2) + grade_to_gpa(grade3) + grade_to_gpa(grade4) + grade_to_gpa(grade5))/5
            self.infoLabel.setText(f'Your GPA is {gpa:.2f}. Press the clear button to use the calculator again.')
        elif menu_selection == "6":
            grade1 = int(self.grade.text())
            self.letterGrade.setText(letter_grade(grade1))
            grade2 = int(self.grade_2.text())
            self.letterGrade_2.setText(letter_grade(grade2))
            grade3 = int(self.grade_3.text())
            self.letterGrade_3.setText(letter_grade(grade3))
            grade4 = int(self.grade_4.text())
            self.letterGrade_4.setText(letter_grade(grade4))
            grade5 = int(self.grade_5.text())
            self.letterGrade_5.setText(letter_grade(grade5))
            grade6 = int(self.grade_6.text())
            self.letterGrade_6.setText(letter_grade(grade6))
            gpa = (grade_to_gpa(grade1) + grade_to_gpa(grade2) + grade_to_gpa(grade3) + grade_to_gpa(grade4) + grade_to_gpa(grade5) + grade_to_gpa(grade6))/6
            self.infoLabel.setText(f'Your GPA is {gpa:.2f}. Press the clear button to use the calculator again.')
        elif menu_selection == "7":
            grade1 = int(self.grade.text())
            self.letterGrade.setText(letter_grade(grade1))
            grade2 = int(self.grade_2.text())
            self.letterGrade_2.setText(letter_grade(grade2))
            grade3 = int(self.grade_3.text())
            self.letterGrade_3.setText(letter_grade(grade3))
            grade4 = int(self.grade_4.text())
            self.letterGrade_4.setText(letter_grade(grade4))
            grade5 = int(self.grade_5.text())
            self.letterGrade_5.setText(letter_grade(grade5))
            grade6 = int(self.grade_6.text())
            self.letterGrade_6.setText(letter_grade(grade6))
            grade7 = int(self.grade_7.text())
            self.letterGrade_7.setText(letter_grade(grade7))
            gpa = (grade_to_gpa(grade1) + grade_to_gpa(grade2) + grade_to_gpa(grade3) + grade_to_gpa(grade4) + grade_to_gpa(grade5) + grade_to_gpa(grade6) + grade_to_gpa(grade7))/7
            self.infoLabel.setText(f'Your GPA is {gpa:.2f}. Press the clear button to use the calculator again.')


    def clear(self):
        """
        Clears all text boxes and resets the dropdown menu.
        :return:
        """
        self.infoLabel.setText("Please choose the number of grades you would like to calculate using the drop-down"
                               " menu above and hit submit.")
        self.classLabel1.setText("")
        self.classLabel2.setText("")
        self.classLabel3.setText("")
        self.classLabel4.setText("")
        self.classLabel5.setText("")
        self.classLabel6.setText("")
        self.classLabel7.setText("")
        self.grade.setText("")
        self.grade_2.setText("")
        self.grade_3.setText("")
        self.grade_4.setText("")
        self.grade_5.setText("")
        self.grade_6.setText("")
        self.grade_7.setText("")
        self.letterGrade.setText("")
        self.letterGrade_2.setText("")
        self.letterGrade_3.setText("")
        self.letterGrade_4.setText("")
        self.letterGrade_5.setText("")
        self.letterGrade_6.setText("")
        self.letterGrade_7.setText("")
        self.comboBox.setCurrentText(" ")

