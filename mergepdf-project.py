import PyPDF2

# List of PDF files to merge
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

# Create a PDF merger object
merger = PyPDF2.PdfMerger()

# Append each PDF to the merger
for pdf in pdf_files:
    merger.append(pdf)

# Write out the merged PDF
merger.write('merged_output.pdf')
merger.close()

print("PDFs merged successfully!")
