import argparse
import crawler
import processing
from logs import logger


def main():
    parser = argparse.ArgumentParser(
        description='SauceDemo Web Scraper',
        epilog='Exemplos:\n  python main.py\n  python main.py --headless\n  python main.py --output meus_produtos.xlsx'
    )

    parser.add_argument(
        '--headless',
        action='store_true',
        help='Executar sem interface gráfica do Chromium'
    )

    parser.add_argument(
        '--output', '-o',
        default='produtos.xlsx',
        help='Nome do arquivo de saída (nome padrão: produtos.xlsx)'
    )

    args = parser.parse_args()

    try:
        logger.info("Comando iniciado")

        logger.info(f"Configurações: Headless={args.headless}, Output={args.output}")

        all_items = crawler.crawler_main(headless=args.headless)
        processing.processing_main(all_items, output_file=args.output)

        logger.success("Comando finalizado com sucesso!")


    except Exception as e:
        logger.error(f"Comando não finalizado. Erro: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())