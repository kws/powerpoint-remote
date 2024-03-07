# Controlling PowerPoint with Python, PyAutoGUI, and Flask

This is the code to accompany the blog post at: <https://www.k-si.com/2024/03/07/pythonautogui-powerpoint-presenter.html>

## Installation

```bash
poetry install
``` 

## Usage

```bash
powerpoint-remote
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Notes

Currently the keyboard shortcuts are for windows and the program makes no attempt to check the operating system. It is trivial to extend this, but if you need to run on a different OS, you will need to modify the keyboard shortcuts in `app.py` for now.

More about PowerPoint keyboard shortcuts here:

- <https://support.microsoft.com/en-au/office/use-keyboard-shortcuts-to-deliver-powerpoint-presentations-1524ffce-bd2a-45f4-9a7f-f18b992b93a0>