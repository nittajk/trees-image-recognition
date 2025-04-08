import os
import mimetypes

""" 
sijoita tämä samaan kansioon, jossa kuvat on. esim. ei trees kansioon, vaan koivu kansioon
vaihda filen paikkaa sen mukaan, minkä kansion kuvat haluat uudelleen nimetä > vaihda base_name (see below)
""" 

def rename_files_in_folder(folder_path: str = ".", base_name: str = "image"):
    folder_path = os.path.abspath(folder_path)
    print(f"Working directory: {folder_path}")

    all_files = os.listdir(folder_path)
    print(f"All files in folder: {all_files}")
    image_files = [f for f in all_files if mimetypes.guess_type(f)[0] and "image" in mimetypes.guess_type(f)[0]]
    print(f"Image files found to rename: {image_files}")

    image_files.sort()

    if not image_files:
        print("No image files found to rename.")
        return

    for index, file in enumerate(image_files, start=1):
        file_extension = os.path.splitext(file)[1].lower()

        new_filename = f"{base_name}_{str(index).zfill(3)}{file_extension}"
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_filename)

        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} -> {new_file_path}")
        
    print(f"Renamed {len(image_files)} files successfully.")

script_folder = os.path.dirname(os.path.abspath(__file__))

 # TODO: vaihda base_name!!!! tämä määrittää file nimen 
rename_files_in_folder(folder_path=script_folder, base_name="testkataja") #
