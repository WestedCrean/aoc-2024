from downloader import Downloader, parse_args
import argparse



def main(**kwargs) -> None:
    parser = argparse.ArgumentParser("aoc-downloader")
    parser.add_argument("--day", help="An integer representing which day to download", type=int, required=True)
    args = parser.parse_args()
    print(f"Downloading input data for day {args.day}...")
    Downloader(save_path=f"../aoc-{args.day}/data").download_input_for_day(day=args.day)
    print("Done!")


if __name__ == "__main__":
    main()