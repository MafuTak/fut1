import random

times = {}
artilheiros = {}
historico = {}

def cadastrar_times():
    nome = input("Digite o nome do time: ")
    if nome in times:
        print("Time já cadastrado!")
    else:
        times[nome] = {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0, "jogadores": {}}

        for i in range(1, 12):
            jogador = input(f"Digite o nome do {i}° jogador: ")
            while True:
                posicao = input(f"Digite a posição do {jogador} (ATA, MC, DEF, GOL): ").upper()
                if posicao in ['ATA', 'MC', 'DEF', 'GOL']:
                    break
                else:
                    print("Posição inválida! Escolha entre: ATA, MC, DEF, GOL.")

            times[nome]["jogadores"][jogador] = {"posicao": posicao}

        print(f"Time '{nome}' e seus jogadores cadastrados com sucesso!")

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

def registrar_resultados_auto():
    confrontos = gerar_confrontos(times)
    rodada = 1
    max_rodada = len(times) - 1
    for time1, time2 in confrontos:
        if rodada > max_rodada:
            break

        print(f"Rodada {rodada}: {time1} x {time2}")

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

        if rodada not in historico:
            historico[rodada] = []
        historico[rodada].append({"time1": time1, "gols1": gols1, "time2": time2, "gols2": gols2})

        rodada += 1
    print("Simulação Concluída!")

def registrar_artilheiros():
    artilheiros = {}

    for time, info_time in times.items():
        for jogador, info_jogador in info_time["jogadores"].items():
            gols_jogador = random.randint(0, 2)
            if jogador in artilheiros:
                artilheiros[jogador] += gols_jogador
            else:
                artilheiros[jogador] = gols_jogador

    print("Artilheiros:")
    for jogador, gols in sorted(artilheiros.items(), key=lambda x: x[1], reverse=True):
        print(f"{jogador}: {gols} gols")

while True:
    print("\n1. Cadastrar Time")
    print("2. Exibir Histórico")
    print("3. Exibir Tabela")
    print("4. Exibir Elencos")
    print("5. Exibir Estatísticas")
    print("6. Simular Jogos")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_times()
    elif opcao == "2":
        rodada = int(input("Digite o número da rodada para exibir os resultados: "))
        exibir_historico(rodada)
    elif opcao == "3":
        exibir_tabela()
    elif opcao == "4":
        exibir_elencos()
    elif opcao == "5":
        estatisticas_times()
    elif opcao == "6":
        registrar_resultados_auto()
    elif opcao == "7":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida!")
