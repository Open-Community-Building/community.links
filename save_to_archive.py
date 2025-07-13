import requests
import time
from urllib.parse import quote
from config import not_on_archive_list


class WaybackSubmitter:

    def __init__(self):
        self.base_url = "https://web.archive.org/save/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; ArchiveBot/1.0)'
        })

    def submit_url(self, url, capture_all=False, capture_outlinks=False):
        """
        Submit a URL to the Wayback Machine.

        Args:
            url (str): The URL to archive
            capture_all (bool): Whether to capture all page resources
            capture_outlinks (bool): Whether to capture outlinks

        Returns:
            dict: Response information
        """
        # URL encode the target URL
        encoded_url = quote(url, safe=':/?#[]@!$&\'()*+,;=')

        # Build the save URL
        save_url = f"{self.base_url}{encoded_url}"

        # Add optional parameters
        params = {}
        if capture_all:
            params['capture_all'] = 'on'
        if capture_outlinks:
            params['capture_outlinks'] = 'on'

        try:
            response = self.session.get(save_url, params=params, timeout=60)

            if response.status_code == 200:
                return {
                    "success": True,
                    "original_url": url,
                    "archived_url": response.url,
                    "timestamp": time.time(),
                    "status_code": response.status_code
                }
            else:
                return {
                    "success": False,
                    "original_url": url,
                    "status_code": response.status_code,
                    "error": response.text[:200]  # First 200 chars of error
                }

        except requests.RequestException as e:
            return {
                "success": False,
                "original_url": url,
                "error": str(e)
            }

    def submit_multiple_urls(self, urls, delay=5):
        """
        Submit multiple URLs with a delay between requests.

        Args:
            urls (list): List of URLs to archive
            delay (int): Delay in seconds between requests

        Returns:
            list: List of results for each URL
        """
        results = []

        for i, url in enumerate(urls):
            print(f"Submitting {i+1}/{len(urls)}: {url}")
            result = self.submit_url(url)
            results.append(result)

            if i < len(urls) - 1:  # Don't delay after the last URL
                time.sleep(delay)

        return results


def run():
    wayback = WaybackSubmitter()
    results = wayback.submit_multiple_urls(not_on_archive_list, delay=3)
    for result in results:
        print(f"{result['original_url']}: {'✓' if result['success'] else '✗'}")


if __name__ == "__main__":
    run()
