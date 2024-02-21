## vimwiki-converter

CLI tool to convert [VimWiki][vimwiki] files from VimWiki (default) syntax to Markdown syntax.

This is built to convert old vimwiki documents from default syntax to markdown
for anyone who decides to make a switch.

Currently, vimwiki provides a way to [switch to a syntax][switch] but not a way
to convert older docs automatically to the new syntax. This tool is an attempt
to solve that.

> [!NOTE]
> This was built specifically looking at my own vimwiki docs and it may
> not support a complete set of conversion features. Documentation on adding
> custom conversion feature is later in the doc

### Installation

```
pip install https://github.com/vipul-sharma20/vimwiki-converter/releases/download/v0.1.0/vimwiki_converter-0.1.0-py3-none-any.whl
```

### Usage

```
vimwiki-converter run --config-yml=config.yml
```

#### Sample Config

```yaml

source_directory: /path/to/vimwiki/docs/
target_directory: /path/to/target/directory/

functions:
  - convert_headers
  - convert_code_blocks
```

Here, these functions are the functions defined in python files in
[`vimwiki_converter/conveters/`][converters] directory.

#### Adding a custom function for conversion

Implement a function with any name taking the file content as the parameter and
put it in any code in [`vimwiki_converter/converters/`][converters] path.

To use the new custom function, add its name the yaml config as shown
previously.

For example: [`convert_headers`][convert_headers] is a function implemented in
[`vimwiki_conver/converters/header.py`][header]. You can use similar methodology to
implement any custom function.

### Licence

MIT


[vimwiki]: https://github.com/vimwiki/vimwiki
[switch]: https://github.com/vimwiki/vimwiki?tab=readme-ov-file#changing-wiki-syntax
[converters]: ./vimwiki_converter/converters/
[convert_headers]: https://github.com/vipul-sharma20/vimwiki-converter/blob/main/vimwiki_converter/converters/header.py#L4
[header]: ./vimwiki_converter/converters/header.py
