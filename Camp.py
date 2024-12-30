import random

times = {
    "Bangu": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
        "Ubirajara": {"posicao": "GOL", "gols": 0},
        "Marinho": {"posicao": "DEF", "gols": 0},
        "Zózimo": {"posicao": "DEF", "gols": 0},
        "Jair Marinho": {"posicao": "DEF", "gols": 0},
        "Moça Bonita": {"posicao": "MC", "gols": 0},
        "Ocimar": {"posicao": "MC", "gols": 0},
        "Mendonça": {"posicao": "MC", "gols": 0},
        "Paulo Borges": {"posicao": "ATA", "gols": 0},
        "Décio Esteves": {"posicao": "ATA", "gols": 0},
        "Ladislau": {"posicao": "ATA", "gols": 0},
        "Ademir da Guia": {"posicao": "ATA", "gols": 0}
    }},
    "Boavista": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
        "Eduardo Allax": {"posicao": "GOL", "gols": 0},
        "Carlos Alberto": {"posicao": "DEF", "gols": 0},
        "Diguinho": {"posicao": "DEF", "gols": 0},
        "Fernando": {"posicao": "DEF", "gols": 0},
        "Michel": {"posicao": "DEF", "gols": 0},
        "Marquinhos": {"posicao": "MC", "gols": 0},
        "Celsinho": {"posicao": "MC", "gols": 0},
        "Zé Roberto": {"posicao": "MC", "gols": 0},
        "Jean": {"posicao": "MC", "gols": 0},
        "Max": {"posicao": "ATA", "gols": 0},
        "Leandrão": {"posicao": "ATA", "gols": 0}
    }},
    "Botafogo": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
        "Manga": {"posicao": "GOL", "gols": 0},
        "Nilton Santos": {"posicao": "DEF", "gols": 0},
        "Sebastião Leônidas": {"posicao": "DEF", "gols": 0},
        "Alexander Barboza": {"posicao": "DEF", "gols": 0},
        "Marlon Freitas": {"posicao": "MC", "gols": 0},
        "Zagallo": {"posicao": "MC", "gols": 0},
        "Gérson": {"posicao": "MC", "gols": 0},
        "Amarildo": {"posicao": "ATA", "gols": 0},
        "Garrincha": {"posicao": "ATA", "gols": 0},
        "Jairzinho": {"posicao": "ATA", "gols": 0},
        "Heleno de Freitas": {"posicao": "ATA", "gols": 0}
    }},
    "Flamengo": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
        "Raul": {"posicao": "GOL", "gols": 0},
        "Rondinelli": {"posicao": "DEF", "gols": 0},
        "Júnior": {"posicao": "DEF", "gols": 0},
        "Leandro": {"posicao": "DEF", "gols": 0},
        "Mozer": {"posicao": "DEF", "gols": 0},
        "Zico": {"posicao": "MC", "gols": 0},
        "Andrade": {"posicao": "MC", "gols": 0},
        "Arrascaeta": {"posicao": "MC", "gols": 0},
        "Adílio": {"posicao": "MC", "gols": 0},
        "Nunes": {"posicao": "ATA", "gols": 0},
        "Tita": {"posicao": "ATA", "gols": 0}
    }},
    "Fluminense": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
        "Castilho": {"posicao": "GOL", "gols": 0},
        "Carlos Alberto Torres": {"posicao": "DEF", "gols": 0},
        "Edinho": {"posicao": "DEF", "gols": 0},
        "Thiago Silva": {"posicao": "DEF", "gols": 0},
        "Rivelino": {"posicao": "MC", "gols": 0},
        "Didi": {"posicao": "MC", "gols": 0},
        "Assis": {"posicao": "MC", "gols": 0},
        "Washington": {"posicao": "MC", "gols": 0},
        "Fred": {"posicao": "ATA", "gols": 0},
        "Waldo": {"posicao": "ATA", "gols": 0},
        "German Cano": {"posicao": "ATA", "gols": 0}
    }},
    "Madureira": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
            "Marcelo Carné": {"posicao": "GOL", "gols": 0},
            "Henrique": {"posicao": "DEF", "gols": 0},
            "Humberto": {"posicao": "DEF", "gols": 0},
            "Valdir": {"posicao": "DEF", "gols": 0},
            "Wanderley": {"posicao": "MC", "gols": 0},
            "Claudinho": {"posicao": "MC", "gols": 0},
            "Caio": {"posicao": "MC", "gols": 0},
            "Bebeto de Freitas": {"posicao": "MC", "gols": 0},
            "Maneco": {"posicao": "ATA", "gols": 0},
            "Eraldo": {"posicao": "ATA", "gols": 0},
            "Jorge Mendonça": {"posicao": "ATA", "gols": 0}
        }},
    "Maricá": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
            "Vinícius": {"posicao": "GOL", "gols": 0},
            "Paulo Vítor": {"posicao": "DEF", "gols": 0},
            "Tiago": {"posicao": "DEF", "gols": 0},
            "Gabriel": {"posicao": "DEF", "gols": 0},
            "Wesley": {"posicao": "DEF", "gols": 0},
            "Renatinho": {"posicao": "MC", "gols": 0},
            "Nildo": {"posicao": "MC", "gols": 0},
            "Marquinhos": {"posicao": "MC", "gols": 0},
            "Silas": {"posicao": "ATA", "gols": 0},
            "Thiaguinho": {"posicao": "ATA", "gols": 0},
            "Felipe Adão": {"posicao": "ATA", "gols": 0}
        }},
    "Nova Iguaçu": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
            "Jefferson": {"posicao": "GOL", "gols": 0},
            "Bruno Costa": {"posicao": "DEF", "gols": 0},
            "Rodrigo Sam": {"posicao": "DEF", "gols": 0},
            "Wallace": {"posicao": "DEF", "gols": 0},
            "Lucas": {"posicao": "MC", "gols": 0},
            "Elias": {"posicao": "MC", "gols": 0},
            "Thiago Martins": {"posicao": "MC", "gols": 0},
            "João Pedro": {"posicao": "MC", "gols": 0},
            "Zambi": {"posicao": "ATA", "gols": 0},
            "Dellatorre": {"posicao": "ATA", "gols": 0},
            "Douglas": {"posicao": "ATA", "gols": 0}
        }},
    "Portuguesa RJ": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
            "Marcão": {"posicao": "GOL", "gols": 0},
            "Diego Guerra": {"posicao": "DEF", "gols": 0},
            "André Silva": {"posicao": "DEF", "gols": 0},
            "Rodrigo Lobão": {"posicao": "DEF", "gols": 0},
            "Luan": {"posicao": "MC", "gols": 0},
            "Romarinho": {"posicao": "MC", "gols": 0},
            "Gean": {"posicao": "MC", "gols": 0},
            "Vinícius Pacheco": {"posicao": "MC", "gols": 0},
            "Ricardinho": {"posicao": "ATA", "gols": 0},
            "Lucas Silva": {"posicao": "ATA", "gols": 0},
            "Bruninho": {"posicao": "ATA", "gols": 0}
        }},
    "Sampaio Corrêa": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
            "Luís": {"posicao": "GOL", "gols": 0},
            "Tiago Gaúcho": {"posicao": "DEF", "gols": 0},
            "Henrique Mattos": {"posicao": "DEF", "gols": 0},
            "Anderson Luiz": {"posicao": "DEF", "gols": 0},
            "Wellington": {"posicao": "DEF", "gols": 0},
            "Márcio Passos": {"posicao": "MC", "gols": 0},
            "Raul": {"posicao": "MC", "gols": 0},
            "Marcio Diogo": {"posicao": "MC", "gols": 0},
            "João Paulo": {"posicao": "MC", "gols": 0},
            "Lucão": {"posicao": "ATA", "gols": 0},
            "Marcos Assunção": {"posicao": "ATA", "gols": 0}
        }},
    "Vasco da Gama": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
            "Barbosa": {"posicao": "GOL", "gols": 0},
            "Bellini": {"posicao": "DEF", "gols": 0},
            "Mauro Galvão": {"posicao": "DEF", "gols": 0},
            "Orlando Peçanha": {"posicao": "DEF", "gols": 0},
            "Juninho Pernambucano": {"posicao": "MC", "gols": 0},
            "Ademir de Menezes": {"posicao": "MC", "gols": 0},
            "Edmundo": {"posicao": "MC", "gols": 0},
            "Roberto Dinamite": {"posicao": "MC", "gols": 0},
            "Romário": {"posicao": "ATA", "gols": 0},
            "Valdir Bigode": {"posicao": "ATA", "gols": 0},
            "Bebeto": {"posicao": "ATA", "gols": 0}
        }},
    "Volta Redonda": {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {
            "Douglas Borges": {"posicao": "GOL", "gols": 0},
            "Marcelo": {"posicao": "DEF", "gols": 0},
            "Willian": {"posicao": "DEF", "gols": 0},
            "João Victor": {"posicao": "DEF", "gols": 0},
            "Michel": {"posicao": "MC", "gols": 0},
            "Bruno Barra": {"posicao": "MC", "gols": 0},
            "Alef": {"posicao": "MC", "gols": 0},
            "Pablo": {"posicao": "MC", "gols": 0},
            "Saulo Mineiro": {"posicao": "ATA", "gols": 0},
            "Pedro Raul": {"posicao": "ATA", "gols": 0},
            "Ramon": {"posicao": "ATA", "gols": 0}
    }},
}
artilheiros = {}
historico = {}

