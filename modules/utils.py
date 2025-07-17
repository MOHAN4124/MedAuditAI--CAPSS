# modules/utils.py

def save_output_to_file(text, path="outputs/result_report.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
