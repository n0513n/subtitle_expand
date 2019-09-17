subtitle_expand
---

Simple Python script to expand subtitle times in a file
in order to e.g. allow best syncing on/off commands.

Only tested with .SRT extension format and UTF-8 encoding.

### Requirements

* **Python 2.7+**/**3.4+**

### Usage

```
python subtitle_expand.py input_file.srt
```

### Notes

* In order to make sure your file encoding is right, ```file``` should return "UTF-8 Unicode text":

``` $ file input_file.srt ```
> input_file.srt:    UTF-8 Unicode text

* You may try ```dos2unix``` in order to fix line breaks and encoding issues that might appear:

``` $ dos2unix input_file.srt```
> dos2unix: converting file input_file.srt to Unix format...

