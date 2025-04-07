from main import app, db

with app.app_context():
    if  db.create_all():
        print(".Tabelas criadas com sucesso!")
    else:
        print(".Erro ao criar tabelas.")