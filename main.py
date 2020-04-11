#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python e PyQt5.

Acessando/interagindo com um arquivo ``*.ui`` (XML).
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi

from libraries import cripto

#key_a_public = 0, key_a_private = 0, key_a_sprime = 0, key_b_public = 0, key_b_private = 0,  key_b_sprime = 0

class MeuAplicativo:
    """Classe."""
    
    key_a_public, key_a_private, key_a_sprime, key_b_public, key_b_private, key_b_sprime = 0, 0, 0, 0, 0, 0
    a_2_b_txt, b_2_a_txt = "", ""

    def __init__(self, window):
        """Construtor"""
        
        # Chat A
        self.push_button_a = window.btn_a
        self.a_up = window.a_up
        self.a_down = window.a_down
        self.chat_a = window.a_chat

        self.txt_a_public = window.a_e
        self.txt_a_private = window.a_d
        self.txt_a_sprime = window.a_n


        # Chat B
        self.push_button_b = window.btn_b
        self.b_up = window.b_up
        self.b_down = window.b_down
        self.chat_b = window.b_chat

        self.txt_b_public = window.b_e
        self.txt_b_private = window.b_d
        self.txt_b_sprime = window.b_n
        
        # Conectando um método ao evento de clique do botão.
        self.push_button_a.clicked.connect(self._on_button_clicked_a)
        self.push_button_b.clicked.connect(self._on_button_clicked_b)


    """Gerador de chaves"""

    def keys(self):
        self.key_a_public, self.key_a_sprime, self.key_a_private = cripto.generator()
        self.txt_a_public.setText(str(self.key_a_public))
        self.txt_a_private.setText(str(self.key_a_private))
        self.txt_a_sprime.setText(str(self.key_a_sprime))

        self.key_b_public, self.key_b_sprime, self.key_b_private = cripto.generator()
        self.txt_b_public.setText(str(self.key_b_public))
        self.txt_b_private.setText(str(self.key_b_private))
        self.txt_b_sprime.setText(str(self.key_b_sprime))

    def code(self, txt, user):
        if user == "A":
            self.a_2_b_txt = cripto.lock(txt, self.key_b_public, self.key_b_sprime)
        elif user == "B":
            self.b_2_a_txt = cripto.lock(txt, self.key_a_public, self.key_a_sprime)

    def decode(self, user):
        if user == "A":
            self.a_down.setPlainText(cripto.unlock(self.b_2_a_txt, self.key_a_private, self.key_a_sprime))
        elif user == "B":
            self.b_down.setPlainText(cripto.unlock(self.a_2_b_txt, self.key_b_private, self.key_b_sprime))

    
    """Método é executado quando o botão é pressionado."""

    def _on_button_clicked_a(self):
        
        if (self.key_b_public and self.key_b_sprime) == 0:
            self.keys()

        if self.chat_a.text():
            self.code(self.chat_a.text(), "A")              # Codifica texto digitado e envia para B
            self.a_up.setPlainText(self.a_2_b_txt)          # Mostra texto codificado enviado
            self.chat_a.clear()                             # Limpa o campo de digitação 
            self.decode("B")                                # Pede para B decodificar a mensagem
        
    def _on_button_clicked_b(self):
        
        if (self.key_a_public and self.key_a_sprime) == 0:
            self.keys()

        if self.chat_b.text():
            self.code(self.chat_b.text(), "B")              # Codifica texto digitado e envia para A
            self.b_up.setPlainText(self.b_2_a_txt)          # Mostra texto codificado enviado
            self.chat_b.clear()                             # Limpa o campo de digitação 
            self.decode("A")                                # Pede para A decodificar a mensagem
        
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # Lendo o arquivo de interface.
    window = loadUi('forms/mainwindow.ui')
    ui = MeuAplicativo(window=window)
    window.show()
    sys.exit(app.exec_())
