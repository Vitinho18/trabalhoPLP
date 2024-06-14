from download_manager import DownloadManager
from download_task import DownloadTask

def main():
    manager = DownloadManager()
    
    while True:
        print("\nDownload Manager")
        print("1. Add Download")
        print("2. Remove Download")
        print("3. List Downloads")
        print("4. Execute Downloads")
        print("5. Pause Download")
        print("6. Resume Download")
        print("7. Cancel Download")
        print("8. Save State")
        print("9. Load State")
        print("10. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            url = input("Enter download URL: ")
            file_name = input("Enter file name: ")
            task = DownloadTask(url, file_name)
            manager.add_task(task)
        elif choice == '2':
            file_name = input("Enter file name to remove: ")
            manager.remove_task(file_name)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            manager.execute_tasks()
        elif choice == '5':
            file_name = input("Enter file name to pause: ")
            manager.pause_task(file_name)
        elif choice == '6':
            file_name = input("Enter file name to resume: ")
            manager.resume_task(file_name)
        elif choice == '7':
            file_name = input("Enter file name to cancel: ")
            manager.cancel_task(file_name)
        elif choice == '8':
            filename = input("Enter filename to save state: ")
            manager.save_state(filename)
        elif choice == '9':
            filename = input("Enter filename to load state: ")
            manager.load_state(filename)
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
