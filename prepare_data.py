import os
from turtle import st

folder = 'maha_texts'
output_file = 'mahabharata_dataset.txt'

with open(output_file, 'w', encoding='utf-8') as out_f:
    for file in sorted(os.listdir(folder)):
        if file.endswith('.txt'):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                content = f.read()
                out_f.write(f"<|Krishna|>\n{content.strip()}\n<|endoftext|>\n\n")

print("Data preparation complete!")

    st.write(result)

    # Krishna's voice response
    speak(result)
else:
    st.info("Ask a question to receive wisdom from Krishna.")   