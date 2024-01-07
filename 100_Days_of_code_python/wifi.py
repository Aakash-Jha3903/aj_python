
def one():
    import os

    # Run the command to list Wi-Fi profiles and their passwords
    os.system('netsh wlan show profiles')

    # Replace 'Your_WiFi_Name' with the actual Wi-Fi profile name
    wifi_name = 'ABESIT (2.4 G)'
    os.system(f'netsh wlan show profile name="{wifi_name}" key=clear')

def all():
    import os

    # Run the command to list all Wi-Fi profiles
    wifi_profiles = os.popen('netsh wlan show profiles').read()

    # Extract Wi-Fi profile names
    profile_names = [line.split(":")[1].strip() for line in wifi_profiles.splitlines() if "All User Profile" in line]

    # Iterate through profiles and retrieve passwords
    for profile_name in profile_names:
        password_info = os.popen(f'netsh wlan show profile name="{profile_name}" key=clear').read()
        print(f"\nWi-Fi Profile: {profile_name}")
        print(password_info)




# import subprocess
# def run_command(command):
#     result = subprocess.run(command, capture_output=True, text=True, shell=True)
#     return result.stdout.strip()

# # Get the list of all Wi-Fi profiles
# wifi_profiles_command = 'netsh wlan show profiles'
# wifi_profiles_output = run_command(wifi_profiles_command)

# # Extract the names of all Wi-Fi profiles
# wifi_names = [line.split(":")[1].strip() for line in wifi_profiles_output.splitlines() if "All User Profile" in line]

# # Get the Wi-Fi passwords for all profiles
# for wifi_name in wifi_names:
#     wifi_password_command = f'netsh wlan show profile name="{wifi_name}" key=clear'
#     wifi_password_output = run_command(wifi_password_command)
    
#     print(f"Wi-Fi Network: {wifi_name}")
#     print(f"Password: {wifi_password_output}\n")
all()