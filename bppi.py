# BPPI - Blxsted's python package installer
# discord - blxstedxd
# add me to submit bugs etc etc
import subprocess

def install_package(package_name):
    try:
        subprocess.check_call(["pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}. Error: {e}")

def main():
    while True:
        # Get user input
        user_input = input("Enter a command: ")

        # Parse the user input
        if user_input.startswith("bppi install"):
            # Extract the package name from the input
            package_name = user_input.split(" ")[2]
            install_package(package_name)
        elif user_input.lower() == "exit":
            break  # Exit the loop if the user types "exit"
        else:
            print("Invalid command. Type 'bppi install package_name' to install a package.")

if __name__ == "__main__":
    main()
# Please install from github or using pip install bppi