import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S", format="[%(asctime)s] [%(levelname)s] %(message)s")