def exibir_historico(rodada):
    if rodada in historico:
        print(f"Resultados da Rodada {rodada}:")
        for jogo in historico[rodada]:
            print(f"{jogo['time1']} {jogo['gols1']} x {jogo['gols2']} {jogo['time2']}")
    else:
        print("Rodada não encontrada!")

def exibir_tabela():
    while True:
        print("\nExibir Tabela Por:")
        print("1. Pontuação")
        print("2. Saldo de Gols")
        print("3. Gols Marcados")
        print("4. Gols Sofridos")
        print("5. Sair")
        opcao_tabela = input("Escolha uma opção: ")

        if opcao_tabela == "1":
            print("\nTabela de classificação (Pontuação):")
            print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Time", "Pontos", "Gols Pró", "Gols Contra", "Saldo"))
            tabela = sorted(times.items(), key=lambda x: (x[1]["pontos"], x[1]["saldo"], x[1]["gols_pro"]), reverse=True)
            for time, stats in tabela:
                print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(time, stats["pontos"], stats["gols_pro"], stats["gols_contra"], stats["saldo"]))
        elif opcao_tabela == "2":
            print("\nTabela de classificação (Saldo):")
            print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Time", "Pontos", "Gols Pró", "Gols Contra", "Saldo"))
            tabela = sorted(times.items(), key=lambda x: x[1]["saldo"], reverse=True)
            for time, stats in tabela:
                print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(time, stats["pontos"], stats["gols_pro"], stats["gols_contra"], stats["saldo"]))

        elif opcao_tabela == "3":
            print("\nTabela de classificação (Gols Marcados):")
            print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Time", "Pontos", "Gols Pró", "Gols Contra", "Saldo"))
            tabela = sorted(times.items(), key=lambda x: x[1]["gols_pro"], reverse=True)
            for time, stats in tabela:
                print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(time, stats["pontos"], stats["gols_pro"], stats["gols_contra"], stats["saldo"]))

        elif opcao_tabela == "4":
            print("\nTabela de classificação (Gols Sofridos):")
            print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Time", "Pontos", "Gols Pró", "Gols Contra", "Saldo"))
            tabela = sorted(times.items(), key=lambda x: x[1]['gols_contra'], reverse=True)
            for time, stats in tabela:
                print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(time, stats["pontos"], stats["gols_pro"], stats["gols_contra"], stats["saldo"]))

        elif opcao_tabela == "5":
            print("Voltando ao menu principal....")
            break
        else:
            print("Opção inválida!")

