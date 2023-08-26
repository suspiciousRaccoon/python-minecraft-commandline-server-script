import subprocess

"""
Change SERVER_START_BAT to the location of a batch file that starts a minecraft server
Change SERVER_DIRECTORY to the directory in which the Server itself is
"""
SERVER_START_BAT = "C\\path\\to\\server\\start.bat"
SERVER_DIRECTORY = "C:\\path\\to\\server"


class Server:
    def __init__(self, server_start_bat: str, directory: str) -> None:
        self.server_start_bat = server_start_bat
        self.directory = directory
        self.server = None

    def start_server(self) -> None:
        self.server = subprocess.Popen(
            self.server_start_bat, cwd=self.directory, stdin=subprocess.PIPE, text=True)

    def stop_server(self) -> None:
        self.command('stop')
        self.server.communicate()

    def command(self, command: str) -> None:
        try:
            self.server.stdin.write(command+'\n')
            self.server.stdin.flush()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    server = Server(SERVER_START_BAT, SERVER_DIRECTORY)
    server_running = None
    while True:
        print(
            "\nPlease select an option:\n[1] Start Server\n[2] Execute Command\n[3] Stop Server\n[4] Exit Program")
        cmd = input().lower().strip()
        match cmd:
            case "1":
                if server_running:
                    print("Server is already running")
                else:
                    server.start_server()
                    server_running = True
            case "2":
                print("Please Insert Command:\n")
                cmd = input().lower().strip()
                if cmd == "stop":
                    server_running = False
                server.command(cmd)
            case "3":
                server.stop_server()
                server_running = False
            case "4":
                if server_running:
                    server.stop_server()
                break
