from collections import defaultdict
from sortedcontainers import SortedDict # type: ignore
import time
class BrowserHistory:
    def __init__(self):
        self.url_data = {}  # {url: [frequency, last_timestamp]}
        self.sorted_history = SortedDict()  # Sorted by (-freq, -timestamp) for O(log n) retrieval

    def geturl(self, url):
        """Record a URL visit."""
        current_time = time.time()  # Use current timestamp
        
        # If URL is already visited, update frequency and timestamp
        if url in self.url_data:
            freq, timestamp = self.url_data[url]
            # Remove old entry from sorted history
            self.sorted_history.pop((-freq, -timestamp))
            freq += 1  # Increment frequency
        else:
            freq = 1  # First-time visit

        # Update timestamp and store data
        self.url_data[url] = [freq, current_time]
        # Add updated entry to sorted history
        self.sorted_history[(-freq, -current_time)] = url

    def getbrowserhistory(self):
        """Retrieve browser history sorted by frequency and timestamp."""
        # Return sorted URLs
        return [url for _, url in self.sorted_history.items()]
"""
def getbrowserhistory(self):
    sorted_urls = sorted(
        self.url_data.items(),
        key=lambda x: (-x[1][0], -x[1][1])  # Sort by (-freq, -timestamp)
    )
    return [url for url, _ in sorted_urls]
"""


# Example Usage
history = BrowserHistory()
history.geturl("BBC")
history.geturl("Google")
history.geturl("Facebook")
print(history.getbrowserhistory())  # Output: ['Facebook', 'Google', 'BBC']

history.geturl("BBC")
history.geturl("BBC")
history.geturl("Google")
print(history.getbrowserhistory())  # Output: ['BBC', 'Google', 'Facebook']
