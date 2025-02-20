'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import json
import streamlit as st
import packaging

# Initialize counters
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0
if 'summaries' not in st.session_state:
    st.session_state.summaries = []

file = st.file_uploader('Upload a file:', type=['txt'])

if file:
    packages = []
    input_file = file.name
    output_file = input_file.replace(".txt", ".json")
    for line in file:
        line = line.decode("utf-8").strip()
        if line:
            parsed_package = packaging.parse_packaging(line)
            packages.append(parsed_package)
            total_units = packaging.calc_total_units(parsed_package)
            unit = packaging.get_unit(parsed_package)

    with open(output_file, "w") as file:
        json.dump(packages, file, indent=4)
    
    summary = f"{len(packages)} packages written to {output_file}"

    st.session_state.total_files += 1
    st.session_state.total_lines += len(packages)
    st.session_state.summaries.append(summary)

    for summary in st.session_state.summaries:
        st.info(summary)

    st.success(f"{st.session_state.total_files} files processed, {st.session_state.total_lines} total lines processed")