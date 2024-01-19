from PyPDF2 import PdfMerger

def merge_pdfs(file_paths, output_path):
    merger = PdfMerger()
    for file_path in file_paths:
        merger.append(file_path)
    
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

merge_pdfs("Your Path File Here","Your Output Path Here")