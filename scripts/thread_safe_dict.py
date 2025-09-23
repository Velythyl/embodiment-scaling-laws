import psutil
import os
import time
import numpy as np
from collections import OrderedDict
import threading


import threading

class ThreadSafeSingleEntryDict:
    def __init__(self, max_size):
        assert max_size == 1, f"max_size must be 1, but got {max_size}"
        self.key = None
        self.value = None
        self.lock = threading.RLock()

    def get(self, key):
        """Retrieve the value if the key exists."""
        with self.lock:
            if key == self.key:
                return self.value
            else:
                return None

    def put(self, key, value):
        """
        Insert or update the key-value pair.
        Since this dictionary supports only one entry, any existing key-value pair will be replaced.
        """
        with self.lock:
            self.key = key
            self.value = value

    def delete(self):
        """Delete the stored key-value pair."""
        with self.lock:
            self.key = None
            self.value = None

    def has_key(self, key):
        """Check if the stored key matches the given key."""
        with self.lock:
            return self.key == key

    def clear(self):
        """Clear the dictionary."""
        self.delete()

    def current_key(self):
        """Retrieve the current key."""
        with self.lock:
            return self.key


# ThreadSafeDict implementation
class ThreadSafeDict:
    def __init__(self, max_size):
        self.dict = OrderedDict()
        self.lock = threading.RLock()
        self.max_size = max_size

    def get(self, key):
        with self.lock:
            if key in self.dict:
                self.dict.move_to_end(key)  # Mark as recently used
                return self.dict[key]
            return None

    def put(self, key, value):
        with self.lock:
            if key in self.dict:
                self.dict.move_to_end(key)  # Update usage order
            self.dict[key] = value
            if len(self.dict) > self.max_size:
                item = self.dict.popitem(last=False)  # Remove oldest item
                del item

    def delete(self, key):
        with self.lock:
            if key in self.dict:
                del self.dict[key]

    def clear(self):
        with self.lock:
            self.dict.clear()

    def keys(self):
        """
        Get all the keys in the dictionary.

        Returns:
            list: A list of all keys in the dictionary.
        """
        with self.lock:
            return self.dict.keys()

    def __len__(self):
        return len(self.dict)

#
# class ThreadSafeDict:
#     def __init__(self, max_size, manager_dict=None):
#         """
#         A thread/process-safe dictionary with an optional size limit.
#
#         Args:
#             max_size (int): Maximum number of items in the dictionary.
#             manager_dict: An optional multiprocessing.Manager().dict().
#                           If None, an in-memory OrderedDict is used.
#         """
#         self.dict = manager_dict if manager_dict is not None else OrderedDict()
#         self.max_size = max_size
#
#     def get(self, key):
#         """
#         Retrieve a value from the dictionary.
#
#         Args:
#             key: The key to retrieve.
#
#         Returns:
#             The value associated with the key, or None if the key is not present.
#         """
#         if key in self.dict:
#             # Move key to the end if using OrderedDict (for LRU behavior)
#             if isinstance(self.dict, OrderedDict):
#                 self.dict.move_to_end(key)
#             return self.dict[key]
#         return None
#
#     def put(self, key, value):
#         """
#         Add or update a key-value pair in the dictionary.
#
#         Args:
#             key: The key to add or update.
#             value: The value to associate with the key.
#         """
#         if key in self.dict:
#             # Move key to the end if using OrderedDict (for LRU behavior)
#             if isinstance(self.dict, OrderedDict):
#                 self.dict.move_to_end(key)
#         self.dict[key] = value
#         # Enforce max size for OrderedDict
#         if isinstance(self.dict, OrderedDict) and len(self.dict) > self.max_size:
#             self.dict.popitem(last=False)  # Remove the oldest item
#
#     def delete(self, key):
#         """
#         Remove a key-value pair from the dictionary.
#
#         Args:
#             key: The key to remove.
#         """
#         if key in self.dict:
#             del self.dict[key]
#
#     def clear(self):
#         """
#         Clear all items from the dictionary.
#         """
#         self.dict.clear()
#
#     def keys(self):
#         """
#         Retrieve all keys in the dictionary.
#
#         Returns:
#             A list of all keys.
#         """
#         return list(self.dict.keys())

# Function to monitor memory usage
def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB


# Function to get system-wide memory information
def get_system_ram_usage():
    """
    Returns system-wide memory usage statistics.
    Returns:
        total (float): Total system memory in MB.
        used (float): Used system memory in MB.
        available (float): Available system memory in MB.
    """
    memory = psutil.virtual_memory()
    total = memory.total / (1024 ** 2)  # Convert bytes to MB
    used = memory.used / (1024 ** 2)    # Convert bytes to GB
    available = memory.available / (1024 ** 3)  # Convert bytes to GB
    return used


# Test the ThreadSafeDict with large NumPy arrays
def test_memory_leak():
    print("Starting memory leak test with large NumPy arrays...")
    max_size = 1  # Maximum number of items in cache
    cache = ThreadSafeSingleEntryDict(max_size=max_size)
    array_size = (10, 4096, 300)  # Large NumPy array size (1 million elements)

    initial_memory = memory_usage()
    print(f"Initial Memory Usage: {initial_memory:.2f} MB")

    # Insert large NumPy arrays into the cache
    for i in range(1_000_000):
        large_array = np.random.rand(*array_size)  # Create a large NumPy array
        cache.put(i, large_array)  # Insert into cache

        if i % 10 == 0:  # Check memory usage periodically
            current_memory = memory_usage()
            print(f"Iteration {i}, Process Memory Usage: {current_memory:.2f} MB, Sys Memory Usage: {get_system_ram_usage():.2f} MB")

            # # Stop test if memory usage grows excessively (indicates a leak)
            # if current_memory - initial_memory > 500:  # Allowable growth of 500 MB
            #     print("Potential memory leak detected!")
            #     break

    final_memory = memory_usage()
    print(f"Final Memory Usage: {final_memory:.2f} MB")
    print("Memory leak test complete.")


if __name__ == "__main__":
    test_memory_leak()
