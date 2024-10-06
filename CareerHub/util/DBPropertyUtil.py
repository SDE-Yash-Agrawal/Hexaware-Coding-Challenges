class DBPropertyUtil:
    @staticmethod
    def get_connection_string(file_name):
        try:
            with open(file_name, 'r') as file:
                connection_string = file.read().strip()
                return connection_string
        except FileNotFoundError:
            print(f"Properties file '{file_name}' not found.")
            raise
        except Exception as e:
            print(f"Error reading properties file: {str(e)}")
            raise
