def convert_code_blocks(content):
    content = content.replace("{{{", "```")
    content = content.replace("}}}", "```")

    return content

