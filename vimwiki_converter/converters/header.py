import re


def convert_headers(content):
    for i in range(5, 0, -1):
        vimwiki_header_pattern = r"^(=+)(.*?)(=+)$"
        def replace_with_markdown_header(match):
            level = len(match.group(1))  # Determine header level by length of "=" string
            header_text = match.group(2).strip()  # Trim any leading/trailing spaces
            return "#" * level + " " + header_text  # Add a space after "#" as per Markdown syntax
        content = re.sub(vimwiki_header_pattern, replace_with_markdown_header, content, flags=re.MULTILINE)

    return content

