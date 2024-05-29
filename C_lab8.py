import sqlite3
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class EmployeePayrollInfo:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1530x800")
        self.window.title("Laboratory 8")
        self.window.configure(bg='#637A9F')
        self.frames()
        self.employee_picture()

    def frames(self):
        self.frame = Frame(width=0, height=0)
        self.frame.place(x=0, y=0)

    def labeldesign1(self, x, y, text_value):
        self.Label1 = Label(text=text_value, font=("", 13), bg='#637A9F')
        self.Label1.place(x=x, y=y)

    def employee_picture(self):
        Image1 = Image.open('Image1.jpg')
        EmployeeImage = ImageTk.PhotoImage(Image1.resize((160, 160)))
        BGLabel = Label(image=EmployeeImage)
        BGLabel.image = EmployeeImage  # Keep a reference to avoid garbage collection
        BGLabel.place(x=60, y=120)

con = sqlite3.connect("empinfos.db")
cursor = con.cursor()

# Create the main window
window = tk.Tk()
GUI = EmployeePayrollInfo(window)

# Define the search function
def search():
    Employee_Number = EmployeeNumberEntry.get()
    cursor.execute("SELECT * FROM employeeinfotbl WHERE EmployeeNumber=? ", (Employee_Number,))
    row1 = cursor.fetchone()
    if row1:

    # Clear existing entries
        FirstNameEntry.delete(0, 'end')
        MiddleNameEntry.delete(0, 'end')
        LastNameEntry.delete(0, 'end')
        CivilStatusEntry.delete(0, 'end')
        DepartmentEntry.delete(0, 'end')
        DesignationEntry.delete(0, 'end')
        QualifiedDeEntry.delete(0, 'end')
        PaydateEntry.delete(0, 'end')
        EmployeeStatusEntry.delete(0, 'end')

    # Insert new values

        FirstNameEntry.insert(0, row1[0])
        MiddleNameEntry.insert(0, row1[1])
        LastNameEntry.insert(0, row1[2])
        CivilStatusEntry.insert(0, row1[7])
        DepartmentEntry.insert(0, row1[8])
        DesignationEntry.insert(0, row1[9])
        QualifiedDeEntry.insert(0, row1[10])
        PaydateEntry.insert(0, row1[13])
        EmployeeStatusEntry.insert(0, row1[11])


