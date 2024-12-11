import requests
import pathlib

def parse_args(kwargs: dict) -> str:
    return kwargs.get("day")

class Downloader:
    save_path = ""
    def __init__(self, save_path: str = "./data" ) -> None:
        self.save_path = save_path
        pathlib.Path(self.save_path).mkdir(parents=True, exist_ok=True)
        

    def download_input_for_day(self, day: str) -> None:
        url = f"https://adventofcode.com/2024/day/{day}/input"
        file_name = f"{self.save_path}/day_{day}_input.txt"
        print(f"Saving location: {self.save_path}, to file: {file_name}")
        with requests.get(url) as data:
            with open(file_name, 'w') as f:
                f.write(data.text)
        return file_name
    
