import socket
import requests
import webbrowser
from rich.console import Console
import rich.traceback
from pyfiglet import Figlet


"""
MADE originally by Verratti
Reworked by KuroN3ko
"""


rich.traceback.install()
fig = Figlet(font="doom")
con = Console()


def valid_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except Exception:
        return False


def app():
    action = con.input("[bold]>>[/bold] ")
    if action in "23456" and len(action) == 1:
        pages = {
            "2": "https://t.me/llllIllIIl",
            "3": "https://Instagram.com/0xi0m",
            "4": "https://t.me/Verratti3",
            "5": "https://t.me/desperado_pasta",
            "6": "https://t.me/doomed_being",
        }
        try:
            webbrowser.open(pages[action])
        except Exception as e:
            con.print(
                f"[red][reverse]Error:[/reverse]cannot open url[/red]\n[bold]Error info: [u orange]{e}[/u orange][/bold]"
            )
    elif action == "0":
        exit(0)
    else:
        get_ip_info(
            con.input(
                "[bold blue]Enter an IP address [bold white]>>[/bold white][/bold blue]"
            )
        )


def get_ip_info(ip_add: str) -> None:
    if not valid_ip(ip_add):
        con.print("[bold red]Error: invalid IP address[/bold red]")
        exit(1)

    req = requests.get(f"http://ip-api.com/json/{ip_add}")
    req_j = req.json()
    con.print_json(data=req_j)


if __name__ == "__main__":
    try:
        banner_top = fig.renderText("1P 1NF0")
        banner = """\
======================================================
[bold]Choose an option from below[/bold]
[bold]| [[red]1[/red]] Check an IP address[/bold]
[bold]| [[cyan]2[/cyan]] open Verratti's channel : @[blue]llllIllIIl[/blue][/bold]
[bold]| [[cyan]3[/cyan]] open Verratti's Instagram : @[blue]0xi0m[/blue][/bold]
[bold]| [[cyan]4[/cyan]] open Verratti's Telegram : @[blue]Verratti3[/blue][/bold]
[bold]| [[cyan]5[/cyan]] open Kuro's channel : @[blue]desperado_pasta[/blue][/bold]
[bold]| [[cyan]6[/cyan]] open Kuro's Telegram : @[blue]doomed_being[/blue][/bold]
[bold]| [[cyan]0[/cyan]] EXIT[/bold]
        """

        con.print(f"[bold red]{banner_top}[/bold red]")
        con.print(
            "[bold]BY: [cyan]Mr <> Verratti[/cyan] and [cyan]KuroN3ko[/cyan][/bold]"
        )
        con.print(banner)
        con.print(
            "[bold]Choose an action or type an [red]IP address[/red] below[/bold]"
        )
        app()
    except (KeyboardInterrupt, EOFError):
        con.print("\n[bold][red]Exitting[/red]...[/bold]")
        exit(0)
