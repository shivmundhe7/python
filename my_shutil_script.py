# it helps to delete add or move files

# Copy file
import shutil
shutil.copy("data.txt", "backup/data.txt")


# Move file
shutil.move("test.txt","archieve/test.txt")

# Delete entire folder
shutil.rmtree("old_backup")

