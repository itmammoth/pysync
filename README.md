# pysync

pysync is a simple backup/sync tool with python & rsync.

[日本語版ドキュメント](https://www.ohmyenter.com/simple-backup-tool-pysync/)

# Installation

```shell
$ pip install itm.pysync
```

# Usage

Create `pysync.json` file in `~/.config/pysync.json` or `~/pysync.json`.

Here is an example of `pysync.json`.

```json5
{
    // Set rsync options (default: -a -v -h)
    "rsync_options": ["-a", "-v", "-h", "--delete", "--iconv=UTF-8-MAC,UTF-8"],

    // Define rsync filters
    "filters": {
        "git": ["-C", "--filter", ":- .gitignore"]
    },

    // Set global exclusions to exclude files and directories in all backup sources
    "global_exclusions": [".DS_Store"],

    // Set destination directory path
    "destination": "/Volumes/HDD/backup",

    // Set backup sources
    "sources": [
        {
            "path": "/Users/whoami/Documents"
        },
        {
            "path": "/Users/whoami/Pictures",
            "exclusions": ["*.photoslibrary", "secrets/"]    // Specify exclusion patterns to exclude in the source
        },
        {
            "path": "/Users/whoami/Programs",
            "filter": "git"     // Use filter in the source
        }
    ]
}
```

Run pysync.

```shell
$ pysync
```

## Command Line Options

| Option            | Feature                                                         |
| ----------------- | --------------------------------------------------------------- |
| -c, --config-file | Indicate config file path (e.x. `pysync -c ~/hoge/pysync.json`) |
| -h, --help        | Show help                                                       |
| --version         | Show version                                                    |

# License

MIT License

# Testing

Test with `pytest`.

```shell
$ pytest
```
