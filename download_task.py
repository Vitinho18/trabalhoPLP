from network_task import NetworkTask
import threading
import time
import random

class DownloadTask(NetworkTask):
    def __init__(self, url, file_name):
        super().__init__(url)
        self.file_name = file_name
        self.progress = 0
        self.paused = threading.Event()
        self.paused.set()  # Inicialmente, a tarefa não está pausada
        self.cancelled = False

    def pause(self):
        self.paused.clear()

    def resume(self):
        self.paused.set()

    def cancel(self):
        self.cancelled = True

    def execute(self):
        print(f"Starting download: {self.file_name} from {self.url}")
        self.status = 'downloading'
        for _ in range(5):
            if self.cancelled:
                self.status = 'cancelled'
                print(f"Download cancelled: {self.file_name}")
                return
            self.paused.wait()  # Espera se estiver pausado
            time.sleep(random.uniform(0.5, 1.5))  # Simulando tempo de download
            self.progress += 20
            print(f"{self.file_name}: {self.progress}% complete")
        self.status = 'completed'
        print(f"Download completed: {self.file_name}")
