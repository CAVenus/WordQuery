#-*- coding:utf-8 -*-
import wquery
from anki.hooks import addHook

wquery.context.update_all = False


def start_here():
    wquery.read_parameters()
    if not wquery.have_setup:
        wquery.setup_options_menu()
        wquery.customize_addcards()
        wquery.setup_browser_menu()
        wquery.setup_context_menu()

addHook("profileLoaded", start_here)
