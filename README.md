# pysync

pysync is a simple backup/sync tool with rsync.

# Installation

```shell
$ pip install pysync
```

# Usage

Create `pysync.json` file in `~/.config/pysync.json` or `~/pysync.json`.

```json5
{

}
```

Run pysync.

```shell
$ pysync
```

## Command Line Options

|                   |                                                                 |
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
