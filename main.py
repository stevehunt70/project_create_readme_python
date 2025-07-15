from InquirerPy import prompt
from rich.console import Console

console = Console()

#The function asks various questions in order to build a readme.md file automatically using the programming language of Python.
#The user's input of questions answered will populate the readme.md file in the appropriate positions, which in turn will format the actual file.


# get user input using Inquirer
questions = [
    {"type": "input","name": "projName", "message": "What is the name of your project?"},
    {"type": "input","name": "projDesc", "message": "Give a description of your project"},
    {"type": "input","name": "listImports", "message": "Please list the imports for Python that you need in order to be able to format this readme.md file separated by a comma"},
    #{"type": "input","name": "mainDesc", "message": "Give a description of how the project works and what will be the end result?"},
    {
        "type": "list",
        "name": "licence",
        "message": "Choose a licence type:",
        "choices": [
            "MIT",
            "GILv3",
            "Apache 2.0",
            "BSD 3-Clause",
            "Unlicensed",
            "Proprietary"
        ]
    },
    #{"type": "input","name": "projLinks", "message": "Please copy in any links that are necessary. e.g. GitHub links?"},
    {
        "type": "list",
        "name": "projStatus",
        "message": "What is the status of your project?",
        "choices": [
            "Active / In development",
            "Completed",
            "On hold",
            "Abandoned"
        ]
    }
]

answers = prompt(questions)

# Split the input list of Imports from comma to seprate lists in the Installation section
imports = [lib.strip() for lib in answers["listImports"].split(",") if lib.strip()]
formatted_imports = "\n".join(f"pip install {lib}" for lib in imports)

readme_content = f"""
# {answers['projName']}\n\n
### Project Description\n
{answers['projDesc']}\n\n
### Installation\n
Use the package manager pip to install the following imports:
\n{formatted_imports}\n
### Questions:\n
These are the questions that the user will need to answer in order to fill in the readme.md file.\n
    * What is the name of your project?\n
    * Please list the library imports for Python that you need in order to be able to format this readme.md file separated by a comma.\n
    * Give a description of how the project works and what will be the end result.\n
    * What type of licence is needed?\n
    * Please copy in any links that are necessary. e.g. GitHub links.\n
    * What is the project status?\n\n
### Description\n
{'projDesc'}\n\n
### Licence\n
This project is licensed under the {answers['licence']} format.\n
You are free to use, modify and distribute this code with proper attribution.\n\n
### Links\n
{'projLinks'}\n\n
### Project Status\n
The status of this project is {answers['projStatus']}\n
"""

with open("readme2.md", "w") as file:
    file.write(readme_content)

console.print("[bold green]readme2.md successfully generated![/bold green]")