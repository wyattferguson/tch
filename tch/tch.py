import re

import click


@click.command()
@click.argument(
    "files",
    type=str,
    nargs=-1,
)
@click.option(
    "--verbose",
    "-v",
    default=False,
    is_flag=True,
    help="Show notice as files are created.",
)
def cli(files: tuple[str, ...] = (), verbose: bool = False) -> None:
    """Create an empty file(s) with the specified name(s)."""
    for filename in files:
        try:
            # check if filename is valid for Windows
            if not is_valid_windows_filename(filename):
                click.echo(f"Error: '{filename}' is not a valid Windows filename.")
                continue

            # create file
            with open(filename, "x") as fp:
                # verify file was created & write empty string
                fp.write("")
            if verbose:
                click.echo(f"Created file: {filename}")
        except FileExistsError:
            click.echo(f"Error: File '{filename}' already exists.")
        except Exception as e:
            click.echo(f"Error: {e}")


def is_valid_windows_filename(filename: str) -> bool:
    # invalid characters in Windows filenames
    invalid_chars_pattern = r'[<>:"/\\|?*]'
    # Check if the filename contains any invalid characters or is a reserved name
    if re.search(invalid_chars_pattern, filename) or filename in (
        "CON",
        "PRN",
        "AUX",
        "NUL",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM6",
        "COM7",
        "COM8",
        "COM9",
        "LPT1",
        "LPT2",
        "LPT3",
        "LPT4",
        "LPT5",
        "LPT6",
        "LPT7",
        "LPT8",
        "LPT9",
    ):
        return False
    return True


if __name__ == "__main__":
    cli()
