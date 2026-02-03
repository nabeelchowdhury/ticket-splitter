from pypdf import PdfReader, PdfWriter
import os

# Set the input file path
input_path = r"C:\Users\Downloads\PDF.pdf"

# Check if file exists
if not os.path.exists(input_path):
    print(f"ERROR: File not found at {input_path}")
else:
    print(f"File found! Reading PDF...")
    reader = PdfReader(input_path)
    print(f"Total pages: {len(reader.pages)}")
    
    # Set output directory to Downloads folder
    output_dir = r"C:\Users\Downloads"
    
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_file = os.path.join(output_dir, f"page_{i+1}.pdf")
        with open(output_file, "wb") as output:
            writer.write(output)
        print(f"Created: {output_file}")
    
    print("PDF split complete!")