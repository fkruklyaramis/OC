
from views.interface_view import InterfaceView
from controllers.interface_controller import InterfaceController


def main():
    while True:
        main_view = InterfaceView
        InterfaceController(main_view).show_menu()


if __name__ == "__main__":
    main()
