import importlib

def main():
    project = importlib.import_module(
        '.project_' + input('What project do you want to run? '), package='projects')
    project.main()

if __name__ == '__main__':
    main()