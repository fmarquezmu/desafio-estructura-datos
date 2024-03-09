import sys

soles = float(sys.argv[1])*float(sys.argv[4])
pesos_arg = float(sys.argv[2])*float(sys.argv[4])
dolares = float(sys.argv[3])*float(sys.argv[4])
pesos_cl = float(sys.argv[4])

print(f'''
    Los {pesos_cl} equivalen a:
    {soles:.1f} Soles
    {pesos_arg:.1f} Pesos Argentinos
    {dolares:.1f} Dólares
''')