import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="excorpus",
        description="Exquisite Corpus command-line tool "
    )

    parser.add_argument(
        "command",
        help="Command to run (right now only 'head' is supported)"
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="Path to a corpus CSV file (optional for now)"
    )

    args = parser.parse_args()

    if args.command == "head":
        print("Pretend we are previewing the first few rows of:", args.file)
    else:
        print("Unknown command:", args.command)


if __name__ == "__main__":
    main()
