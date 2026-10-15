#open an empty window tkinter

import tkinter.filedialog
import tkinter
import pymupdf
import os

window = tkinter.Tk()
window.title("PDF Reader")
window.geometry("800x600")

#define path

path = tkinter.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
if ( path == "" ):
    exit()

book = pymupdf.open(path)
print("Number of pages: ", book.page_count)

#define current page
current_page = 0

# on opening read that file and jump to the saved page
book_save = os.path.basename(path) + '.txt'
if os.path.exists(book_save):
    with open(book_save, 'r') as file:
        current_page = int(file.read())

#show page 1 in the window
page_1_pixmap = book[current_page].get_pixmap()
page_1_image = tkinter.PhotoImage(data=page_1_pixmap.tobytes("ppm"))
page_1_label = tkinter.Label(window, image=page_1_image)
page_1_label.pack()

#arrow keys change the page
window.bind("<Left>", lambda event: change_page(-1))
window.bind("<Right>", lambda event: change_page(+1))

#change pages
def change_page(direction):
    global current_page
    current_page += direction
    if current_page < 0:
        current_page = 0
    elif current_page >= book.page_count:
        current_page = book.page_count - 1

    # Update the displayed page
    page_1_pixmap = book[current_page].get_pixmap()
    page_1_image = tkinter.PhotoImage(data=page_1_pixmap.tobytes("ppm"))
    page_1_label.config(image=page_1_image)
    page_1_label.image = page_1_image

# save the page number to a text file when you close it
    with open(book_save, 'w') as file:
        file.write(str(current_page))
    
#window stays open
window.focus_force()
window.mainloop()