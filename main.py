#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python e PyQt5.

Acessando/interagindo com um arquivo ``*.ui`` (XML).
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi

from libraries import cripto

global key_a_public, key_a_private, key_a_sprime, key_b_public, key_b_private, key_b_sprime

class MeuAplicativo:
    """Classe."""
    
    

    def __init__(self, window):
        """Construtor."""

       # key_a_public, key_a_private, key_a_sprime, key_b_public, key_b_private, key_b_sprime

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


    def _on_button_clicked_a(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
        key_a_public, key_a_sprime, key_a_private = cripto.generator()

        self.txt_a_public.setText(str(key_a_public))
        self.txt_a_private.setText(str(key_a_private))
        self.txt_a_sprime.setText(str(key_a_sprime))

        text_a = self.chat_a.text()
        if text_a:
            self.b_down.setText(text_a)

           # txt = cripto.lock(text_a, key_a_public, key_a_sprime)
            self.a_up.setText(text_a)
            self.chat_a.clear()
    
    def _on_button_clicked_b(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
        key_b_public, key_b_sprime, key_b_private = cripto.generator()

        self.txt_b_public.setText(str(key_b_public))
        self.txt_b_private.setText(str(key_b_private))
        self.txt_b_sprime.setText(str(key_b_sprime))

        text_b = self.chat_b.text()
        if text_b:
            self.a_down.setText(text_b)
            self.b_up.setText(text_b)
            self.chat_b.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # Lendo o arquivo de interface.
    window = loadUi('forms/mainwindow.ui')
    ui = MeuAplicativo(window=window)
    window.show()
    sys.exit(app.exec_())
