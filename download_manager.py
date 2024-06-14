import json
from logger import Logger
from download_task import DownloadTask

class DownloadManager:
    def __init__(self):
        self.tasks = []
        self.logger = Logger()

    def add_task(self, task):
        self.tasks.append(task)
        self.logger.log(f"Download task for {task.file_name} added.")

    def remove_task(self, file_name):
        for task in self.tasks:
            if task.file_name == file_name:
                if task.status == 'downloading':
                    self.logger.log(f"Cannot remove {file_name}, it's currently downloading.")
                    return
                self.tasks.remove(task)
                self.logger.log(f"Download task for {file_name} removed.")
                return
        self.logger.log(f"Download task for {file_name} not found.")

    def list_tasks(self):
        if not self.tasks:
            self.logger.log("No download tasks available.")
        for task in self.tasks:
            self.logger.log(f"File: {task.file_name}, URL: {task.url}, Status: {task.status}, Progress: {task.progress}%")

    def execute_tasks(self):
        threads = []
        for task in self.tasks:
            if task.status == 'pending':
                thread = threading.Thread(target=task.execute)
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()

    def pause_task(self, file_name):
        for task in self.tasks:
            if task.file_name == file_name:
                if task.status == 'downloading':
                    task.pause()
                    self.logger.log(f"Download task for {file_name} paused.")
                    return
        self.logger.log(f"Download task for {file_name} not found or not downloading.")

    def resume_task(self, file_name):
        for task in self.tasks:
            if task.file_name == file_name:
                if task.status == 'downloading':
                    task.resume()
                    self.logger.log(f"Download task for {file_name} resumed.")
                    return
        self.logger.log(f"Download task for {file_name} not found or not downloading.")

    def cancel_task(self, file_name):
        for task in self.tasks:
            if task.file_name == file_name:
                task.cancel()
                self.logger.log(f"Download task for {file_name} cancelled.")
                return
        self.logger.log(f"Download task for {file_name} not found.")

    def save_state(self, filename):
        state = [{
            'url': task.url,
            'file_name': task.file_name,
            'status': task.status,
            'progress': task.progress
        } for task in self.tasks]
        with open(filename, 'w') as f:
            json.dump(state, f)
        self.logger.log(f"Download manager state saved to {filename}.")

    def load_state(self, filename):
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            self.tasks = [DownloadTask(task['url'], task['file_name']) for task in state]
            for task, saved_task in zip(self.tasks, state):
                task.status = saved_task['status']
                task.progress = saved_task['progress']
            self.logger.log(f"Download manager state loaded from {filename}.")
        except FileNotFoundError:
            self.logger.log(f"File {filename} not found.")
