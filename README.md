# Python-minecraft-commandline-server-script
This is a simple python script made to manage a minecraft server from the command-line.

## Requirements
- Python 3.10+
- A [minecraft server](https://www.minecraft.net/en-us/download/server)
- A batch file to start the server. More info [here](https://minecraft.fandom.com/wiki/Tutorials/Setting_up_a_server#Configuring_the_environment)

## Installation
Clone the repository or download main.py
```bash
git clone https://github.com/suspiciousRaccoon/python-minecraft-commandline-server-script.git
```

## Usage
1. Modify the following constants at the beginning of the script to match your setup:

    ```python
    SERVER_START_BAT = "C:\\path\\to\\your\\start.bat"
    SERVER_DIRECTORY = "C:\\path\\to\\your\\server\\directory"
    ```
    
2. Open a command prompt and navigate to the directory containing `main.py`.

3. Run the script using the following command:

    ```bash
    python main.py
    ```

4. The script will present you with a menu of options:

    - `[1] Start Server`: Starts the Minecraft server if it's not already running.
    - `[2] Execute Command`: Allows you to send commands to the server. 
    - `[3] Stop Server`: Stops the running Minecraft server.
    - `[4] Exit Program`: Stops the server (if running) and exits the script.

## License

This project is licensed under the [MIT License](LICENSE).
