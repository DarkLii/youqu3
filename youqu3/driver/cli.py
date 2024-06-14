import click
from rich.console import Console

console = Console()


@click.group()
@click.option("-v", "--version")
def cli():
    console.print(
        "YouQu3 :dragon:",
        style="blue",
    )


@cli.command()
@click.option("-k", "--keywords", default=None, type=click.STRING, help="keywords driver")
@click.option("-t", "--tags", default=None, type=click.STRING, help="tags driver")
def run(
        keywords,
        tags,
):
    """RUN模式"""
    args = {
        "keywords": keywords,
        "tags": tags,
    }
    from youqu3.driver.run import Run
    Run(**args).run()


@cli.command()
def remote():
    """REMOTE模式"""
    console.print("Remote Running YouQu3")

@cli.command()
def init():
    """创建用例工程"""
    from youqu3.driver.init import Init
    Init().init()


if __name__ == '__main__':
    cli()
