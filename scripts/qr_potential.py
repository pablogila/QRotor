import os
import qrotor as qr

in_filename = 'potential_felix.dat'
in_file = os.getcwd() + '/' + in_filename
out_file = qr.logdirfile + '_potential_felix'

variables = qr.Variables()
variables.searched_E_levels = 5
variables.atom_type = 'H'
variables.B = qr.B_Hydrogen
variables = qr.file.read_potential(variables, in_file)
variables.gridsize = 200000
variables = qr.solve.interpolate_potential(variables)
variables.comment = f'Custom potential energies, converged to gridsize {variables.gridsize}'

data = qr.solve.energies(variables)

qr.file.write(data, out_file)
qr.file.compress(out_file)

# qr.plot.energies(data)

