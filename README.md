# Base de Dados com Imagens Microscópicas de Madeira

Este repositório contém um conjunto de imagens microscópicas de madeira, com o objetivo de estudar os vasos da madeira, uma característica fundamental na anatomia da madeira. Essas imagens são provenientes do site [InsideWood](https://insidewood.lib.ncsu.edu/search?0), que oferece uma ampla coleção de dados sobre anatomia da madeira de diferentes espécies.

## Objetivo

O objetivo deste projeto é criar uma base de dados com imagens microscópicas que permitirá o estudo detalhado dos vasos da madeira. O estudo da anatomia da madeira é crucial para a compreensão de suas propriedades físicas e mecânicas, o que pode ser aplicado em diversas áreas, como construção, móveis, e pesquisa botânica.

## Fontes das Imagens

As imagens utilizadas neste repositório foram coletadas a partir do portal InsideWood, que fornece dados sobre anatomia da madeira. Você pode explorar mais sobre essas imagens e os dados relacionados através do site [InsideWood](https://insidewood.lib.ncsu.edu/search?0).

## Citação

Se você usar ou fizer referência a este conjunto de dados em seu trabalho, por favor, cite o InsideWood e os seguintes artigos:

- InsideWood. 2004-onwards. Publicado na Internet. [http://insidewood.lib.ncsu.edu/search](http://insidewood.lib.ncsu.edu/search) [data de acesso].
  
- Wheeler, E.A. 2011. InsideWood – A Web Resource For Hardwood Identification. IAWA Journal 32(2): 199-211. [PDF](https://www.jstor.org/stable/10.5555/iawa.32.2.199)

- Wheeler, E.A., P.E. Gasson, & P. Baas. 2020. Using The InsideWood Web Site: Potentials And Pitfalls. IAWA Journal 41(4): 412-462. [PDF](https://www.jstor.org/stable/10.5555/iawa.41.4.412)

> **Nota**: Ao usar as imagens ou dados do InsideWood, sempre dê crédito à instituição que forneceu as imagens. O uso comercial ou redistribuição sem permissão por escrito é estritamente proibido.

## Licença

Livre

## Estrutura do Repositório

O repositório contém os seguintes diretórios:

- **Data/**: Imagens microscópicas (ou link para elas).
- **Script/**: Contém os scripts utilizados para processar as imagens e preparar os dados para estudo.
- **selenium_env/**: Ambiente de execução do Selenium para automatizar o download das imagens.

## Como Usar

### Requisitos

- Python 3.x
- Selenium
- Chrome WebDriver

### Instalação

1. Clone este repositório para seu ambiente local:

    ```bash
    git clone https://github.com/gChagasGit/microscopic-wood-images.git
    ```

2. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

3. Baixe o Chrome WebDriver adequado para sua versão do Chrome. O WebDriver pode ser encontrado [aqui](https://sites.google.com/a/chromium.org/chromedriver/).

### Executando os Scripts

Para rodar os scripts que processam as imagens, basta executar:

```bash
python script_dowload.py
```

Esse comando irá baixar e processar as imagens conforme a lógica definida no código.

## Links Úteis

- [InsideWood](https://insidewood.lib.ncsu.edu/search?0): Portal principal de dados sobre anatomia da madeira.
- [Calendário de 2025 "Plants With A Past"](https://www.insidewood.lib.ncsu.edu/)

## Contribuições

Contribuições para melhorar a base de dados ou o processo de estudo são bem-vindas. Para contribuir:

1. Fork o repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/MinhaNovaFeature`).
3. Faça o commit das suas mudanças (`git commit -am 'Adicionando nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/MinhaNovaFeature`).
5. Abra um Pull Request.

## Agradecimentos

Gostaríamos de agradecer aos curadores do InsideWood e a todas as instituições que forneceram os dados para este estudo.

---

Se tiver alguma dúvida ou precisar de mais informações, sinta-se à vontade para abrir uma issue ou enviar um e-mail para o curador do InsideWood: elisabeth_wheeler@NCSU.edu.
