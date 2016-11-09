from Tkinter import *
import tkFileDialog
import csv

# master = Tk()

# opens a file dialog for csv files
def openFileDialogCsv():
    # source: http://tkinter.unpythonic.net/wiki/tkFileDialog
    # define options for opening or saving a file
    file_opt = options = {}
    options['defaultextension'] = '.csv'
    options['filetypes'] = [('Comma-separated values', '.csv')]
    options['initialdir'] = 'C:\\Temp\\'
    options['initialfile'] = 'myFile.csv'
    options['title'] = 'Please choose a .csv file'
    fileName = tkFileDialog.askopenfilename(**file_opt)
    return fileName

# open a csv file and give back a list of the set column
# fileNameCsv: the filename of the csv file
# columnHeaderToShow: the string representing a cell in the first row
# isHeaderInList: shall the given column text be in the list as well
# return: a list with the values in the cells of the column
def getListFromCsvFile(fileNameCsv,columnHeaderToShow,isHeaderInList):
    with open(fileNameCsv, 'rb') as csvFile:
        table = csv.reader(csvFile)
        firstRow=True
        for row in table:
            if (firstRow == True):
                firstRow = False
                columnCount = 0
                for columnheader in row:
                    if(columnHeaderToShow == columnheader):
                        columnCountToShow = columnCount
                        lines = []
                        if(isHeaderInList):
                            lines.append(columnheader)
                    columnCount += 1
            else:
                columnCount = 0
                for column in row:
                    if (columnCountToShow < columnCount):
                        break
                    if (columnCountToShow == columnCount):
                        lines.append(column)
                    columnCount += 1
    return lines

# open a csv file and give back a list of the set column
# fileNameCsv: the filename of the csv file
# columnHeaderToShow: the number representing a cell in the first row
# isHeaderInList: shall the given column text be in the list as well
# return: a list with the values in the cells of the column
def getListFromCsvFile(fileNameCsv,columnHeaderNumberToShow,isHeaderInList):
    with open(fileNameCsv, 'rb') as csvFile:
        table = csv.reader(csvFile)
        firstRow=True
        for row in table:
            if (firstRow == True):
                firstRow = False
                columnCount = 0
                for columnheader in row:
                    if (columnHeaderNumberToShow < columnCount):
                        break
                    if(columnHeaderNumberToShow == columnCount):
                        columnCountToShow = columnHeaderNumberToShow
                        lines = []
                        if(isHeaderInList):
                            lines.append(columnheader)
                    columnCount += 1
            else:
                columnCount = 0
                for column in row:
                    if (columnCountToShow < columnCount):
                        break
                    if (columnCountToShow == columnCount):
                        lines.append(column)
                    columnCount += 1
    return lines


# print getListFromCsvFile(openFileDialogCsv(), "hallo", True)

# mainloop()