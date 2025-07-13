import os
import requests
import json
from typing import Optional, Dict, Any
from config import *


def is_url_archived(url: str) -> Dict[str, Any]:
    """
    Check if a URL is archived on archive.org using the Wayback Machine API.

    Args:
        url (str): The URL to check

    Returns:
        Dict containing:
        - 'archived': bool - Whether the URL is archived
        - 'latest_snapshot': str or None - Latest archived snapshot URL
        - 'first_snapshot': str or None - First archived snapshot URL
        - 'total_snapshots': int - Total number of snapshots
        - 'error': str or None - Error message if any
    """

    # Wayback Machine availability API endpoint
    api_url = "http://archive.org/wayback/available"

    try:
        # Make request to check availability
        response = requests.get(api_url, params={'url': url}, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Check if archived snapshots exist
        archived_snapshots = data.get('archived_snapshots', {})
        closest = archived_snapshots.get('closest', {})

        if closest and closest.get('available'):
            return {
                'archived': True,
                'latest_snapshot': closest.get('url'),
                'timestamp': closest.get('timestamp'),
                'status': closest.get('status'),
                'total_snapshots': None,  # This API doesn't provide count
                'error': None
            }
        else:
            return {
                'archived': False,
                'latest_snapshot': None,
                'timestamp': None,
                'status': None,
                'total_snapshots': 0,
                'error': None
            }

    except requests.RequestException as e:
        return {
            'archived': False,
            'latest_snapshot': None,
            'timestamp': None,
            'status': None,
            'total_snapshots': 0,
            'error': f"Request error: {str(e)}"
        }
    except json.JSONDecodeError as e:
        return {
            'archived': False,
            'latest_snapshot': None,
            'timestamp': None,
            'status': None,
            'total_snapshots': 0,
            'error': f"JSON decode error: {str(e)}"
        }

def get_snapshot_count(url: str) -> Optional[int]:
    """
    Get the total number of snapshots for a URL using the CDX API.
    This provides more detailed information but may be slower.

    Args:
        url (str): The URL to check

    Returns:
        int: Number of snapshots, or None if error
    """

    cdx_api_url = "http://web.archive.org/cdx/search/cdx"

    try:
        params = {
            'url': url,
            'output': 'json',
            #'fl': 'timestamp',
            'collapse': 'digest'  # Collapse duplicate content
        }

        response = requests.get(cdx_api_url, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        # First row contains headers, so subtract 1
        return len(data) - 1 if len(data) > 1 else 0

    except (requests.RequestException, json.JSONDecodeError, ValueError):
        return None


def wayback_to_html(timestamp, wayback_url):
    """Fetch a Wayback Machine snapshot"""
    target = HTML_FOLDER + timestamp + '.html'
    if os.path.isfile(target):
        return
    try:
        response = requests.get(wayback_url)
        if response.status_code == 200:
            # Create PDF from HTML content
            html = response.text
            with open(target, 'w') as ia_html:
                ia_html.write(html)
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def run(links):
    # Test URLs
    for url in links:
        print(f"\nChecking: {url}")
        result = is_url_archived(url)

        if result['error']:
            print(f"Error: {result['error']}")
        else:
            if result['archived']:
                print(f"✓ Archived: Yes")
                print(f"  Latest snapshot: {result['latest_snapshot']}")
                print(f"  Timestamp: {result['timestamp']}")
                print(f"  Status: {result['status']}")
                # Usage
                wayback_to_html(result['timestamp'], result['latest_snapshot'])

# Example usage
if __name__ == "__main__":
    run(on_archive_list)




