"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.secret_key = 'une_cle_secrete_bien_longue_et_unique'

import CEHv13_Prep.views
