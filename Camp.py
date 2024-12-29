times = {}
historico = {}
artilheiros = {}

def cadastrar_times():
    nome = input("Digite o nome do time: ")
    if nome in times:
        print("Time já cadastrado!")
    else:
        times[nome] = {"pontos": 0, "gols_pro": 0, "gols_contra": 0, "saldo": 0 }
        print(f"Time '{nome}' cadastrado com sucesso!")

def registrar_resultados():
    rodada = int(input("Digite o número da rodada: "))
    time1 = input("Digite o nome do primeiro time: ")
    time2 = input("Digite o nome do segundo time: ")
    if time1 not in times or time2 not in times:
        print("Um ou ambos os times não foram encontrados!")
        return

    gols1 = int(input(f"Gols do {time1}: "))
    gols2 = int(input(f"Gols do {time2}: "))

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

    for _ in range(gols1):
        jogador = input(f"Digite o nome de quem marcou no {time1}: ")
        if jogador in artilheiros:
            artilheiros[jogador] += 1
        else:
            artilheiros[jogador] =1

    for _ in range(gols2):
        jogador = input(f"Digite o nome de quem marcou no {time2}: ")
        if jogador in artilheiros:
            artilheiros[jogador] += 1
        else:
            artilheiros[jogador] = 1

    if rodada not in historico:
        historico[rodada] = []
    historico[rodada].append({"time1": time1, "gols1": gols1, "time2": time2, "gols2": gols2})

    print("Resultado registrado com sucesso!")

def exibir_historico():
    rodada = int(input("Escolha a rodada: "))
    if rodada not in historico:
        print(f"Nenhum resultado registrado na rodada {rodada}.")
        return
    print(f"\nResultados da rodada {rodada}:")
    for partida in historico[rodada]:
        print(f"{partida['time1']} {partida['gols1']} x {partida['gols2']} {partida['time2']}")

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
                print(
                    "{:<15} {:<10} {:<10} {:<10} {:<10}".format(time, stats["pontos"], stats["gols_pro"], stats["gols_contra"], stats["saldo"]))
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
        if not opcao_tabela.isdigit():
            print("Opção inválida! Digite um número.")
            continue

def exibir_artilharia():
    if not artilheiros:
        print("Ainda não há artilheiros registrados.")
        return

    print("\nArtilharia:")
    print("{:<20} {:<10}".format("Jogador", "Gols"))
    print("-" * 30)

    for jogador, gols in sorted(artilheiros.items(), key=lambda x: x[1], reverse=True):
        print("{:<20} {:<10}".format(jogador, gols))

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
    empates = pontos % 3
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

while True:
    print("\n1. Cadastrar Time")
    print("2. Registrar Resultado")
    print("3. Exibir Histórico")
    print("4. Exibir Tabela")
    print("5. Exibir Artilheiros")
    print("6. Exibir Estatísticas")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_times()
    elif opcao == "2":
        registrar_resultados()
    elif opcao =="3":
        exibir_historico()
    elif opcao == "4":
        exibir_tabela()
    elif opcao == "5":
        exibir_artilharia()
    elif opcao == "6":
        estatisticas_times()
    elif opcao == "7":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida!")
    if not opcao.isdigit():
        print("Opção inválida! Digite um número.")
        continue