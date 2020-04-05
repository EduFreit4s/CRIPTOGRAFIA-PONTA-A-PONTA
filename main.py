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
        # Widgets
        self.label = window.txt
        self.push_button = window.btn
        # Conectando um método ao evento de clique do botão.
        self.push_button.clicked.connect(self._on_button_clicked)

    def _on_button_clicked(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
        self.label.setText('olá mundo')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # Lendo o arquivo de interface.
    window = loadUi('forms/mainwindow.ui')
    ui = MeuAplicativo(window=window)
    window.show()
    sys.exit(app.exec_())
