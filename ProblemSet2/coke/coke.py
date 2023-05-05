def main():
    sum = 0
    Amount_due = 50

    while Amount_due > sum:
        #50 - 0 = 0 continua porque es menor a amount
        print(f"Amount Due: {Amount_due - sum}")

        #pide al usario que inserte una coin lo guarda en inserted
        coin_inserted =  int(input(f"Insert Coin: ").strip())
        # si inserted es 5 o 10 o 25 suma eso a la variable sum para ir restando
        if coin_inserted == 5 or coin_inserted == 10 or coin_inserted == 25:
            # suma la suma del momento con la inserada nuevamente ya que repitio el ciclo
            sum = coin_inserted + sum
            #Sigue con el ciclo
        else:
            continue
    print(f"Change Owed: {sum - Amount_due}")


main()