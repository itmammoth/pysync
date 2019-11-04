# pysync
pysync is a simple rsync wrapper with python.

# Usage

Create `settings.json` file anywhere you like.

```json
{
    //
    // pysync - settings.json
    //
    // Set destination path
    "destination": "/Volumes/HDD/backup",
    //
    // Set source paths to backup
    "sources": [
        {
            "path": "/Users/whoami/Documents",
            "exclusions": [".DS_Store"]
        },
        // ... expected command: rsync -avh --exclude=".DS_Store" /Users/whoami/Documents /Volumes/HDD/backup

        {
            "path": "/Users/whoami/code",
            "exclusions": ["*.log", "tmp/"]
        }
        // ... expected command: rsync -avh --exclude="*.log" --exclude="tmp/" /Users/whoami/code /Volumes/HDD/backup
    ]
}

```

Run pysync as a module.

```shell
$ python -m pysync -f "PATH_TO_YOUR_SETTINGS_JSON"
```

# License
MIT License

# Testing
Test with `pytest`.
```shell
$ pytest
```
