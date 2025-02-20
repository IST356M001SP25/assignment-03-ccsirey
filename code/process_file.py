'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''

import json
import streamlit as st
import packaging

file = st.file_uploader('Upload a file:', type=['txt'])

if file:
    packages = []
    input_file = file.name
    output_file = input_file.replace(".txt", ".json")
    for line in file:
        line = line.decode("utf-8").strip()
        line = line.strip()
        if line:
            parsed_package = packaging.parse_packaging(line)
            packages.append(parsed_package)
            total_units = packaging.calc_total_units(parsed_package)
            unit = packaging.get_unit(parsed_package)
            st.info(f"{line} :arrow_right: Total :package: size {total_units} {unit}")

    with open(output_file, "w") as file:
        json.dump(packages, file, indent=4)
    st.success(f"{len(packages)} packages written to {output_file}", icon="💾")