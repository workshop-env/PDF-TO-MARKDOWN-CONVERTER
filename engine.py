import pymupdf4llm
from pathlib import Path

def convert_pdf_to_md(pdf_path, output_folder):
    try:
        md_text = pymupdf4llm.to_markdown(pdf_path, ignore_images = True, page_chunks = True)
        
        file_name = Path(pdf_path).stem + ".md"
        output_path = Path(output_folder) / file_name
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_text)
            
        # The most "User-Friendly" message
        return f"Success! Your Markdown file is now in your Downloads folder."
        
    except Exception as e:
        return f"Error: {str(e)}"
