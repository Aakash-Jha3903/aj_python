def Current_Working_Directory_and_Directory_Operations():
    import os

    # Get current working directory
    current_directory = os.getcwd()
    print("Current Working Directory:", current_directory)

    # List files in the current directory
    files_in_directory = os.listdir()
    print("Files in Current Directory:", files_in_directory)

    # Change directory
    new_directory = "example_directory"
    os.mkdir(new_directory)
    os.chdir(new_directory)

    # List files in the new directory
    files_in_new_directory = os.listdir()
    print("Files in New Directory:", files_in_new_directory)

def Path_Manipulation():
    import os

    # Join paths
    path1 = "folder"
    path2 = "file.txt"
    full_path = os.path.join(path1, path2)  
    print("Full Path:", full_path)

    # Get absolute path
    absolute_path = os.path.abspath(full_path)
    print("Absolute Path:", absolute_path)

    # Get directory and basename
    directory_name = os.path.dirname(full_path)
    base_name = os.path.basename(full_path)
    print("Directory Name:", directory_name)
    print("Base Name:", base_name)

def File_and_Directory_Information():
    import os

    # Check if a path exists
    path_to_check = "example_directory"
    if os.path.exists(path_to_check):
        print(f"{path_to_check} exists.")

    # Check if it's a file or directory
    if os.path.isdir(path_to_check):
        print(f"{path_to_check} is a directory.")
    elif os.path.isfile(path_to_check):
        print(f"{path_to_check} is a file.")  

def  File_and_Directory_Manipulation():
    import os

    # Remove a file
    file_to_remove = "example_file.txt"
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)
        print(f"{file_to_remove} removed.")

    # Remove a directory
    directory_to_remove = "example_directory"
    if os.path.exists(directory_to_remove):
        os.rmdir(directory_to_remove)
        print(f"{directory_to_remove} removed.")

def Executing_Shell_Commands():
    import os  

    # Execute a shell command
    # os.system("echo Hello, OS Module!")
    
    # Print the current working directory
    # os.system("cd")

    # List files in the current directory
    # os.system("dir")

    # Display system information
    # os.system("systeminfo")

    # Display Network Configuration
    # os.system('ipconfig /all')

    # os.system('ping localhost')

    ### os.system('shutdown /s /t 0')  # Shutdown
    ### os.system('shutdown /r /t 0')  # Restart

    # Replace 'YourWiFiName' with the actual name of your Wi-Fi network
    # wifi_name = 'unhackable'
    # Run the netsh command
    # os.system(f'netsh wlan show profile name={wifi_name} key=clear')


    # Run a custom command
    # os.system("python 100_Days_of_code_python\\range_fun.py")
    

def Environment_Variables():
    import os

    # Get the value of an environment variable
    username = os.getenv("USER", "Guest")
    print("Current User:", username)

    # Access the entire environment variables dictionary
    all_env_variables = os.environ
    print("All Environment Variables:", all_env_variables)




#..........................................................................................
#..........................................................................................
#..........................................................................................
#..........................................................................................
    
# Most Popular os functions : 
def popular(mod):
    def Working_with_Directories():
        import os

        # Example 1: Get the current working directory
        current_directory = os.getcwd()
        print("Current Directory:", current_directory)

        # Example 2: Change the current working directory
        new_directory = '/path/to/new_directory'
        os.chdir(new_directory)

        # Example 3: List files in the current directory
        files_in_directory = os.listdir()
        print("Files in Directory:", files_in_directory)

    def Path_Manipulation():
        import os
        # Example 4: Joining path components
        path = os.path.join('/root', 'folder', 'file.txt')
        print("Joined Path:", path)

        # Example 5: Checking if a path exists
        exists = os.path.exists('/path/to/existing/file.txt')
        print("Path Exists:", exists)

    def File_and_Directory_Operations():
        import os

        # Example 6: Creating a new directory
        os.mkdir('/path/to/new_directory')

        # Example 7: Creating a directory and its parents
        os.makedirs('/path/to/new/complex/directory', exist_ok=True)

        # Example: Remove an empty directory
        directory_to_remove = '/path/to/empty_directory'
        os.rmdir(directory_to_remove)

        # Example 8: Removing a file
        os.remove('/path/to/file.txt')

        # Example 9: Renaming a file or directory
        os.rename('/path/to/old_name.txt', '/path/to/new_name.txt')


    if mod == "Working_with_Directories":
        Working_with_Directories()
    elif mod == "Path_Manipulation":
        Path_Manipulation()
    elif mod == "File_and_Directory_Operations":
        File_and_Directory_Operations()
    else:
        print("Invalid choice")

# Call the function with the desired module name
# popular("Working_with_Directories")
        

# Environment_Variables()
import os

# Check if the VIRTUAL_ENV environment variable is set
# if 'VIRTUAL_ENV' in os.environ:
if 'virtual_env' in os.environ:
    virtual_env_path = os.environ['VIRTUAL_ENV']
    virtual_env_name = os.path.basename(virtual_env_path)
    print(f"Virtual Environment Name: {virtual_env_name}")
else:
    print("Not in a virtual environment.")
