# jprinter - Your Ultimate Debugging Companion! 🔥

<div align="center">
    <br>
    <p>
        Wassup, fam! 👋 Meet <code>jprinter</code>, your new go-to tool for debugging! 💯
        This ain't just your regular <code>print()</code> function; we're talkin' next-level debugging that keeps it real and helps you crush those bugs! 💪
    </p>
</div>

<br>

<div align="center">
    <a href="https://github.com/OE-LUCIFER/JPRINT/issues">
        <img src="https://img.shields.io/github/issues/OE-LUCIFER/JPRINT" alt="GitHub Issues" />
    </a>
    <a href="https://github.com/OE-LUCIFER/JPRINT/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/OE-LUCIFER/JPRINT" alt="License" />
     </a>
    <a href="https://pypi.org/project/jprinter/">
      <img src="https://img.shields.io/pypi/v/jprinter" alt="PyPI version" />
    </a>
</div>

<br>

## Table of Contents

- [What's `jprinter` All About?](#whats-jprinter-all-about)
- [Key Features That Keep It 💯](#key-features-that-keep-it-💯)
- [How to Use `jprinter` Like a Pro](#how-to-use-jprinter-like-a-pro)
    - [Basic Usage with `jp` and `jprint`](#basic-usage-with-jp-and-jprint)
    - [Logging with Different Levels](#logging-with-different-levels)
    - [Global Enable/Disable](#global-enabledisable)
    - [Custom Prefixes](#custom-prefixes)
    - [Pretty Printing Complex Data Structures](#pretty-printing-complex-data-structures)
    - [Custom Separators](#custom-separators)
    - [File Logging](#file-logging)
- [Installation - Keeping It Simple](#installation---keeping-it-simple)
    - [Option 1: Copy and Paste (The Easiest Way)](#option-1-copy-and-paste-the-easiest-way)
    - [Option 2: Using `pip` (For the Pros)](#option-2-using-pip-for-the-pros)
    - [Option 3: Installing to Python's Builtins (Advanced & Risky)](#option-3-installing-to-pythons-builtins-advanced--risky)
- [Package Structure - Know Your Tools](#package-structure---know-your-tools)
- [Output Format Examples - See It to Believe It](#output-format-examples---see-it-to-believe-it)
    - [Basic `jp` Usage](#basic-jp-usage)
    - [Basic `jprint` Usage](#basic-jprint-usage)
    - [Custom Prefix](#custom-prefix)
    - [Pretty Print](#pretty-print)
    - [Logging Output](#logging-output)
- [Advanced Usage - Level Up Your Debugging Game](#advanced-usage---level-up-your-debugging-game)
- [Troubleshooting - When Things Get Tricky](#troubleshooting---when-things-get-tricky)
    - [Common Issues](#common-issues)
- [Let's Level Up Together!](#lets-level-up-together)
- [License - Keeping It Open and Free](#license---keeping-it-open-and-free)

<br>

## What's `jprinter` All About? 🤔

<div align="justify">
    <code>jprinter</code> is here to replace that basic <code>print()</code> function and bring your debugging game into the future! 🚀 We know that debugging can be a pain, so we've built this tool with all the features you need to make it real, fast, and efficient. 😤
</div>

<br>

## Key Features That Keep It 💯

<div align="justify">
    <ul>
        <li><strong>Enhanced Output:</strong> See variable values, context (filename, line number, function name) all in one clean output.</li>
        <li><strong>Customizable Prefixes:</strong> Set a custom prefix to make sure you know what's being printed from which part of your code! 🗣️</li>
        <li><strong>Built-in Context:</strong> Automatically adds the file name, line number, and function name, so you always know where the action is! 📍</li>
        <li><strong>Colorized Output:</strong> Make your output stand out with custom colors that make it easier to read. 🎨</li>
        <li><strong><code>sep</code> and <code>end</code>:</strong> Full control over separators and end-of-line characters, just like the original <code>print()</code>. 🔤</li>
        <li><strong>Pretty Printing:</strong> Nicely format complex data structures like dictionaries and lists so they're easy to read. ✨</li>
        <li><strong>File Logging:</strong> Log all your output to a file, with or without timestamps, for keeping track of everything. 📝</li>
         <li><strong>Global Enable/Disable:</strong> Turn off all <code>jprinter</code> output with a single command so you can clean up the console when needed. 📴</li>
        <li><strong>Log Function:</strong> Output different log levels (debug, info, warning, error) for better organization and clarity! 🗂️</li>
    </ul>
</div>

<br>

## How to Use `jprinter` Like a Pro

### Basic Usage with `jp` and `jprint`

Here's a basic example of how to use `jprint` and its shortcut, `jp`:

```python
from jprinter import jp, jprint

# Using jp for a quick print statement
jp("Hello, world!")

# Using jprint with multiple arguments
jprint("This is", "a", "test")
```

### Logging with Different Levels

You can log with different levels using the `log` function:

```python
from jprinter import log

log("This is a debug message", level="debug")
log("This is an info message", level="info")
log("This is a warning message", level="warning")
log("This is an error message", level="error")
```

### Global Enable/Disable

You can disable and enable all `jprinter` output using the `JPrintDebugger` class:

```python
from jprinter import jp
from jprinter.core import JPrintDebugger

jp("This will be printed")
JPrintDebugger.disable_all()
jp("This will not be printed")
JPrintDebugger.enable_all()
jp("This will be printed again")
```

### Custom Prefixes

Set custom prefixes for different debugging sections:

```python
from jprinter import jp

jp("Debug info here", prefix="DEBUG >>> ")
jp("Important note", prefix="NOTE >>> ")
```

### Pretty Printing Complex Data Structures

Format complex data structures for readability:

```python
from jprinter import jp

data = {"name": "HAI", "age": 17, "hobbies": ["coding", "gaming", "reading"]}
jp(data, pprint_options={"indent": 4})
```

### Custom Separators

Use custom separators:

```python
from jprinter import jp

jp("Keep", "it", "real", sep=" - ")
```

### File Logging

Log your output to a file:

```python
from jprinter import jp

jp("This is a log message", log_file="debug.log")
```

<br>

## Installation - Keeping It Simple

### Option 1: Copy and Paste (The Easiest Way)

Just drop the `jprinter` folder into your project's directory, and you're good to go! 💯 No extra installations needed.

### Option 2: Using `pip` (For the Pros)

If you like to keep it clean, install `jprinter` with pip:

```bash
pip install jprinter
```

### Option 3: Installing to Python's Builtins (Advanced & Risky)

**⚠️ WARNING: Modifying Python's builtins can cause issues and is not recommended. Proceed with caution!**

To use `jprinter` as a built-in function, edit `builtins.py` in your Python installation:

1.  **Locate `builtins.py`:** Usually found in your Python installation directory.
2.  **Edit `builtins.py`:** Add the following lines to the file:

    ```python
    from jprinter import jprint as print
    ```
3.  **Restart Python:** This will make the changes effective.

<br>

## Package Structure - Know Your Tools

<div align="justify">
   Here's a breakdown of the key files:
    <ul>
    <li><strong><code>__init__.py</code>:</strong> Initializes the <code>jprinter</code> package.</li>
    <li><strong><code>builtins.py</code>:</strong> Functions to integrate <code>jprinter</code> with Python builtins.</li>
     <li><strong><code>coloring.py</code>:</strong> Handles the color magic.</li>
    <li><strong><code>core.py</code>:</strong> The heart of <code>jprinter</code> with all the core functionality.</li>
    <li><strong><code>jp.py</code>:</strong> The <code>jp</code> function for quick debugging.</li>
    <li><strong><code>jprint.py</code>:</strong> The main module for <code>jprint</code>.</li>
    <li><strong><code>README.md</code>:</strong> This file, for all the important documentation.</li>
    </ul>
</div>

<br>

## Output Format Examples - See It to Believe It

### Basic `jp` Usage

```python
from jprinter import jp
jp("Hello, world!")
```

**Output:**

```
JARVIS -> [test_jprint.py:2] in () >>> Hello, world!
```

### Basic `jprint` Usage

```python
from jprinter import jprint
jprint("Hello, world!")
```

**Output:**

```
JARVIS -> [test_jprint.py:2] in () >>> Hello, world!
```

### Custom Prefix

```python
from jprinter import jp
jp("Hello, world!", prefix="DEBUG >>> ")
```

**Output:**

```
DEBUG >>> [test_jprint.py:2] in () >>> Hello, world!
```

### Pretty Print

```python
from jprinter import jp
data = {"name": "HAI", "age": 17, "hobbies": ["coding", "gaming", "reading"]}
jp(data, pprint_options={"indent": 4})
```

**Output:**

```
JARVIS -> [test_jprint.py:2] in () >>> {
    "name": "HAI",
    "age": 17,
    "hobbies": [
        "coding",
        "gaming",
        "reading"
    ]
}
```

### Logging Output

```python
from jprinter import log
log("This is a warning", level="warning")
```

**Output:**

```
[WARNING] JARVIS -> [test_jprint.py:2] in () >>> This is a warning
```

<br>

## Advanced Usage - Level Up Your Debugging Game

See how to use the global enable/disable and logging in the [How to Use](#how-to-use-jprinter-like-a-pro) section.

<br>

## Troubleshooting - When Things Get Tricky

### Common Issues

1.  **`ImportError`**: Make sure you have installed or copied the files properly.
2.  **Output Not Working**: Make sure the `JPrintDebugger` is enabled and configured.

<br>

## Let's Level Up Together!

<div align="justify">
    Feel free to contribute to the project by submitting issues or pull requests. Let's make <code>jprinter</code> the best tool for all the devs out there! 💪
</div>

<br>

Your boy,

HAI 🙋‍♂️

<br>

## License - Keeping It Open and Free

<div align="justify">
    This project is licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>.
</div>
