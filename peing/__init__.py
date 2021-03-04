import argparse
from .PeingAPI import PeingAPI


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("URL")
    parser.add_argument("-f", "--format", default="json")
    parser.add_argument("-n", "--name")

    args = parser.parse_args()

    url = args.URL
    format = args.format
    save_name = args.name

    screen_name = url.split("/")[-1]

    png = PeingAPI(screen_name)
    item = png.get_item()

    if save_name is None:
        save_name = screen_name

    if format == "csv":
        png.save_csv(item, save_name)
    else:
        png.save_json(item, save_name)


if __name__ == "__main__":
    main()