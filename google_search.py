from googlesearch import search
import subprocess
import tqdm
import time

class GoogleSearch:

    def __init__(self, query, num_results = 20, timeout = 900, depth = 3, max_processes = 3):

        # Define the search query
        self.query = query

        # Perform the search and retrieve the links
        self.num_results = num_results  # Number of search results to retrieve
        self.timeout = timeout # Number of seconds before a scrapy stop
        self.depth = depth

        self.max_processes = max_processes  # Maximum number of processes to run concurrently

        self.running_processes = []  # List to hold currently running processes


    # Function to check the status of running processes
    def check_process_status(self):
        terminated_processes = []
        for process in self.running_processes:
            if process.poll() is not None:  # Process has terminated
                terminated_processes.append(process)
        for process in terminated_processes:
            self.running_processes.remove(process)
        return len(self.running_processes)

    # Function to create new processes if needed
    def create_new_processes(self, url):
        # Create a new process and append it to the list
        # new_process = subprocess.Popen(["python", "DbScraper/trigger.py", "--url", url, "--timeout", str(self.timeout), "--depth", str(self.depth)])
        new_process = subprocess.Popen(["python", "DbScraper/trigger.py", "--url", url, "--timeout", str(self.timeout), "--depth", str(self.depth)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.running_processes.append(new_process)

    def start(self):
        # Main loop to continuously check and create processes
        search_results = search(self.query, num_results=self.num_results, lang="jp")
        while True:
            running_count = self.check_process_status()
            print(f"Running processes: {running_count}")

            if running_count < self.max_processes:
                url = next(search_results, None)
                if url is not None:
                    print(url)
                    self.create_new_processes(url)

            if running_count == 0 and len(self.running_processes) == 0:
                break  # All processes have terminated

            time.sleep(1)  # Sleep for 1 second before checking again

####
# Language loop