# Define the save function
def save():
    query1 = """INSERT INTO payroll_info_tbl (EmployeeNumber, Department, FirstName, MiddleName, LastName,
                                                CivilStatus, QualifiedDepStatus, Paydate, EmployeeStatus, Designation)
                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    query2 = """INSERT INTO payroll_income_tbl (RateHour, NoOfHoursCutOff, IncomeCutOff, RateHour2, NoOfHoursCutOff2, IncomeCutOff2,
                                                   RateHour3, NoOfHoursCutOff3, IncomeCutOff3)
                                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    query3 = """INSERT INTO payroll_summary_income_tbl (GrossIncome, NetIncome)
                                                       VALUES (?, ?)"""
    query4 = """INSERT INTO payroll_deduction_tbl (SSSContribution, PHILHEALTHContribution, PAGIBIGContribution, INCOMETAXContribution,
                                                       SSSLOAN, PAGIBIGLOAN, FACULTYSAVINGDEPOSIT, FACULTYSAVINGLOAN,
                                                       SALARYLOAN, OTHERLOANS, TotalDeduction)
                                                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    query_tuple1 = (EmployeeNumberEntry.get(), DepartmentEntry.get(), FirstNameEntry.get(), MiddleNameEntry.get(),
                    LastNameEntry.get(),CivilStatusEntry.get(), QualifiedDeEntry.get(), PaydateEntry.get(),
                    EmployeeStatusEntry.get(),DesignationEntry.get())

    query_tuple2 = (RateHourEntry.get(), NoOfHoursCutOffEntry.get(), IncomeCutOffEntry.get(),
        RateHourEntry2.get(), NoOfHoursCutOffEntry2.get(), IncomeCutOffEntry2.get(),
        RateHourEntry3.get(), NoOfHoursCutOffEntry3.get(), IncomeCutOffEntry3.get())

    query_tuple3 = (GrossIncomeEntry.get(), NetIncomeEntry.get())

    query_tuple4 = (SSSContributionEntry.get(), PHILHEALTHContributionEntry.get(), PAGIBIGContributionEntry.get(),
        INCOMETAXContributionEntry.get(),
        SSSLOANEntry.get(), PAGIBIGLOANEntry.get(), FACULTYSAVINGDEPOSITEntry.get(), FACULTYSAVINGLOANEntry.get(),
        SALARYLOANEntry.get(), OTHERLOANSEntry.get(), TotalDeductionEntry.get())

    con.execute(query1, query_tuple1)
    con.execute(query2, query_tuple2)
    con.execute(query3, query_tuple3)
    con.execute(query4, query_tuple4)
    con.commit()
    con.close()

def update():
    Employee_Number = EmployeeNumberEntry.get()
    cursor.execute("SELECT * FROM employeeinfotbl WHERE EmployeeNumber=? ", (Employee_Number,))
    record = cursor.fetchone()
    if record:
        query = """ UPDATE employeeinfotbl SET Department=?, FirstName=?, MiddleName=?, LastName=?,
                                            CivilStatus=?, QualifiedDepStatus=?, Paydate=?, EmployeeStatus=?, Designation=? WHERE EmployeeNumber=?"""

        query_tuple = (DepartmentEntry.get(), FirstNameEntry.get(), MiddleNameEntry.get(),
                    LastNameEntry.get(),CivilStatusEntry.get(), QualifiedDeEntry.get(), PaydateEntry.get(),
                    EmployeeStatusEntry.get(),DesignationEntry.get(), Employee_Number)

        cursor.execute(query, query_tuple)
        con.commit()

# Add labels and entries
EmployeeBasicInfo = GUI.labeldesign1(60, 97, 'EMPLOYEE BASIC INFO:')
EmployeeNumber = GUI.labeldesign1(60, 300, 'Employee Number:')
SearchEmployee = GUI.labeldesign1(60, 340, 'Search Employee:')
Department = GUI.labeldesign1(60, 380, 'Department:')

FirstNameLabel = GUI.labeldesign1(350, 150, 'First Name:')
MiddleNameLabel = GUI.labeldesign1(350, 190, 'Middle Name:')
LastNameLabel = GUI.labeldesign1(350, 230, 'Last Name:')
CivilStatusLabel = GUI.labeldesign1(710, 150, 'Civil Status:')
QualifiedDeLabel = GUI.labeldesign1(710, 180, 'Qual Dep Status:')
StatusLabel = GUI.labeldesign1(710, 200, 'Status:')
PaydateLabel = GUI.labeldesign1(710, 230, 'Paydate:')
EmployeeStatusLabel = GUI.labeldesign1(1110, 150, 'Employee Status:')
DesignationLabel = GUI.labeldesign1(1110, 190, 'Designation:')

BasicIncome = GUI.labeldesign1(370, 300, 'BASIC INCOME:')
RateHour = GUI.labeldesign1(370, 340, 'Rate/Hour:')
NoOfHoursCutOff = GUI.labeldesign1(370, 380, 'No. of Hours/Cut Off:')
IncomeCutOff = GUI.labeldesign1(370, 420, 'Income/Cut Off:')

HonorariumIncome = GUI.labeldesign1(740, 300, 'HONORARIUM INCOME:')
RateHour2 = GUI.labeldesign1(740, 340, 'Rate/Hour:')
NoOfHoursCutOff2 = GUI.labeldesign1(740, 380, 'No. of Hours/Cut Off:')
IncomeCutOff2 = GUI.labeldesign1(740, 420, 'Income/Cut Off:')

OtherIncome = GUI.labeldesign1(1110, 300, 'OTHER INCOME:')
RateHour3 = GUI.labeldesign1(1110, 340, 'Rate/Hour:')
NoOfHoursCutOff3 = GUI.labeldesign1(1110, 380, 'No. of Hours/Cut Off:')
IncomeCutOff3 = GUI.labeldesign1(1110, 420, 'Income/Cut Off:')

SummaryIncome = GUI.labeldesign1(1110, 470, 'SUMMARY INCOME:')
GrossIncome = GUI.labeldesign1(1110, 505, 'GROSS INCOME:')
NetIncome = GUI.labeldesign1(1110, 540, 'NET INCOME:')

RegularDeduction = GUI.labeldesign1(60, 470, 'REGULAR DEDUCTION:')
SSSContribution = GUI.labeldesign1(60, 500, 'SSS CONTRIBUTION:')
PHILHEALTHContribution = GUI.labeldesign1(60, 540, 'PHIL-HEALTH CONTRIBUTION:')
PAGIBIGContribution = GUI.labeldesign1(60, 580, 'PAG-IBIG CONTRIBUTION:')
INCOMETAXContribution = GUI.labeldesign1(60, 620, 'INCOME TAX CONTRIBUTION:')

OtherDeduction = GUI.labeldesign1(580, 470, 'OTHER DEDUCTION:')
SSSLOAN = GUI.labeldesign1(580, 500, 'SSS LOAN:')
PAGIBIGLOAN = GUI.labeldesign1(580, 540, 'PAG-IBIG LOAN:')
FACULTYSAVINGDEPOSIT = GUI.labeldesign1(580, 580, 'FACULTY SAVING DEPOSIT:')
FACULTYSAVINGLOAN = GUI.labeldesign1(580, 620, 'FACULTY SAVING LOAN:')
SALARYLOAN = GUI.labeldesign1(580, 660, 'SALARY LOAN:')
OTHERLOANS = GUI.labeldesign1(580, 700, 'OTHER LOANS:')

DeductionSummary = GUI.labeldesign1(1060, 620, 'DEDUCTION SUMMARY:')
TotalDeduction = GUI.labeldesign1(1090, 650, 'TOTAL DEDUCTIONS:')

# Entries for search section
EmployeeNumberEntry = tk.Entry(window, font=("", 10), width=20)
EmployeeNumberEntry.place(x=210, y=300)
DepartmentEntry = tk.Entry(window, font=("", 10), width=20)
DepartmentEntry.place(x=210, y=380)

# Entries for info section
FirstNameEntry = tk.Entry(window, font=("", 13), width=20)
FirstNameEntry.place(x=470, y=150)
MiddleNameEntry = tk.Entry(window, font=("", 13), width=20)
MiddleNameEntry.place(x=470, y=190)
LastNameEntry = tk.Entry(window, font=("", 13), width=20)
LastNameEntry.place(x=470, y=230)
CivilStatusEntry = tk.Entry(window, font=("", 13), width=20)
CivilStatusEntry.place(x=870, y=150)
QualifiedDeEntry = tk.Entry(window, font=("", 17), width=14)
QualifiedDeEntry.place(x=870, y=187)
PaydateEntry = tk.Entry(window, font=("", 13), width=20)
PaydateEntry.place(x=870, y=230)
EmployeeStatusEntry = tk.Entry(window, font=("", 13), width=20)
EmployeeStatusEntry.place(x=1270, y=150)
DesignationEntry = tk.Entry(window, font=("", 13), width=20)
DesignationEntry.place(x=1270, y=190)

# Entries for basic income section
RateHourEntry = tk.Entry(window, font=("", 13), width=20)
RateHourEntry.place(x=540, y=340)
NoOfHoursCutOffEntry = tk.Entry(window, font=("", 13), width=20)
NoOfHoursCutOffEntry.place(x=540, y=380)
IncomeCutOffEntry = tk.Entry(window, font=("", 13), width=20)
IncomeCutOffEntry.place(x=540, y=420)

# Entries for honorarium section
RateHourEntry2 = tk.Entry(window, font=("", 13), width=20)
RateHourEntry2.place(x=910, y=340)
NoOfHoursCutOffEntry2 = tk.Entry(window, font=("", 13), width=20)
NoOfHoursCutOffEntry2.place(x=910, y=380)
IncomeCutOffEntry2 = tk.Entry(window, font=("", 13), width=20)
IncomeCutOffEntry2.place(x=910, y=420)

# Entries for other income section
RateHourEntry3 = tk.Entry(window, font=("", 13), width=20)
RateHourEntry3.place(x=1280, y=340)
NoOfHoursCutOffEntry3 = tk.Entry(window, font=("", 13), width=20)
NoOfHoursCutOffEntry3.place(x=1280, y=380)
IncomeCutOffEntry3 = tk.Entry(window, font=("", 13), width=20)
IncomeCutOffEntry3.place(x=1280, y=420)

# Entries for summary income section
GrossIncomeEntry = tk.Entry(window, font=("", 13), width=20)
GrossIncomeEntry.place(x=1260, y=500)
NetIncomeEntry = tk.Entry(window, font=("", 13), width=20)
NetIncomeEntry.place(x=1260, y=540)

# Entries for regular deduction section
SSSContributionEntry = tk.Entry(window, font=("", 13), width=20)
SSSContributionEntry.place(x=310, y=500)
PHILHEALTHContributionEntry = tk.Entry(window, font=("", 13), width=20)
PHILHEALTHContributionEntry.place(x=310, y=540)
PAGIBIGContributionEntry = tk.Entry(window, font=("", 13), width=20)
PAGIBIGContributionEntry.place(x=310, y=580)
INCOMETAXContributionEntry = tk.Entry(window, font=("", 13), width=20)
INCOMETAXContributionEntry.place(x=310, y=620)

# Entries for other deduction section
SSSLOANEntry = tk.Entry(window, font=("", 13), width=20)
SSSLOANEntry.place(x=820, y=500)
PAGIBIGLOANEntry = tk.Entry(window, font=("", 13), width=20)
PAGIBIGLOANEntry.place(x=820, y=540)
FACULTYSAVINGDEPOSITEntry = tk.Entry(window, font=("", 13), width=20)
FACULTYSAVINGDEPOSITEntry.place(x=820, y=580)
FACULTYSAVINGLOANEntry = tk.Entry(window, font=("", 13), width=20)
FACULTYSAVINGLOANEntry.place(x=820, y=620)
SALARYLOANEntry = tk.Entry(window, font=("", 13), width=20)
SALARYLOANEntry.place(x=820, y=660)
OTHERLOANSEntry = tk.Entry(window, font=("", 13), width=20)
OTHERLOANSEntry.place(x=820, y=700)

# Entries for deduction summary section
TotalDeductionEntry = tk.Entry(window, font=("", 13), width=20)
TotalDeductionEntry.place(x=1270, y=650)

# Buttons
Update = tk.Button(width=10, pady=1, text='SEARCH', bg='#8EACCD', border=1, font=('Arial', 10), command=search)
Update.place(x=210, y=340)
Save = tk.Button(width=7, height=1, text='SAVE', bg='#8EACCD', font=('Arial', 10), command=save)
Save.place(x=1285, y=690)
GrossIncomeButton = tk.Button(width=13, pady=1, text='GROSS INCOME',bg='#8EACCD', border=1, font=('Arial',10))
GrossIncomeButton.place(x=1060, y=690)
NetIncomeButton = tk.Button(width=11, pady=1, text='NET INCOME', bg='#8EACCD', border=1, font=('Arial', 10))
NetIncomeButton.place(x=1180, y=690)
UpdateButton = tk.Button(width=8, pady=1, text='UPDATE', bg='#8EACCD', border=1, font=('Arial', 10), command=update)
UpdateButton.place(x=1359, y=690)
New = tk.Button(width=7, pady=1, text='NEW', bg='#8EACCD', border=1, font=('Arial', 10))
New.place(x=1439, y=690)

window.mainloop()
