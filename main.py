
# el = new Element()
import os
from app.utils.env import load_env
from app.core.element import *
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

def main():
	env_vars = load_env(dotenv_path)

	el = Element(env_vars)
	el.start()

if __name__ == "__main__":
    main()

# window = sg.Window('Авто-кликер', layout)