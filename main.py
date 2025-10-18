from matrix_func import *

def main():
    print("=== Matrix Operations ===")
    
    while True:
        print("\nAvailable operations:")
        print("1. Create and fill matrix")
        print("2. Exit")
        
        user_choice_one = input("\nSelect choic (1-2): ")
        
        if user_choice_one == "1":
            print("\n--- Creating Matrix ---")
            matrix_one = create_and_fill_matrix()
            print("\nFinal matrix:")
            print_matrix(matrix_one)

            while True:
                print('Create second matrix for operations?: ')
                user_choice_two = input('\nEnter (y/n): ')

                if user_choice_two in ['Yes', 'yes', 'y', 'Y']:
                    print("\n--- Creating Second Matrix ---")
                    matrix_two = create_and_fill_matrix()
                    print_matrix(matrix_two)

                    while True:
                        print('Matrix operations')
                        print('1. Summ matrix')
                        user_choice_op = input("\nSelect operation (1-3): ")
                        
                        if user_choice_op == "1":
                            result = matrix_sum(matrix_one, matrix_two)
                            if result is not None:
                                print_matrix(result)
                            break
                    break

                elif user_choice_two in ['no', 'n']:
                    break
                else:
                    ("Please enter 'y' or 'n' ")
            
        elif user_choice_one in ['2', 'Exit', 'ex']:
            break
            
        else:
            print("Invalid choice! Please select 1-3.")

if __name__ == "__main__":
    main()