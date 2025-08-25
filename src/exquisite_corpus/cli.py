import argparse
from .corpus import load_corpus


def main(argv=None):
    """
    Entry point for the Exquisite Corpus command-line (CLI) tool.

    - Uses argparse to define commands (e.g., 'corpus', 'skeleton')
      and subcommands (e.g., 'head').
    - The parsed arguments are stored in the 'args' object.
    """
    # Create the top-level parser for the CLI program
    parser = argparse.ArgumentParser(
        prog="excorpus",  # This is the command name users will type
        description="Exquisite Corpus command-line tool"
    )

    # Add support for subcommands under the top-level command
    subparsers = parser.add_subparsers(
        dest="top_level_command",  # argparse will store the choice here
        required=True              # argparse will require a subcommand
    )

    # Define the corpus command group
    parser_corpus = subparsers.add_parser(
        "corpus",  # Name of this top-level command
        help="Work with corpora (preview, stats, etc.)"
    )

    # Add subcommands under "corpus"
    corpus_subparsers = parser_corpus.add_subparsers(
        dest="corpus_subcommand",  # argparse will store the choice here
        required=True
    )

    # Define the "corpus head" subcommand
    parser_corpus_head = corpus_subparsers.add_parser(
        "head",  # Subcommand name under "corpus"
        help="Show the first N rows of a corpus CSV (file preview)"
    )

    # Add arguments for "corpus head"
    parser_corpus_head.add_argument(
        "path",  # Positional argument
        help="Path to a corpus CSV file"
    )

    parser_corpus_head.add_argument(
        "--rows",              # Optional argument with a flag
        type=int,              # Must be an integer
        default=5,             # Default value if user does not supply it
        help="Number of rows to show (default: 5)"
    )

    # Parse the arguments from the command line (or from 'argv' for testing)
    args = parser.parse_args(argv)

    # Act on the chosen command and subcommand
    if args.top_level_command == "corpus":
        if args.corpus_subcommand == "head":
            # Load the corpus CSV into a DataFrame
            df = load_corpus(args.path)

            # Print the first N rows (N comes from --rows or defaults to 5)
            # Convert the rows to a list of dictionaries so the output is
            # human-readable in the terminal and easy to test in CI
            print(df.head(args.rows).to_dict(orient="records"))
            return

    # If we ever get here, it means no command matched.
    # Show the help message instead of crashing.
    parser.print_help()


if __name__ == "__main__":
    main()