def exibir_elencos():
    time = input("Digite o nome do time para exibir o elenco: ")
    if time not in times:
        print("Time não encontrado.")
        return

    print(f"\nElenco do {time}:")
    print("{:<20} {:<10}".format("Jogador", "Posição"))
    print("-" * 30)

    for jogador, info in times[time]["jogadores"].items():
        print("{:<20} {:<10}".format(jogador, info["posicao"]))

def contar_jogos(time):
    jogos = 0
    for rodada, partidas in historico.items():
        for partida in partidas:
            if partida["time1"] == time or partida["time2"] == time:
                jogos += 1
    return jogos

def estatisticas_times():
    time = input("Digite o nome do time para exibir as estatísticas: ")
    if time not in times:
        print("Time não encontrado!")
        return

    jogos = contar_jogos(time)
    pontos = times[time]["pontos"]
    gols_pro = times[time]["gols_pro"]
    gols_contra = times[time]["gols_contra"]
    saldo = times[time]["saldo"]
    vitorias = pontos // 3
    empates = pontos % 3 // 1
    derrotas = jogos - vitorias - empates
    aproveitamento = (pontos / (jogos * 3)) * 100 if jogos > 0 else 0

    print(f"\nEstatísticas do {time}:")
    print(f"Jogos: {jogos}")
    print(f"Vitórias: {vitorias}")
    print(f"Empates: {empates}")
    print(f"Derrotas: {derrotas}")
    print(f"Gols Marcados: {gols_pro}")
    print(f"Gols Sofridos: {gols_contra}")
    print(f"Saldo de Gols: {saldo}")
    print(f"Aproveitamento: {aproveitamento:.2f}%")

