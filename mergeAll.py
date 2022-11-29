# pip install PyPDF2
# pip install PySimpleGUI
"""
mergePDFs takes in the folder path and merges all PDFs in a specific priority for End of Fiscal Year Reports

Using PyPDF2 we merge pdfs
Using PySimpleGUI we can launch a simple gui to paste in the folder location or manually search and select the folder path to unmerged pdfs.

"""

from PyPDF2 import PdfMerger
import PySimpleGUI as sg
import os
import sys

def mergePDFs(folderPath):
	if not os.path.isdir(folderPath):
		print("Invalid path")
		return False
	
	print(f"Path is valid: {folderPath}")

	file_list = os.listdir(folderPath)
	# print(file_list)

	# ----- file priority -----
	# MyNSMSummary
	# ppsoftVerification
	# MyNSMReport - (active only)
	# Payroll Report
	# 1074
	# Build Packets
	# ----- end file priority -----
	IDs = []
	for filename in file_list:
		if filename[0:5].isnumeric() and filename[0:5] not in IDs:
			IDs.append(filename[0:5])
	
	for ID in IDs:
		# for every ID in the IDs we will add files to priority and then merge them for every ID
		print("Checking for files with ID: ", ID)
		file_priority = ["","","","","",""] # create/clear file priority
	
		for file in file_list:
			#print(file)
			#continue
			# print(f"File we are checking is {file}")
			tempfile = file.upper()
			if ID + " COST CENTER SUMMARY" in tempfile: #nsm summary
				file_priority[0] = file
			elif ID + " VERIFICATION REPORT" in tempfile: # ppsoft verification
				file_priority[1] = file
			elif ID + " REPORT" in tempfile: # mynsm report (2 in priority)
				file_priority[2] = file 
			elif ID + " PAYROLL REPORT" in tempfile: # payroll report
				file_priority[3] = file
			elif ID + " 1074 REPORT" in tempfile: # 1074 report
				file_priority[4] = file
			elif ID + " Build Packets" in tempfile:
				file_priority[5] = file
		merger = PdfMerger()
		# print(file_priority)
		for file in file_priority:
			fileLoc = folderPath + '\\' + file
			if file == "":
				continue
			else:
				merger.append(fileLoc)
	
		mergedFilename = folderPath + "/" + ID + " ZZZ_RESULT.pdf"
		print(f"Writing to path: {mergedFilename}")
		merger.write(mergedFilename)
		merger.close()
	return True
	
def main():
	layout = [	[sg.Text('Folder: '), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-', right_click_menu=[[''], ['Paste']]), sg.FolderBrowse()],
				[sg.Button('Select'),
				sg.Button('Cancel')]	]
	window = sg.Window('Merge All PDFs', layout, resizable=True)
	
	while True:
		event, values = window.read()
		# print('event: ',event)
		# print('values: ',values)
		
		if event in (sg.WIN_CLOSED,'Exit') or event == 'Cancel':
			return 0
		if event == '-FOLDER-':
			path = values['-FOLDER-']
			# print(path)
			mergePDFs(path)
			return 0
		if event == 'Paste':
			path = sg.clipboard_get()
			# print(path)
			mergePDFs(path)
			return 0
	
	
	# path = input("Input folder path: ")
	# id = input("Input id number: ")
	
	# print(f"Path: {path} and ID: {id}")
	# return 0
	# path = "/home/runner/pdfMerge"
	# windows path will be something like "C:\\Users\foo.csv"
	# mergeName = id + " ZZZ_RESULT.pdf"
	
	# mergePDFs(path)
	return 0

if __name__ == "__main__":
	main()
