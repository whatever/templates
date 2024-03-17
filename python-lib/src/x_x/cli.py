import argparse


from x_x import splash, x_x


def main():
    """CLI stub"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--splash", action="store_true", help="show splash screen")
    args = parser.parse_args()

    if args.splash:
        print(splash("sword"))
    else:
        print(x_x())
