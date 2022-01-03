import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../../")
sys.path.append(topdir)
from main import app
from src.services.Wscatgeo import searchStateByName

def test_searchStateByName():
    result = searchStateByName('Zacatecas')
    assert result == str(32)

def test_searchStateByName_accent():
    result = searchStateByName('Yucatán')
    assert result == str(31)

def test_searchStateByName_space():
    result = searchStateByName('Baja California')
    assert result == '02'

def test_searchStateByName_noCaseSensitive():
    result = searchStateByName('CoLiMa')
    assert result == '06'
