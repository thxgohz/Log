import logging
from app.infra.logConfig import Assinatura


def main():
    Assinatura()
    logger = logging.getLogger(__name__)

    logger.info("mensagem")
    logger.warning("aviso")
    logger.error("erro")


main()