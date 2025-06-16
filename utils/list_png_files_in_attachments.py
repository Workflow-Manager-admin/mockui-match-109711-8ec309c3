import os

def list_png_files(directory):
    png_files = []
    if os.path.exists(directory):
        for fname in os.listdir(directory):
            if fname.lower().endswith('.png') and os.path.isfile(os.path.join(directory, fname)):
                png_files.append(fname)
    return png_files

if __name__ == "__main__":
    directory = "/home/kavia/workspace/code-generation/attachments"
    png_files = list_png_files(directory)
    print("Available .png files in /home/kavia/workspace/code-generation/attachments:")
    for f in png_files:
        print(f)
