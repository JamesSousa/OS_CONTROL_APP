# criar persistencia no docker
# docker run -p 5432:5432 -v C:\Users\james\Documents\postgres\:/var/lib/postgresql/data -e POSTGRES_PASSWORD=password -e POSTGRES_USER=admin postgres
#


# docker run --name postgres-docker -p 5432:5432 -e POSTGRES_PASSWORD=exemplo -d postgres
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
--name: é o nome que será  criado o container, conseguirá visualizar quando abrir o docker
-e: se refere as variáveis de ambiente
-p: incluindo qual a porta que irá executar o container
-d: significa que o container vai rodar em segundo plano, dessa forma pode usar o terminal/prompt para outros comandos
POSTGRES_PASSWORD: é um campo obrigatório para inicialização do postgre, com essa senha conseguirá acessar o banco de dados criado localmente
postgres: referência da imagem que será baixada
#
#

#VERSÃO DO dJANGO 5.2


#https://github.com/JamesSousa/OS_CONTROL_APP.git

#echo "# OS_CONTROL_APP" >> README.md
#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/JamesSousa/OS_CONTROL_APP.git
#git push -u origin main


#git remote add origin https://github.com/JamesSousa/OS_CONTROL_APP.git
#git branch -M main
#git push -u origin main