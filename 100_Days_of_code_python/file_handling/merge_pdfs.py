
def merge_pdfs(input_paths, output_path):
    with open(output_path, 'wb') as output_file:
        for input_path in input_paths:
            with open(input_path, 'rb') as input_file:
                output_file.write(input_file.read())

# Example usage:
# pdf_files_to_merge = ['file1.pdf', 'file2.pdf', 'file3.pdf']
pdf_files_to_merge = ['7.pdf','8.pdf','9.pdf','10.pdf']
output_pdf = 'merged_output2.pdf'

merge_pdfs(pdf_files_to_merge, output_pdf)
