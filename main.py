
import os
from app.utils.env import load_env
from app.core.application import Application
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

def main():
	env_vars = load_env(dotenv_path)

	Application(env_vars).start()

if __name__ == "__main__":
	main()
