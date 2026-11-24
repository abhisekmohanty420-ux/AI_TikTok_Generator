
import os

# Get the directory where generate_process.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
DONE_FILE = os.path.join(BASE_DIR, "done.txt")


def text_to_audio(folder):
    print("TTA", folder)


def create_reel(folder):
    print("CA", folder)


if __name__ == "__main__":

    # Create uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Create done.txt if it doesn't exist
    if not os.path.exists(DONE_FILE):
        open(DONE_FILE, "w").close()

    # Read already processed folders
    with open(DONE_FILE, "r") as f:
        done_folder = f.read().splitlines()

    # Get all folders from uploads
    folders = os.listdir(UPLOAD_FOLDER)

    print("All folders:", folders)
    print("Completed folders:", done_folder)

    for folder in folders:

        folder_path = os.path.join(UPLOAD_FOLDER, folder)

        # Process only directories
        if os.path.isdir(folder_path) and folder not in done_folder:

            text_to_audio(folder)
            create_reel(folder)

            # Save completed folder name
            with open(DONE_FILE, "a") as f:
                f.write(folder + "\n")

            print(folder, "completed successfully!")

