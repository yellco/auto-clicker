
import os, sys
import argparse
from app.utils.env import load_env
from app.core.application import Application
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')


def parse_args():
	parser = argparse.ArgumentParser(description="Auto-clicker")
	parser.add_argument("-x", dest="x", required=False, type=int, help='Х координата')
	parser.add_argument("-y", dest="y", required=False, type=int, help='Y координата')
	parser.add_argument("-i", dest="interval", required=False, type=int, help='Интервал срабатываний')
	parser.add_argument("-c", dest="count_def", required=False, type=int, help='Количество срабатываний кликера')
	parser.add_argument("-s", dest="start", required=False, type=bool, help='Если true, то кликер сразу запускается')
	return parser.parse_args()


def main():
	"""
	Точка входа приложения
	"""
	env_vars = load_env(dotenv_path)
	args = parse_args()

	try:
		Application(
			env_vars,
			x_coord=args.x,
			y_coord=args.y,
			interval=args.interval,
			count_def=args.count_def,
			start=args.start
		).start_app()
	except KeyboardInterrupt:
		sys.exit()


if __name__ == "__main__":
	main()
