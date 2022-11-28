executar_jupyter:
	jupyter-notebook
instalar_dependencias_pacotes_pip:
	sudo apt-get install libspatialindex-dev -y
instalar_python3_e_dependencias:
	sudo apt-get update
	sudo apt-get install python3 python3-dev python3-venv python3-tk -y
criar_ambiente_virtualenv:
	python3 -m venv ambiente-dados1
	ambiente-dados1/bin/pip3 install --upgrade pip
	ambiente-dados1/bin/pip3 install -r requirements.txt
	clear
	echo "Pacotes instalados:"
	ambiente-dados1/bin/pip3 freeze
criar_repositorio_git_local:
	git init
	echo "*.pyc\nambiente-dados1/" > .gitignore
atualizar_ambiente_virtualenv:
	ambiente-dados1/bin/pip3 install --upgrade pip
	ambiente-dados1/bin/pip3 install -r requirements.txt
	clear
	echo "Pacotes instalados:"
	ambiente-dados1/bin/pip3 freeze
remover_ambiente_virtualenv:
	rm -r ambiente-dados1/
