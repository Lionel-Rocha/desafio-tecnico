> [!WARNING]
> Só produtos acima de $20 entram na lista (e ganham 10% de desconto)

## Como usar

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar o ambiente
Crie um arquivo .env na raiz do projeto:

```env
USUARIO=tipo_de_usuario
SENHA=secret_sauce
URL=https://www.saucedemo.com/
```
#### Tipos de usuário

standard_user: Usuário OK

locked_out_user: Usuário com problema (tratamento OK)

problem_user: Todas as imagens são de cães

performance_glitch_user: Demora uns segundos antes de entrar (tratamento OK)

error_user: Não descobri

visual_user: Os preços mudam a cada refresh de página

### 3. Executar

```python main.py``` >	Executa normalmente (com navegador visível)

```python main.py --headless``` >   Executa em segundo plano (sem janela)

```python main.py --output meu_arquivo.xlsx``` >	Salva com outro nome

```python main.py --headless --output relatorio``` >   Todas as anteriores. O arquivo vai salvar com uma extensão .xlsx 

