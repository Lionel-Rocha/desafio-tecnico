import crawler
import processing
from logs import logger
def main():
    try:
        logger.info("Comando iniciado.")
        all_items = crawler.crawler_main()
        processing.processing_main(all_items)
        logger.info("Comando finalizado.")
    except Exception:
        logger.error("Comando não finalizado.")

main()
