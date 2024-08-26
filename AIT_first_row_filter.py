def extract_first_rows(input_filename, output_filename):
    # Dictionary to store the first occurrence of each Particle ID
    first_occurrences = {}
    
    # Open the input file and read it line by line
    with open(input_filename, 'r') as infile:
        for line in infile:
            # Split the line into columns
            columns = line.strip().split()
            # Extract the Particle ID
            particle_id = columns[0]
            
            # If this Particle ID has not been seen before, store the line
            if particle_id not in first_occurrences:
                first_occurrences[particle_id] = line.strip()
    
    # Write the first occurrences to the output file
    with open(output_filename, 'w') as outfile:
        for line in first_occurrences.values():
            outfile.write(line + '\n')

# Specify the input and output file names
input_filename = 'Moon_surface_neutron_voxel_without_H_1_6.dat'
output_filename = 'Voxel_without_H_1_6.dat'

# Call the function to perform the extraction and writing
extract_first_rows(input_filename, output_filename)
