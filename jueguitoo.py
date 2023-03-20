import random

def run():
    
    
    def choose_option():
        options = ('piedra', 'papel', 'tijeras')
        
        user_options = input('piedra, papel o tijeras : ')
        user_options = user_options.lower()
        
        if not user_options in options:
            print('Esa opcion no es valida')
            # continue
            return None, None
        computer_option = random.choice(options)
        
        print('User option: ', user_options)
        print('computer_option: ', computer_option)
        
        return user_options, computer_option

    def check_rules(user_options, computer_option, user_wins, computer_wins):
        if user_options == computer_option:
            print('Empate')
        elif user_options == 'piedra':
            if computer_option == 'tijera':
                print('Piedra gana a tijera')
                print('Usuario ganó')
                user_wins += 1
            else:
                print('Papel gana a piedra')
                print('Computer ganó')
                computer_wins += 1
        elif user_options == 'papel':
            if computer_option == 'piedra':
                print('Papel gana a piedra')
                print('Usuario ganó')
                user_wins += 1
            else:
                print('Tijera gana a papel')
                print('Computer ganó')
                computer_wins += 1
        elif user_options == 'tijeras':
            if computer_option == 'papel':
                print('Tijera gana a papel')
                print('Usuario ganó')
                user_wins += 1
            else:
                print('Piedra gana a tijera')
                print('Computer ganó')
                computer_wins += 1
        return user_wins, computer_wins
    
    def check_winner(user_wins, computer_wins):
        if computer_wins == 2:
            print('El ganador es la computadora')
            exit()
        if user_wins == 2:
            print('El ganador es el usuario')
            exit()
    
    def run_game():
        computer_wins = 0
        user_wins = 0
        rounds = 0
                
        while True:
            print('*' * 10)
            print('ROUND', rounds)
            print('*' * 10)
        
            print('computer_wins', computer_wins)
            print('user_wins', user_wins)
        
            rounds += 1
        
            user_options, computer_option = choose_option()
            user_wins, computer_wins = check_rules(user_options, computer_option, user_wins, computer_wins)
            check_winner(user_wins, computer_wins)

    run_game()

if __name__ == '__main__':
    run()