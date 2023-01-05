# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
#
# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.


# match extension:
#     case ".gif":
#         print ("image/gif")
#     case ".jpg":
#         print ("image/jpg")
#     case ".jpeg":
#         print ("image/jpeg")
#     case ".png":
#         print ("image/png")
#     case ".pdf":
#         print("document/pdf")
#     case ".txt":
#         print("document/txt")
#     case _:
#         print("application/octet-stream")

# import os
#
# # List of media types and their corresponding file suffixes
# media_types = {
#     'image': ['.gif', '.jpg', '.jpeg', '.png'],
#     'pdf': ['.pdf'],
#     'text': ['.txt'],
#     'zip': ['.zip']
# }
#
# def get_media_type(filename):
#     # Get the file extension from the filename
#     _, file_extension = os.path.splitext(filename)
#     file_extension = file_extension.lower()  # Make the extension lowercase
#
#     # Iterate through the media types and check if the file extension matches any of the suffixes
#     for media_type, suffixes in media_types.items():
#         if file_extension in suffixes:
#             return media_type
#
#     # If no media type is found, return "application/octet-stream"
#     return "application/octet-stream"
#
# # Prompt the user for a filename
# filename = input("Enter the name of a file: ")
#
# # Get the media type of the file
# media_type = get_media_type(filename)
#
# # Output the media type
# print(f"The media type of the file is: {media_type}")

import os.path
extension = input("extension? ")
extension = os.path.splitext(extension)[1].lower().lstrip().rstrip()

extension = extension.lstrip()
if extension == ".gif":
        print("image/gif")
elif extension == ".jpg":
        print("image/jpeg")
elif extension == ".jpeg":
        print("image/jpeg")
elif extension == ".png":
        print("image/png")
elif extension == ".pdf":
        print("application/pdf")
elif extension == ".txt":
        print("text/plain")
elif extension == ".zip":
        print("application/zip")
else:
        print("application/octet-stream")
