# Blockbreaker's GitHub Release Downloader
![me!!!!](https://s3.emk530.net/IMG_0142.png)

This Python script allows you to download the latest release from a GitHub repository, extract its contents, and store them in a specified target folder.

## Getting Started

### Prerequisites

Make sure you have Python and `pip` installed on your system. You'll also need to install the required Python packages. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone this repository or download the `main.py` file.

2. Open a terminal or command prompt in the directory where `main.py` is located.

3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. The script will prompt you to select a release to download or specify 'latest' for the latest release. It will clear the contents of the target folder, download the release, extract its contents, and store them in the target folder.

### Configuration

You can configure the following parameters in the script:

- `repository_owner`: The owner of the GitHub repository.
- `repository_name`: The name of the GitHub repository.
- `github_token`: Your GitHub Personal Access Token.
- `target_folder`: The folder where you want to store the downloaded and extracted files.

Please make sure to keep your GitHub token and sensitive information secure.

## Creating an Executable (Optional)

You have the option to convert the `main.py` script into a standalone executable using PyInstaller. This can be useful if you want to distribute the application as an executable file that doesn't require users to have Python installed.

To create an executable, follow these steps:

1. Install PyInstaller if you haven't already:

   ```bash
   pip install pyinstaller
   ```

2. Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. Run the following command to create the executable:

   ```bash
   pyinstaller --onefile main.py
   ```

   This will generate a `dist` directory containing the executable file.

4. You can now distribute the executable to others. They can run the program without needing to install Python or any dependencies separately.

Choose this option if you want to provide a convenient way for users to run the application without Python.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
