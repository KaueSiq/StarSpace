import sys
from cx_Freeze import setup, Executable
import pygame

base = None
if sys.platform == "win32":
    base = "Win32GUI"

Executables=[
    Executable("main.py",base= base)
]

buildOptions=dict(
    packages=[],
    includes=["pygame"],
    include_files=["fundo.jpg","fundo3.jpg","shark_Nebula.jpg","space.ico","space.png","interstellar.mp3"],
    excludes=[]
)
setup(
    name="Space",
    version="1.0",
    description="joguinho do espaço",
    options=dict(build_exe=buildOptions),
    executables=Executables
)