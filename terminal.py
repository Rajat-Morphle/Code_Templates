import subprocess

def fetch_UUID():
    # Define the command you want to run

    username = os.getenv("USERNAME")
    query_command = ("python3 /home/" + username + "/PicoControl/bootloader/flash_can.py -i can0 -q")

    # Run the command and capture the output
    process = subprocess.Popen(query_command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    # Decode the byte output to string
    output_str = output.decode("utf-8")

    # Print the captured output
    print(output_str)

    keywords = output_str.split(" ")

    for i in range(len(keywords)):
        if keywords[i] == "Katapult\nQuery":
            # print("**************** Katapult's index is: " + str(i) + "***************************")
            UUID = str(keywords[i-2].split(",")[0])

    return UUID