#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python e PyQt5.

Acessando/interagindo com um arquivo ``*.ui`` (XML).
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi

from libraries import cripto

class MeuAplicativo:
    """Classe."""

    def __init__(self, window):
        """Construtor."""
        # Chat A
        self.push_button_a = window.btn_a
        self.a_up = window.a_up
        self.a_down = window.a_down
        self.chat_a = window.a_chat
        # Chat B
        self.push_button_b = window.btn_b
        self.b_up = window.b_up
        self.b_down = window.b_down
        self.chat_b = window.b_chat

        # Conectando um método ao evento de clique do botão.
        self.push_button_a.clicked.connect(self._on_button_clicked_a)
        self.push_button_b.clicked.connect(self._on_button_clicked_b)

    def _on_button_clicked_a(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
        text_a = self.chat_a.text()
        if text_a:
            self.b_down.setText(text_a)
            self.a_up.setText(text_a)
            self.chat_a.clear()
    
    def _on_button_clicked_b(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
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