def gerar_confrontos(times):
    confrontos = []
    times_list = list(times.keys())

    for i in range(len(times_list)):
        for j in range(i + 1, len(times_list)):
            confrontos.append((times_list[i], times_list[j]))

    random.shuffle(confrontos)
    return confrontos

def simular_jogo(time1, time2):
    gols1 = random.randint(0, 5)
    gols2 = random.randint(0, 5)
    return {"gols1": gols1, "gols2": gols2}

    for _ in range(gols1):
        jogador_escolhido = random.choise(
            list(times[time1]["jogadores"].keys()),
            weights=[0.8 if info["posicao"] == "ATA" else 0.5 if info["posicao"] == "MC" else 0.3 for info in times[time1]["jogadores"].vlues()],
            k=1
        )[0]
        times[time1]["jogadores"][jogador_escolhido]["gols"] += 1

        for _ in range(gols2):
            jogador_escolhido = random.choices(
                list(times[time2]["jogadores"].keys()),
                weights=[0.8 if info["posicao"] == "ATA" else 0.5 if info["posicao"] == "MC" else 0.3 for info in
                         times[time2]["jogadores"].values()],
                k=1
            )[0]
            times[time2]["jogadores"][jogador_escolhido]["gols"] += 1

        return {"gols1": gols1, "gols2": gols2}

def registrar_resultados_auto():
    confrontos = gerar_confrontos(times)
    total_rodadas = len(times) - 1
    rodada_atual = 1

    confrontos_por_rodada = len(confrontos) // total_rodadas
    for i in range(0, len(confrontos), confrontos_por_rodada):
        if rodada_atual > total_rodadas:
            break

        historico[rodada_atual] = []
        rodada_confrontos = confrontos[i:i + confrontos_por_rodada]

        for time1, time2 in rodada_confrontos:
            resultado = simular_jogo(time1, time2)
            gols1 = resultado["gols1"]
            gols2 = resultado["gols2"]

            times[time1]["gols_pro"] += gols1
            times[time1]["gols_contra"] += gols2
            times[time1]["saldo"] = times[time1]["gols_pro"] - times[time1]["gols_contra"]
            if gols1 > gols2:
                times[time1]["pontos"] += 3
            elif gols1 == gols2:
                times[time1]["pontos"] += 1

            times[time2]["gols_pro"] += gols2
            times[time2]["gols_contra"] += gols1
            times[time2]["saldo"] = times[time2]["gols_pro"] - times[time2]["gols_contra"]
            if gols2 > gols1:
                times[time2]["pontos"] += 3
            elif gols1 == gols2:
                times[time2]["pontos"] += 1

            historico[rodada_atual].append({"time1": time1, "gols1": gols1, "time2": time2, "gols2": gols2})

        rodada_atual += 1

    print("Simulação Concluída!")

def exibir_artilheiros():
    artilheiros = []

    for time, info_time in times.items():
        for jogador, info_jogador in info_time["jogadores"].items():
            artilheiros.append({"jogador": jogador, "time": time, "gols": info_jogador["gols"]})

    artilheiros = sorted(artilheiros, key=lambda x: x["gols"], reverse=True)

    print("\nArtilheiros:")
    print("-" * 30)
    for artilheiro in artilheiros:
        print(f"{artilheiro['jogador']} ({artilheiro['time']}): {artilheiro['gols']} gols")
        print("-" * 30)

while True:
    print("1. Exibir Histórico")
    print("2. Exibir Tabela")
    print("3. Exibir Elencos")
    print("4. Exibir Estatísticas")
    print("5. Simular Jogos")
    print("6. Exibir Artilheiros")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        rodada = int(input("Digite o número da rodada para exibir os resultados: "))
        exibir_historico(rodada)
    elif opcao == "2":
        exibir_tabela()
    elif opcao == "3":
        exibir_elencos()
    elif opcao == "4":
        estatisticas_times()
    elif opcao == "5":
        registrar_resultados_auto()
    elif opcao == "6":
        exibir_artilheiros()
    elif opcao == "7":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida!")
