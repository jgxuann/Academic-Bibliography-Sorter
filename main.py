import re

def extract_sort_key(bibitem_block):
    """
    Extracts the surname of the first author for sorting from the bibitem block.
    It looks for the author list immediately following the \bibitem[Author(Year)]{Key} tag.
    """
    # 1. Try to extract the author surname from the square brackets in \bibitem[...] (e.g., Song, Rizvi)
    match_tag = re.search(r'\\bibitem\[([^)]+)\)\{', bibitem_block)
    if match_tag:
        # Extract content inside the square brackets, e.g., "Song et al.(2024"
        tag_content = match_tag.group(1)
        # Try to extract the first word in the tag content as the surname
        first_author = tag_content.split()[0].strip()
        # Remove commas or periods, and return the surname for sorting (e.g., Song, Rizvi)
        return first_author.replace(',', '').replace('.', '')

    # 2. If Method 1 fails (e.g., for Russell(2019) which only has a surname), look for the next author line
    # Find the author line (usually the first line after the \bibitem tag)
    match_author = re.search(r'\}\n\s*([^,]+),', bibitem_block)
    if match_author:
        # Extract the surname of the first author (e.g., Song, T. -> Song)
        # Look up to the first comma (if the author is in the format LastName, FirstName)
        author_line = match_author.group(1).strip()
        
        # Try again to extract the surname from the author line (e.g., Rizvi, M. -> Rizvi)
        if ',' in author_line:
            surname = author_line.split(',')[0].strip()
            return surname
        else:
            # If the format is only surname (e.g., Hamdi, M.)
            surname = author_line.split()[0].strip()
            return surname

    # If extraction fails, use the entire block as a fallback sort key
    return bibitem_block

def sort_bibliography(input_filename="bib.txt", output_filename="sorted_bib.txt"):
    """
    Reads the bibliography file, sorts the references by author surname, and writes to a new file.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found. Please ensure the file exists.")
        return

    # 1. Split the file content: Extract \begin{thebibliography} and \end{thebibliography}
    header_match = re.match(r'\\begin\{thebibliography\}\{00\}\s*\n', content)
    footer_match = re.search(r'\\end\{thebibliography\}', content)

    if not header_match or not footer_match:
        print("Error: Non-standard file structure. Please ensure the file contains \\begin{thebibliography}{00} and \\end{thebibliography}.")
        return

    # Extract header and footer
    header = header_match.group(0)
    footer = content[footer_match.start():]
    
    # Extract content between \begin{thebibliography} and \end{thebibliography}
    bib_content = content[header_match.end():footer_match.start()]

    # 2. Split the content into individual \bibitem blocks
    # Use regex to split while keeping the delimiter \bibitem
    bibitem_blocks = re.split(r'(\n\\bibitem\[)', bib_content)
    
    # Recombine blocks, ensuring each block starts with \bibitem[
    items = []
    if bibitem_blocks:
        # The first element is usually an empty string or newline, skip it
        for i in range(1, len(bibitem_blocks), 2):
            # Concatenate \bibitem[ and the following content
            full_block = bibitem_blocks[i].strip() + bibitem_blocks[i+1]
            items.append(full_block)
    
    # ********* Added Reference Count Line *********
    num_references = len(items)
    print(f"Detected {num_references} reference entries.")
    # ***********************************

    if num_references == 0:
        print("Warning: No reference entries detected. The output file will be empty.")
        # Still output an empty file with header and footer
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(header + '\n' + footer)
        return

    # 3. Sorting: Use the extracted surname as the key
    try:
        # lambda x: extract_sort_key(x).lower() ensures case-insensitive alphabetical sorting by surname
        sorted_items = sorted(items, key=lambda x: extract_sort_key(x).lower())
    except Exception as e:
        print(f"Error during sorting: {e}")
        return


    # 4. Rebuild and output the file
    sorted_bib_content = '\n\n'.join(sorted_items)
    final_output = header + sorted_bib_content + '\n' + footer

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(final_output)

    print(f"Successfully sorted {len(sorted_items)} references.")
    print(f"Results saved to file: '{output_filename}'")


if __name__ == "__main__":
    sort_bibliography()