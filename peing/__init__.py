import argparse
from .PeingAPI import PeingAPI


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("URL")
    parser.add_argument("-f", "--format")

    args = parser.parse_args()

    url = args.URL
    format = args.format

    screen_name = url.split("/")[-1]

    png = PeingAPI(screen_name)
    item = png.get_item()

    png.save_json(item, screen_name)


if __name__ == "__main__":
    main()