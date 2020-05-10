#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python e PyQt5.

Acessando/interagindo com um arquivo ``*.ui`` (XML).
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from libraries import cripto

class MeuAplicativo:
    """Classe."""
    key_a_public, key_a_private, key_a_sprime, key_b_public, key_b_private, key_b_sprime = 0, 0, 0, 0, 0, 0
    a_2_b_txt, b_2_a_txt = "", ""
    state = False

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

        #btn

        self.push_button_dec = window.btn_dec
        self.push_button_key = window.btn_key

        self.push_button_email = window.btn_email
        self.push_button_git = window.btn_git
        
        # Conectando um método ao evento de clique do botão.
        self.push_button_dec.clicked.connect(self._on_button_clicked_dec)
        self.push_button_key.clicked.connect(self._on_button_clicked_key)
        self.push_button_email.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("mailto:freitas.eduardo@academico.ifpb.edu.br")))
        self.push_button_git.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/EduFreit4s/end-to-end-encryption")))

        self.push_button_a.clicked.connect(self._on_button_clicked_a)
        self.push_button_b.clicked.connect(self._on_button_clicked_b)

    """Gerador de chaves"""

    def keys(self):
        self.key_a_public, self.key_a_sprime, self.key_a_private = cripto.generator()
        self.key_b_public, self.key_b_sprime, self.key_b_private = cripto.generator()
        self.output()

    def empty_key(self):
        if (self.key_a_public or self.key_a_sprime or self.key_b_public  or self.key_b_sprime) == 0:
            self.keys()

    """Exibição hexa/decimal"""

    def output(self):
        if self.state:
            self.push_button_dec.setText("Decimal")
            if self.a_2_b_txt != "":
                self.a_up.setPlainText(self.a_2_b_txt)
            if self.b_2_a_txt != "":
                self.b_up.setPlainText(self.b_2_a_txt)
        else:
            self.push_button_dec.setText("Hexadecimal")
            if self.a_2_b_txt != "":
                self.a_up.setPlainText(hex(int(self.a_2_b_txt))[2:])
            if self.b_2_a_txt != "":
                self.b_up.setPlainText(hex(int(self.b_2_a_txt))[2:])

        if self.state:
            self.txt_a_public.setText(str(self.key_a_public))
            self.txt_a_private.setText(str(self.key_a_private))
            self.txt_a_sprime.setText(str(self.key_a_sprime))
            self.txt_b_public.setText(str(self.key_b_public))
            self.txt_b_private.setText(str(self.key_b_private))
            self.txt_b_sprime.setText(str(self.key_b_sprime))
        else:
            self.txt_a_public.setText(hex(self.key_a_public))
            self.txt_a_private.setText(hex(self.key_a_private))
            self.txt_a_sprime.setText(hex(self.key_a_sprime))
            self.txt_b_public.setText(hex(self.key_b_public))
            self.txt_b_private.setText(hex(self.key_b_private))
            self.txt_b_sprime.setText(hex(self.key_b_sprime))

    """Tradutor"""
    
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

    def _on_button_clicked_dec(self):                       #Alterna exibição de dados para hexadecimal ou inteiro
        self.state = not self.state
        self.output()     

    def _on_button_clicked_key(self):
        self.keys()

    def _on_button_clicked_a(self):
        if self.chat_a.text():
            self.empty_key()
            self.output()
            self.code(self.chat_a.text(), "A")              # Codifica texto digitado e envia para B
            self.output()                                   # Mostra texto codificado enviado 
            self.chat_a.clear()                             # Limpa o campo de digitação 
            self.decode("B")                                # Pede para B decodificar a mensagem
        
    def _on_button_clicked_b(self):
        if self.chat_b.text():
            self.empty_key()
            self.output()
            self.code(self.chat_b.text(), "B")              # Codifica texto digitado e envia para A
            self.output()                                   # Mostra texto codificado enviado
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
