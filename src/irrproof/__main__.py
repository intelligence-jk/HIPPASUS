import sys
from .core import prove


def main(argv=None):
    a = sys.argv[1:] if argv is None else argv
    try:
        n = int(a[0])
        print("\n".join(f"{i}. {s}" for i, s in enumerate(prove(n), 1)))
        return 0
    except (IndexError, ValueError) as e:
        print("error:", e if a else "give n, for example: python -m irrproof 12")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
