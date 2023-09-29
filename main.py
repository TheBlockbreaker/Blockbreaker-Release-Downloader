import os
import requests
import zipfile
from tqdm import tqdm
import shutil

# GitHub repository information
repository_owner = "changetoyourname"
repository_name = "changetoyourrepo"
github_token = "changetoyourtoken"  # Your GitHub token
target_folder = "target"  # Specify your target folder here

# GitHub API request to get the list of releases
releases_url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/releases"
headers = {"Authorization": f"token {github_token}"}

try:
    response = requests.get(releases_url, headers=headers)
    response.raise_for_status()
    releases_data = response.json()

    if not releases_data:
        print("No releases found in the repository.")
    else:
        # List available releases and let the user choose
        print("Available releases:")
        for i, release in enumerate(releases_data):
            print(f"{i + 1}. {release['name']}")

        release_choice = input("Enter the number of the release to download (or 'latest' for the latest release): ")

        if release_choice.lower() == "latest":
            # Download the latest release
            release_data = releases_data[0]
        else:
            try:
                choice_index = int(release_choice) - 1
                if 0 <= choice_index < len(releases_data):
                    release_data = releases_data[choice_index]
                else:
                    print("Invalid choice. Please enter a valid release number.")
                    exit(1)
            except ValueError:
                print("Invalid choice. Please enter a valid release number or 'latest'.")
                exit(1)

        # Clear the target folder
        if os.path.exists(target_folder):
            shutil.rmtree(target_folder)
        os.makedirs(target_folder)

        # Get the assets of the selected release
        assets = release_data.get('assets')
        if not assets:
            print("No assets found in the selected release.")
            exit(1)

        # Get the asset download URL
        download_url = assets[0].get("browser_download_url")  # Using the first available asset

        # Get the total file size to display the progress bar
        response = requests.head(download_url)
        total_size = int(response.headers.get('content-length', 0))

        # Download the asset with a progress bar
        target_path = os.path.join(target_folder, os.path.basename(download_url))  # Full path including the target folder

        with requests.get(download_url, stream=True) as response:
            response.raise_for_status()
            with open(target_path, 'wb') as asset_file:
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as progress_bar:
                    for data in response.iter_content(chunk_size=1024):
                        asset_file.write(data)
                        progress_bar.update(len(data))

        print(f"Downloaded {os.path.basename(download_url)} to {target_path} successfully.")

        # Unzip the downloaded file to the target folder
        with zipfile.ZipFile(target_path, 'r') as zip_ref:
            zip_ref.extractall(target_folder)

        # Clean up - remove the zip file
        os.remove(target_path)

        print(f"Extracted contents to {target_folder} successfully.")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
