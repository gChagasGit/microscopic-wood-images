# Base de Dados com Imagens Microscópicas de Madeira

Este repositório tem como objetivo criar um script automatizado para realizar o download de imagens microscópicas de seção transversal de madeira do portal [InsideWood](https://insidewood.lib.ncsu.edu/search?0). As imagens coletadas servirão para estudos detalhados sobre a anatomia da madeira, com ênfase na identificação e análise de vasos.

## Objetivo

Automatizar o download de imagens microscópicas de madeira para criar uma base de dados robusta e facilitar o estudo dos vasos da madeira. Esses estudos são cruciais para compreender as propriedades anatômicas, físicas e mecânicas da madeira, com aplicações em diversas áreas, como construção civil, fabricação de móveis e pesquisa botânica.

## Fontes das Imagens

As imagens utilizadas são provenientes do portal InsideWood, uma ampla base de dados que disponibiliza informações sobre a anatomia da madeira de diversas espécies. Você pode explorar o portal e acessar as imagens através do link [InsideWood](https://insidewood.lib.ncsu.edu/search?0).

## Citação

Se você usar ou fizer referência a este conjunto de dados em seu trabalho, por favor, cite o InsideWood e os seguintes artigos:

- InsideWood. 2004-onwards. Publicado na Internet. [http://insidewood.lib.ncsu.edu/search](http://insidewood.lib.ncsu.edu/search) [data de acesso].

- Wheeler, E.A. 2011. InsideWood – A Web Resource For Hardwood Identification. IAWA Journal 32(2): 199-211. [PDF](https://www.jstor.org/stable/10.5555/iawa.32.2.199)

- Wheeler, E.A., P.E. Gasson, & P. Baas. 2020. Using The InsideWood Web Site: Potentials And Pitfalls. IAWA Journal 41(4): 412-462. [PDF](https://www.jstor.org/stable/10.5555/iawa.41.4.412)

> **Nota**: Ao usar as imagens ou dados do InsideWood, sempre dê crédito à instituição que forneceu as imagens. O uso comercial ou redistribuição sem permissão por escrito é estritamente proibido.

## Licença

Livre para fins educacionais e de pesquisa. Consulte os termos de uso do InsideWood para mais detalhes.

<!-- ## Estrutura do Repositório

O repositório está organizado da seguinte forma:

- **data/**: Contém as imagens baixadas ou links para elas.
- **scripts/**: Scripts para automatizar o download e processamento das imagens.
- **selenium_env/**: Ambiente configurado para o uso do Selenium. -->

## Como Usar o Script

### Requisitos

- Python 3.x
- Selenium
- Chrome WebDriver

### Instalação

1. Clone este repositório para seu ambiente local:

    ```bash
    git clone https://github.com/gChagasGit/microscopic-wood-images.git
    ```

2. Instale as dependências:

    ```bash
    pip install -r dependencies.txt
    ```

3. Baixe o Chrome WebDriver compatível com sua versão do navegador Chrome. Você pode encontrar o WebDriver [aqui](https://sites.google.com/a/chromium.org/chromedriver/).

### Executando o Script

- Execute o script principal para iniciar o download:

    ```bash
    python script_download.py
    ```

O script irá acessar o portal InsideWood, realizar buscas conforme os parâmetros definidos e baixar as imagens.

## Links Úteis

- [InsideWood](https://insidewood.lib.ncsu.edu/search?0): Portal com imagens e dados sobre anatomia da madeira.
- [Guia de uso do Selenium](https://selenium-python.readthedocs.io/): Documentação oficial do Selenium para Python.

## Contribuições

Contribuições para melhorar os scripts ou o processo de coleta são bem-vindas. Para contribuir:

1. Fork o repositório.
2. Crie uma branch para sua modificação (`git checkout -b feature/nova-funcionalidade`).
3. Faça o commit das alterações (`git commit -am 'Adicionando nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.


