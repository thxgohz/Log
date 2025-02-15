import logging
import os
from datetime import datetime
from art import text2art
import app.local_settings as local_settings

log_base_path = local_settings.log_path

year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%B')

log_dir = os.path.join(log_base_path, year, month)
os.makedirs(log_dir, exist_ok=True)

log_filename = os.path.join(log_dir, f"log_Usuarios_LastLogon_{datetime.now().strftime('%d-%m-%Y')}.log")

ascii_art = text2art("t h x g o h z", font='Standard')
developer_info = """Autor: Thiago Inacio\n"""

with open(log_filename, "w", encoding="utf-8") as file:
    file.write(ascii_art + developer_info + "\n")

print(ascii_art)
print(developer_info)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, delay=False),
        logging.StreamHandler()
    ]
)

for handler in logging.root.handlers:
    if isinstance(handler, logging.FileHandler):
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y'))
    elif isinstance(handler, logging.StreamHandler):
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y'))


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def Assinatura():
    pass