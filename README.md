# pdfMerge

A simple script in Python with a GUI to merge together PDFs in a specific order for the Physics Business Office

mergePDFs takes in the folder path and merges all PDFs in a specific priority for End of Fiscal Year Reports.

Using PyPDF2 we merge pdfs.
Using PySimpleGUI we can launch a simple gui to paste in the folder location or manually search and select the folder path to unmerged pdfs.

# Requirements

- Python
- PyPDF2
- PySimpleGUI

# Installation

Make sure you have the latest version of pip and at least Python 3.0
In your command prompt, type in the following.

`python -m pip install --upgrade pip`

`pip install PyPDF2`

`pip install PySimpleGUI`

# Run pdfMerge

To run pdfMerge, run pdfMerge.py in command prompt.

`python mergeAll.py`

then a dialogue box will pop up 

# Bugs

After the dialogue box opens, pressing on any key on your keyboard will close the dialogue window and you will have to restart the program
