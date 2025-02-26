# :robot: tch - Quick Command-line File Creation

A universal version of `touch` that runs on windows, linux, and mac. Quickly create a file or files with the `tch` command.

## Usage + Examples

```
# create a single file
tch example.txt

# pass a full path
tch c:\example.txt

# create multiple files at once
tch test.py config.yml readme.txt
```

## Development Setup

Installation is pretty straight forward, Im using [UV](https://docs.astral.sh/uv/) to manage everything.

To get it all running from scratch:

```
# spin up a virtual enviroment
uv venv

# activate virtual enviroment
.venv\Scripts\activate

# install all the cool dependancies
uv sync

# run tch
task run

# run pytests
task tests

```

## References

- [Click](https://click.palletsprojects.com/en/stable/): Python library for building CLI's

## Contact + Support

Created by [Wyatt Ferguson](https://wyattf.bsky.social)

For any questions or comments heres how you can reach me:

### :mailbox_with_mail: Email me at [wyattxdev@duck.com](wyattxdev@duck.com)

### :tropical_drink: Follow on [BlueSky @wyattf](https://wyattf.bsky.social)

If you find this useful and want to tip me a little coffee money:

### :coffee: [Buy Me A Coffee](https://www.buymeacoffee.com/wyattferguson)
