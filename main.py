import crawler


def main():
    # 0. FAZER LOGIN!!!
    # 1. pegar o item do site
    # 2. verificar se está acima de 20 dol -> sim? aplicar_desconto()
    # 3. colocar o item no dataframe
    # 4. após todos os itens serem processados, colocar o dataframe pra xlsx
    print("Comando iniciado.")
    all_items = crawler.crawler_main()
    print("Comando finalizado.")


main()
