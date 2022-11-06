import importlib

def main():
    while True:
        try:
            project = importlib.import_module(
                '.project_' + input('What project do you want to run? '), package='projects')
            project.main()
            break
        except ModuleNotFoundError:
            print("This project doesn't exist, Try again.\n")
        
if __name__ == '__main__':
    main()