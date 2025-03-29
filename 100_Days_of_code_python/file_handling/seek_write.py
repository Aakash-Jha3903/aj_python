# Open the file in write mode
with open("poem.txt", "w") as file:
    # Write a poem
    file.write("In the garden of spring,\n")
    file.write("Petals dance in the breeze,\n")
    file.write("Whispers of love sing,\n")
    file.write("Underneath the cherry trees.\n")
    file.write("Nature's beauty, ever free.\n")

# Open the file in read mode
with open("poem.txt", "r") as file:
    # Read the content of the file
    poem_content = file.read()
    print("Original poem:\n", poem_content)

    # Seek to the beginning of the file
    file.seek(0)

    # Read the content again after seeking
    new_poem_content = file.read()
    print("\nContent after seeking to the beginning:\n", new_poem_content)

with open("poem.txt","a") as f:
    f.write("yo")
    f.seek(0)
    f.write("i am at 0 ")




# Open the file in read mode
with open("poem.txt", "r") as file:
    # Read the content of the file
    poem_content = file.read()
    print("Original poem:\n", poem_content)

    # Seek to the beginning of the file
    file.seek(0)

    # Read the content again after seeking
    new_poem_content = file.read()
    print("\nContent after seeking to the beginning:\n", new_poem_content)
