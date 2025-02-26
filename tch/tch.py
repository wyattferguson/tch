import click


@click.command()
@click.argument(
    "files",
    type=str,
    nargs=-1,
)
def cli(files: tuple[str, ...] = ()) -> None:
    """Create an empty file(s) with the specified name(s). \n
    Example:\n
    tch file1.txt file2.txt
    """
    if not files or not all(isinstance(file, str) for file in files):
        return

    for filename in files:
        try:
            # create file
            with open(filename, "x") as fp:
                # verify file was created
                fp.write("")
            click.echo(f"Created file: {filename}")
        except FileExistsError:
            click.echo(f"Error: File '{filename}' already exists.")
        except Exception as e:
            click.echo(f"Error: {e}")


if __name__ == "__main__":
    cli()
