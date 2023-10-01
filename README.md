# Google Image Downloader

This Python script allows you to download images from Google Images based on a specified search term. It uses Selenium to automate the process of searching for images, clicking on them to reveal the full-size image, and then downloading those images to a specified folder.

## How to Use

1. Clone the repository or download the script.

2. Install the required Python packages if you haven't already. You can install them using pip:

   ```bash
   pip install selenium requests Pillow
   ```

3. Ensure you have a compatible web driver installed and add its path to the script. You can download web drivers for different browsers like Chrome or Firefox.

4. Modify the following variables in the script to match your preferences:

   - `search_term`: Specify the term you want to search for on Google Images.
   - `target_path`: Provide the path to the folder where you want to save the downloaded images.
   - `number_of_images`: Set the maximum number of images to download.
   - `sleep_time`: Adjust the sleep time between interactions with the web page.

5. Run the script:

   ```bash
   python google_image_downloader.py
   ```

6. The script will start searching for images based on the provided search term and download them to the specified folder.

## Important Note

- This script uses Selenium and web scraping to interact with Google Images. Make sure you comply with Google's terms of service and usage policies while using this script. Unauthorized scraping may violate their terms.

## License

Specify the license under which your project is distributed. If you're not sure which license to choose, you can visit [choosealicense.com](https://choosealicense.com/) for guidance.



