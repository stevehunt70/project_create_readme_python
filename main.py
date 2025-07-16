from InquirerPy import prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Welcome panel
console.print(
    Panel.fit(
        "[bold cyan]Automatic README Generator[/bold cyan]\n[green]Answer a few questions to generate a well-formatted README.md file[/green]",
        title="📘 README Builder",
        subtitle="by Python + rich"
    )
)

# Prompt user for input
questions = [
    {"type": "input", "name": "projName", "message": "📌 What is the name of your project?"},
    {"type": "input", "name": "projDesc", "message": "📝 Give a short description of your project."},
    {"type": "input", "name": "listImports", "message": "📦 List the required Python libraries (comma-separated):"},
    {"type": "input", "name": "mainDesc", "message": "🔧 Describe how the project works and the end result:"},
    {
        "type": "list",
        "name": "licence",
        "message": "🔐 Choose a licence type:",
        "choices": ["MIT", "GILv3", "Apache 2.0", "BSD 3-Clause", "Unlicensed", "Proprietary"]
    },
    {"type": "input", "name": "projLinks", "message": "🔗 Add any relevant links (e.g., GitHub):"},
    {
        "type": "list",
        "name": "projStatus",
        "message": "🚦 What is the status of your project?",
        "choices": ["Active / In development", "Completed", "On hold", "Abandoned"]
    }
]

answers = prompt(questions)

# Process library list
imports = [lib.strip() for lib in answers["listImports"].split(",") if lib.strip()]
formatted_imports = "\n".join(f"- `pip install {lib}`" for lib in imports)

# Markdown content
readme_content = f"""![Project Logo](./images/logo.png)

# {answers['projName']}

## 📝 Description
{answers['projDesc']}

## ⚙️ How It Works
{answers['mainDesc']}

## 📦 Installation
To install the required dependencies, run:
{formatted_imports}

## ❓ Project Setup Questions
These questions were used to build this README:

- What is the name of your project?
- Provide a description of your project.
- List the Python libraries required.
- How does the project work?
- Choose a license type.
- Add any project-related links.
- What is the current status of the project?

## 🔐 License
This project is licensed under the **{answers['licence']}** license.

## 🔗 Links
{answers['projLinks']}

## 🚦 Project Status
**{answers['projStatus']}**

---

_This README was automatically generated using a Python script powered by [rich](https://github.com/Textualize/rich) and [InquirerPy](https://github.com/kazhala/InquirerPy)._
"""

# Write to file
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

# Print success message
console.print("\n[bold green]✅ README.md successfully generated![/bold green]")
console.print("[cyan]Check your project directory for the file.[/cyan]\n")
