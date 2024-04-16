readme_file = open("readme.txt", "r+")

# print(readme_file.read())

readme_file.write("hello")

print(readme_file.read())

readme_file.close()

readme_file.write("hello again")