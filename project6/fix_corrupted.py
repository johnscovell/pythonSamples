from markov_model import MarkovModel
import stdio
import sys


# Entry point.
def main():
    k = int(sys.argv[1])
    corrupted = str(sys.argv[2])
    text = sys.stdin.read()
    mark = MarkovModel(text, k)
    stdio.writeln(mark.replace_unknown(corrupted))


if __name__ == '__main__':
    main()
