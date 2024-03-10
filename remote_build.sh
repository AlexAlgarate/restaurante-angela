python -m pip install --upgrade pip
pip install -r requirements.txt
rm -fr public
isort restaurante_ostras_nin/
black restaurante_ostras_nin/
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
