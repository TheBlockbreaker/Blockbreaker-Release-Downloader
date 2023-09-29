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

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
