import subprocess

def open_app(app_name):
    """Open a macOS application by name."""
    try:
        subprocess.run(["open", "-a", app_name], check=True)
        print(f"Successfully opened {app_name}.")
    except FileNotFoundError:
        print(f"Application not found: {app_name}. Please ensure the name is correct (e.g., 'Zoom.us').")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open {app_name}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")