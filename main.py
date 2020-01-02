from application import Application
from application_manager import ApplicationManager


def main():
    manager = ApplicationManager()
    app = Application(manager)
    app.run_forever()


if __name__ == '__main__':
    main()
