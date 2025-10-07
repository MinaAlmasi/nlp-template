from pathlib import Path

def main():
    # get path of current file
    path = Path(__file__)
    print(f"\nThe path of the file is: '{path}'")

    # get data 
    data_path = path.parents[1] / "data" # go up two levels to the root directory
    print(f"The data path is: '{data_path}'")

    # load raw data
    with open(data_path / "raw_data.txt", "r") as f:
        raw_data = f.read()
    print(f"\nRaw data content: '{raw_data}'")


if __name__ == "__main__":
    main()