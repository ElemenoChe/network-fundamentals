import fitz  # pymupdf
import os
import re

# Path to your PDF folder
PDF_FOLDER = os.path.expanduser("~/OneDrive/Desktop/1749486944300_ReviewQA/Review Q&A")
OUTPUT_FOLDER = "questions"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_qa(text):
    """Parse numbered Q&A pairs from text."""
    # Split on numbered questions like "1.", "2.", etc.
    pattern = r'\n(\d+)\.\s+'
    parts = re.split(pattern, text)
    
    qa_pairs = []
    i = 1
    while i < len(parts) - 1:
        number = parts[i]
        content = parts[i + 1].strip()
        
        # Clean up the content
        content = content.replace('\n', ' ')
        content = re.sub(r'\s+', ' ', content).strip()
        
        if content:
            qa_pairs.append(content)
        i += 2
    
    return qa_pairs

def format_for_quizlet(qa_pairs):
    """Format Q&A pairs as Quizlet import text (tab-separated)."""
    lines = []
    for item in qa_pairs:
        # Try to split question from answer at common patterns
        # Answers often start with bullet points or after a colon
        if '\t' in item:
            lines.append(item)
        else:
            # Find where the answer starts (after the first sentence/question)
            split_match = re.search(r'([^\.\?]+[\.\?])\s+([A-Z•\-])', item)
            if split_match:
                question = split_match.group(1).strip()
                answer = item[split_match.start(2):].strip()
                lines.append(f"{question}\t{answer}")
            else:
                lines.append(item)
    return '\n'.join(lines)

# Process all PDFs
for i in range(1, 19):
    pdf_name = f"Chap {i}.pdf"
    pdf_path = os.path.join(PDF_FOLDER, pdf_name)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  Not found: {pdf_name}")
        continue

    print(f"Processing {pdf_name}...")
    text = extract_text_from_pdf(pdf_path)
    
    # Save raw extracted text as Quizlet txt
    output_file = os.path.join(OUTPUT_FOLDER, f"Chapter_{i:02d}_Quizlet.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"✅ Saved: {output_file}")

print("\nDone! All files saved to the 'questions' folder.")
