import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# 0. FAZER LOGIN!!!
# 1. pegar o item do site
# Vamos separar "login" de "pegar os itens".


class SauceDemoClient:
    load_dotenv()

    def __init__(self, browser_type="chromium", headless=True):
        self.logado = None
        self.browser_type = browser_type
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None

    def login(self, usuario=os.getenv("USUARIO"), senha=os.getenv("SENHA")):
        self.playwright = sync_playwright().start()
        self.browser = getattr(self.playwright, self.browser_type).launch(headless=self.headless)
        self.page = self.browser.new_page()

        self.page.goto("https://www.saucedemo.com/")
        self.page.fill('[data-test="username"]', usuario)
        self.page.fill('[data-test="password"]', senha)
        self.page.click('[data-test="login-button"]')

        try:
            self.page.wait_for_selector('[data-test="inventory-item"]', timeout=5000)
            self.logado = True
            # TODO: Vai para LOG
            print(f"Login realizado com sucesso como {usuario}")
            return True
        except Exception as e:
            # TODO: Vai para LOG
            print(f"Falha no login. Detalhes: {e}")
            return False

    def get_all_items(self):
        # Pelo bem do andamento do fluxo, vou adicionar esse self.logado aqui.
        if not self.logado:
            raise Exception("É necessário fazer login primeiro.")

        itens = self.page.eval_on_selector_all('[data-test="inventory-item"]',
                                               """elementos => elementos.map(el => ({
                                                   nome: el.querySelector('[data-test="inventory-item-name"]')?.innerText || '',
                                                   preco: el.querySelector('[data-test="inventory-item-price"]')?.innerText || '',
                                                   descricao: el.querySelector('[data-test="inventory-item-desc"]')?.innerText || '',
                                                   botao: el.querySelector('button')?.innerText || ''
                                               }))"""
                                               )

        # TODO: Itens vão para LOG
        print(f"{len(itens)} itens encontrados")
        return itens

    def close_playwright(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        # TODO: colocar isso em logs
        print("Conexão fechada")


def crawler_main():
    client = SauceDemoClient(headless=True)
    client.login()
    all_items = client.get_all_items()
    client.close_playwright()
    return all_items
