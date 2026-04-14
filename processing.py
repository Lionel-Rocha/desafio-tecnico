import pandas
from logs import logger
"""
Vou comentar com sinceridade: se fosse um projeto grande,
eu separaria a responsabilidade de colocar os dados no dataframe
da de processá-los. Mas é um desafio relativamente pequeno, então,
eu vou colocar tudo em um lugar só para evitar over-engineering.
"""
def process_data(all_items):
    names = []
    prices = []
    discounted_prices = []

    for item in all_items:

        logger.info(f"Processando item {item['nome']}")

        item_price = float(item['preco'].replace('$', ''))
        item_name = item['nome']

        if item_price > 20:
            discount = item_price * 0.1
            discounted_price = round(item_price - discount, 2)
            names.append(item_name)
            prices.append(item_price)
            discounted_prices.append(discounted_price)

    logger.success("Dados processados com sucesso.")
    return [names, prices, discounted_prices]


def wraps_dataframe(names, prices, discounted_prices, output_file="produtos.xlsx"):
    try:
        dataframe = pandas.DataFrame({
            "Nome": names,
            "Preco": prices,
            "Preco com desconto": discounted_prices
        })

        # É bom garantir que o arquivo virá na extensão correta
        if not output_file.endswith('.xlsx'):
            output_file = output_file + '.xlsx'

        dataframe.to_excel(output_file, index=False)
        logger.success("Arquivo salvo!")
    except Exception as e:
        logger.error(f"Houve um erro no salvamento do arquivo: {e}")

def processing_main(all_items, output_file="produtos.xlsx"):
    try:
        [names, prices, discounted_prices] = process_data(all_items)
        wraps_dataframe(names, prices, discounted_prices, output_file)
    except Exception:
        logger.error("Houve um erro no processamento dos dados.")