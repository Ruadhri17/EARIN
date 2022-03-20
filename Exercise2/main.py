import genetic_algorithm
import menu_service

def main():
    menu_service.run_fx()
    print(genetic_algorithm.create_population(5, 2, 2))
    return


if __name__ == '__main__':
    main()