from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
# from kivy.core.window import Window

from urllib.request import urlopen
from bs4 import BeautifulSoup
import unidecode

# Window.size = (450, 600)


class JanelaGerenciadora(ScreenManager):
    ...


class JanelaPrincipal(MDScreen):
    ...


class Janela1(MDScreen):
    def scraping(self):
        url = urlopen('http://www.geradordepessoas.com.br/gerador-de-pessoas?sexo=masculino&formatacao=sim')
        soup = BeautifulSoup(url.read(), "html.parser")
        data_list = []
        list_tag = soup.find_all('input')
        for data in list_tag:
            # unidecode.unidecode(x) tira os acentos.
            data_list.append(unidecode.unidecode(data.get('value')))

        self.ids.nome.text = f'{data_list[5]}'
        self.ids.cpf.text = f'{data_list[6]}'
        self.ids.rg.text = f'{data_list[7]}'
        self.ids.data.text = f'{data_list[8]}'
        self.ids.cep.text = f'{data_list[11]}'
        self.ids.rua.text = f'{data_list[12]}'
        self.ids.num.text = f'{data_list[13]}'
        self.ids.bairro.text = f'{data_list[14]}'
        self.ids.cidade.text = f'{data_list[15]}'
        self.ids.estado.text = f'{data_list[16]}'
        self.ids.fixo.text = f'{data_list[17]}'
        self.ids.celular.text = f'{data_list[18]}'
        self.ids.mail.text = f'{data_list[9]}'


class Janela2(MDScreen):
    def scraping(self):
        url = urlopen('http://www.geradordepessoas.com.br/gerador-de-pessoas?sexo=feminino&formatacao=sim')
        soup = BeautifulSoup(url.read(), "html.parser")
        data_list = []
        list_tag = soup.find_all('input')
        for data in list_tag:
            # unidecode.unidecode(x) tira os acentos.
            data_list.append(unidecode.unidecode(data.get('value')))

        self.ids.nome.text = f'{data_list[5]}'
        self.ids.cpf.text = f'{data_list[6]}'
        self.ids.rg.text = f'{data_list[7]}'
        self.ids.data.text = f'{data_list[8]}'
        self.ids.cep.text = f'{data_list[11]}'
        self.ids.rua.text = f'{data_list[12]}'
        self.ids.num.text = f'{data_list[13]}'
        self.ids.bairro.text = f'{data_list[14]}'
        self.ids.cidade.text = f'{data_list[15]}'
        self.ids.estado.text = f'{data_list[16]}'
        self.ids.fixo.text = f'{data_list[17]}'
        self.ids.celular.text = f'{data_list[18]}'
        self.ids.mail.text = f'{data_list[9]}'


class MeuApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '700'
        self.title = "Generate-People"
        return Builder.load_file('main.kv')

    def fechar(self):
        self.stop()


MeuApp().run()
