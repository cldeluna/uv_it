# UV Installation and Testing

## What is UV?

Astral's uv is a fast, all-in-one Python package and project manager written in Rust that unifies and accelerates Python development workflows by replacing multiple tools—including pip, pip-tools, poetry, pipx, pyenv, virtualenv, and twine—with a single, high-performance utility. It handles package installation, dependency resolution, virtual environments, project and Python version management, script execution, and package publishing, all with a familiar CLI and dramatic speed improvements. By consolidating these capabilities, uv simplifies and streamlines Python development for everything from individual scripts to complex multi-workspace projects.

## Why are we using it?

Because UV is a comprehensive package manager it shoudl be easier to create the necessary Python virtual environments for the scripts we will be executing in our Jinja2 workshop.

## Installation

### Mac and Linux

```
curl -LsSf https://astral.sh/uv/install.sh | sh

source $HOME/.local/bin/env
```



### Windows (Powershell)

``` 
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
#### Official UV Installation Guide
https://docs.astral.sh/uv/getting-started/installation/

## Execute Test Script

```

```


#### Inline Script Metadata
https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies


### Handy Commands

uv --version
uv python list
uv python install 3.10
uv run myscript.py
uv init --script example.py --python 3.12