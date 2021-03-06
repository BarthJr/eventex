# EVENTEX

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/BarthJr/eventex.svg?branch=master)](https://travis-ci.org/BarthJr/eventex)
[![Updates](https://pyup.io/repos/github/BarthJr/eventex/shield.svg)](https://pyup.io/repos/github/BarthJr/eventex/)


## Como desenvolver?
1. Clone o repositório
2. Instale o pipenv
3. Instale as dependências
4. Configure a instância com o .env
5. Execute os testes.

``` console
git clone git@github.com:barthjr/eventex.git wttd
cd wttd
pip install pipenv
pipenv install -d
cp contrib/env-sample .env
pipenv run python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```
