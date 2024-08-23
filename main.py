candidatos = {
    1: {"nome": "Abias Corpus Da Silva", "partido": "Partido MDB", "vice": "Benvindo Viola", "cargos": ["Vereador", "Deputado Estadual"], "idade": 157},
    2: {"nome": "Colapso Cardíaco da Silva", "partido": "Partido PDT", "vice": "Jacinto Leite Aquino Rêgo", "cargos": ["Secretária de Saúde"], "idade": 171},
    3: {"nome": "José Catarrinho", "partido": "Partido PSB", "vice": "Juvenalda Datia Gulosa", "cargos": ["Prefeito de Cidade A", "Senador"], "idade": 155},
    4: {"nome": "Paula Tejando", "partido": "Partido PCdoB", "vice": "Dayde Costa", "cargos": ["Deputado Federal"], "idade": 69},
    5: {"nome": "Liz Foley", "partido": "Partido PSDB", "vice": "Tomas Leite", "cargos": ["Ministro da Justiça"], "idade": 244},
    6: {"nome": "Pati Farias", "partido": "Partido PV", "vice": "Igor Dinho", "cargos": ["Diretora de Educação"], "idade": 69},
    7: {"nome": "Luiz Inácio Lula da Silva", "partido": "Partido PT", "vice": "Marcos Lula ", "cargos": ["Vereador", "Secretário de Obras"], "idade": 13},
    8: {"nome": "Jair Messias Bolsonaro", "partido": "Partido DeTras", "vice": "Guilherme Fernandes", "cargos": ["Deputado Federal", "Prefeito de Cidade B"], "idade": 22},
    9: {"nome": "Fernando Gomes", "partido": "Partido DaFrente", "vice": "Isabela Costa", "cargos": ["Secretário de Saúde", "Deputado Estadual"], "idade": 133},
    10: {"nome": "Patrícia Lima", "partido": "Partido DeFora", "vice": "Mateus Silva", "cargos": ["Ministro da Educação"], "idade": 777}
}


def mostrar_informacoes(num):
    candidato = candidatos.get(num)
    if candidato:
        print(f"Nome: {candidato['nome']}")
        print(f"Partido: {candidato['partido']}")
        print(f"Nome do Vice: {candidato['vice']}")
        print(f"Cargos Já Ocupados: {', '.join(candidato['cargos'])}")
        print(f"Idade: {candidato['idade']}")
    else:
        print("Candidato não encontrado!")


def main():
    try:
        numero_candidato = int(input("Digite o número do candidato para consultar suas informações (1 a 10): "))
        mostrar_informacoes(numero_candidato)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()