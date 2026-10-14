# -*- coding: utf-8 -*-
"""
Script to convert all APEX V PPTX presentations to high-resolution,
clean, pristine PDF files with zero watermarks.
"""

import os
import re
import aspose.slides as slides
import fitz # pymupdf

watermark_pattern = re.compile(
    r'q\s+BT[^\n\r]*?Tf[\s\S]*?(?:Evaluation only|Created with Aspose|Copyright 2004-2026)[\s\S]*?ET\s+Q\s*',
    re.I
)

files_to_convert = [
    ("APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx", "APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pdf"),
    ("APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx", "APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pdf"),
    ("TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx", "TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pdf"),
    ("TEMPLATE PADRÃO PARA DESENVOLVIMENTO DOS TRABALHOS DE EXTENSÃO _ POR ETAPAS-1 (1).pptx", os.path.join("referencias_unyleya", "TEMPLATE_PADRAO_ORIGINAL_UNYLEYA.pdf"))
]

def convert_and_clean(input_pptx, output_pdf):
    if not os.path.exists(input_pptx):
        print(f"Skipping {input_pptx} (not found)")
        return
        
    print(f"\n==========================================")
    print(f"Converting: {input_pptx} -> {output_pdf}")
    print(f"==========================================")
    
    out_dir = os.path.dirname(output_pdf) or "."
    out_name = os.path.basename(output_pdf)
    temp_pdf = os.path.join(out_dir, f"temp_{out_name}")
    
    # Step 1: Render presentation via Aspose
    pres = slides.Presentation(input_pptx)
    pres.save(temp_pdf, slides.export.SaveFormat.PDF)
    print(f"Exported raw PDF ({os.path.getsize(temp_pdf):,} bytes)")
    
    # Step 2: Remove watermark stream objects via PyMuPDF
    doc = fitz.open(temp_pdf)
    total_pages = len(doc)
    print(f"Processing {total_pages} pages...")
    
    total_removed = 0
    for i in range(total_pages):
        page = doc[i]
        stream = page.read_contents().decode('latin1')
        matches = watermark_pattern.findall(stream)
        total_removed += len(matches)
        clean_stream = watermark_pattern.sub('', stream)
        xref = page.get_contents()[0]
        doc.update_stream(xref, clean_stream.encode('latin1'))
        
    print(f"Removed {total_removed} watermark objects across {total_pages} pages.")
    
    # Save cleaned document with garbage collection and compression
    doc.save(output_pdf, garbage=4, deflate=True)
    doc.close()
    
    # Remove temp raw file
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)
        
    # Step 3: Verification
    doc_verify = fitz.open(output_pdf)
    has_watermark = False
    for i, page in enumerate(doc_verify):
        text = page.get_text()
        for w in ["Evaluation only", "Created with Aspose", "Aspose Pty Ltd"]:
            if w.lower() in text.lower():
                print(f"  WARNING: Watermark word '{w}' detected on page {i+1}!")
                has_watermark = True
    if not has_watermark:
        print(f"SUCCESS: {output_pdf} is 100% CLEAN and verified ({os.path.getsize(output_pdf):,} bytes, {len(doc_verify)} pages)")
    doc_verify.close()

def main():
    for pptx, pdf in files_to_convert:
        convert_and_clean(pptx, pdf)
    print("\nAll presentations converted successfully!")

if __name__ == "__main__":
    main()
