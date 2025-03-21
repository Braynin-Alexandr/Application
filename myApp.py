from app_controller import AppController
import sys

app = AppController()


def main():
    mode = sys.argv[1]
    try:
        if mode == '1':
            app.create_tables()
        elif mode == '2' and len(sys.argv) == 5:
            app.add_employee(sys.argv[2], sys.argv[3], sys.argv[4])
        elif mode == '3':
            app.get_all_employees()
        elif mode == '4':
            app.add_employees()
        elif mode == '5':
            app.get_special_employees()
        else:
            print('Unknown command')
    except Exception as e:
        print(f'Something went wrong: {e}\n')
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <mode> [parameters]")
        sys.exit(1)
    main()


# python myApp.py 1
# python myApp.py 2 "Ivanov Petr Sergeevich" 2009-07-12 Male
# python myApp.py 3
# python myApp.py 4
# python myApp.py 5
