from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

WIDTH = 60
console = Console()

def divider():
    """Print a horizontal divider."""
    console.print("━" * WIDTH, style="dim yellow")

def blank():
    """Print a blank line."""
    console.print()

def center(text):
    """Center text on the terminal."""
    console.print(text.center(WIDTH), style="bold cyan")

def banner():
    """Display the CLIQuest banner."""
    divider()
    center("🧭 CLIQuest")
    center("Learn Linux One Quest at a Time")
    divider()

def page_header(name, campaign, quest, xp):
    """Display Explorer information."""
    blank()
    console.print(f"[bold white]🧑 Explorer :[/bold white] {name}")
    console.print(f"[bold white]🗺️ Campaign :[/bold white] {campaign}")
    console.print(f"[bold white]📜 Quest    :[/bold white] {quest}")
    console.print(f"[bold white]⭐ XP       :[/bold white] {xp}")
    divider()

def card(title, content):
    """Display a content card using Rich panels."""
    blank()
    formatted_content = Text(content, style="bright_white")
    panel = Panel(
        formatted_content,
        title=f"[bold yellow] {title} [/bold yellow]",
        title_align="left",
        border_style="yellow",
        padding=(1, 2)
    )
    console.print(panel)
    blank()

def success(message):
    """Display a success message."""
    blank()
    formatted_message = Text(message, style="bold bright_green")
    panel = Panel(
        formatted_message,
        title="[bold green] 🎉 SUCCESS [/bold green]",
        title_align="left",
        border_style="green",
        padding=(1, 2)
    )
    console.print(panel)

def error(message):
    """Display an error message."""
    blank()
    formatted_message = Text(message, style="bright_red")
    panel = Panel(
        formatted_message,
        title="[bold red] 💡 Gentle Guidance [/bold red]",
        title_align="left",
        border_style="red",
        padding=(1, 2)
    )
    console.print(panel)

def prompt(message):
    """Display a styled input prompt."""
    console.print()
    ans = Prompt.ask(f"[bold magenta]👉 {message}[/bold magenta]")
    return ans

def pause():
    """Pauses the game flow until the user presses Enter."""
    console.print("\n[dim]Press Enter to continue...[/dim]")
    input()
    console.clear()
