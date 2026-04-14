# 0. FAZER LOGIN!!!
# 1. pegar o item do site
# Vamos separar "login" de "pegar os itens".

import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from logs import logger

load_dotenv()
TIMEOUT = 10000

class SauceDemoClient:
    def __init__(self, browser_type="chromium", headless=True):
        self.logado = False
        self.browser_type = browser_type
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None
        self.timeout = TIMEOUT

    def login(self, usuario=os.getenv("USUARIO"), senha=os.getenv("SENHA")):
        self.playwright = sync_playwright().start()
        self.browser = getattr(self.playwright, self.browser_type).launch(headless=self.headless)
        self.page = self.browser.new_page()

        self.page.goto(os.getenv("URL"))
        self.page.fill('[data-test="username"]', usuario)
        self.page.fill('[data-test="password"]', senha)

        self.page.click('[data-test="login-button"]')

        # Aguarda um pouco para a página reagir (mensagem de erro ou navegação).
        self.page.wait_for_timeout(3000)

        erro_element = self.page.query_selector('[data-test="error"]')
        if erro_element:
            mensagem_erro = erro_element.inner_text()
            logger.error(f"Falha no login: {mensagem_erro}")
            return False

        if "/inventory.html" in self.page.url:
            self.logado = True
            logger.success(f"Login realizado com sucesso como {usuario}")
            return True

        logger.error(f"Falha no login para '{usuario}' - motivo desconhecido")
        return False

    def get_all_items(self):
        if not self.logado:
            raise Exception("É necessário fazer login primeiro.")

        try:
            try:
                self.page.wait_for_selector('[data-test="inventory-item"]', timeout=10000)
            except Exception:
                logger.warning("Nenhum item encontrado no inventário")
                return []  # Se não tem itens, sai antes.

            itens = self.page.eval_on_selector_all(
                '[data-test="inventory-item"]',
                """elementos => elementos.map(el => ({
                    nome: el.querySelector('[data-test="inventory-item-name"]')?.innerText || '',
                    preco: el.querySelector('[data-test="inventory-item-price"]')?.innerText || ''
                }))"""
            )

            logger.info(f"{len(itens)} itens encontrados")
            return itens

        except Exception as e:
            logger.error(f"Erro ao extrair itens: {e}")
            return []

    def close_playwright(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        logger.success("Conexão fechada")


def crawler_main(headless=True):
    client = SauceDemoClient(headless=headless)
    client.login()
    all_items = client.get_all_items()
    client.close_playwright()
    return all_items
