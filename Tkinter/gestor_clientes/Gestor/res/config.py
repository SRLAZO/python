import sys

DATABASE_PATH = "res/clientes.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "res/tests/clientes_test.csv"