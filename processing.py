import pandas
from logs import logger
"""
Vou comentar com sinceridade: se fosse um projeto grande,
eu separaria a responsabilidade de colocar os dados no dataframe
da de processá-los. Mas é um desafio relativamente pequeno, então,
eu vou colocar tudo em um lugar só para evitar over-engineering.
"""
def process_data(all_items):
    nomes = []
    precos = []
    precos_com_desconto = []

    for item in all_items:
        item_price = float(item['preco'].replace('$', ''))
        item_name = item['nome']

        if item_price >= 20:
            discount = item_price * 0.1
            discounted_price = round(item_price - discount, 2)
        else:
            discounted_price = None

        nomes.append(item_name)
        precos.append(item_price)
        precos_com_desconto.append(discounted_price)

    logger.success("Dados processados com sucesso.")
    return [nomes, precos, precos_com_desconto]


def wraps_dataframe(nomes, precos, precos_com_desconto):
    try:
        dataframe = pandas.DataFrame({
            "Nome": nomes,
            "Preco": precos,
            "Preco com desconto": precos_com_desconto
        })

        dataframe.to_excel("arquivo.xlsx", index=False)
        logger.success("Arquivo salvo!")
    except Exception as e:
        logger.error("Houve um erro no salvamento do arquivo: ", e)

def processing_main(all_items):
    try:
        [names, prices, discounted_prices] = process_data(all_items)
        wraps_dataframe(names, prices, discounted_prices)
    except Exception:
        logger.error("Houve um erro no processamento dos dados.")