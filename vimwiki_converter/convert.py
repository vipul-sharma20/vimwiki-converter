import os
import re
import yaml
import importlib
import pkgutil


def run(config_path):

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    source_directory, target_directory = config["source_directory"], config["target_directory"]

    for filename in os.listdir(source_directory):
        if filename.endswith(".wiki"):
            source_file_path = os.path.join(source_directory, filename)

        with open(source_file_path, "r", encoding="utf-8") as file:
            content = file.read()

        for function_name in config["functions"]:
            func = find_function_in_package("vimwiki_converter.converters", function_name)

            if func:
                content = func(content)
            else:
                print(f"""Function {function_name} not found in any module within "functions" """)

        # Construct target file path
        target_file_path = os.path.join(target_directory, os.path.splitext(os.path.basename(source_file_path))[0] + ".md")
        with open(target_file_path, "w", encoding="utf-8") as file:
            file.write(content)


def find_function_in_package(package, function_name):
    package = importlib.import_module(package)
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
        if not ispkg:
            module = importlib.import_module(modname)
            if hasattr(module, function_name):
                return getattr(module, function_name)
    return None

