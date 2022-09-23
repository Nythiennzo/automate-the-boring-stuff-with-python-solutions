from PIL import Image, ImageDraw
import os

guests_list_file_path = r'C:\repos\python\automate_the_boring_stuff\chapter19\working_folder\guests.txt'
source_image_path = r'C:\repos\python\automate_the_boring_stuff\chapter19\working_folder\Twin_flower_Xray.jpg'
working_folder = r'C:\repos\python\automate_the_boring_stuff\chapter19\working_folder'

guests_list_file = open(guests_list_file_path)
guests = [guest.rstrip('\n') for guest in guests_list_file.readlines()]
guests_list_file.close()

image = Image.open(source_image_path)
image = image.resize((288, 360))
draw_edge = ImageDraw.Draw(image)
draw_edge.line([(0, 0), (287, 0), (287, 359), (0, 359), (0, 0)], fill='black')

for guest in guests:
    guest_card = image.copy()
    draw_text = ImageDraw.Draw(guest_card)
    draw_text.text((30, 300), guest, 'black')

    guest_card.save(working_folder + os.sep + guest + '.png')

