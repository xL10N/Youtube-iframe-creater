import random
import tkinter as tk

# generate the file name
file_name = str(random.random())[2:]
links = []
def create_html_with_youtube():
    global links
    """
    This function create the html file.
    This function need the embed version
    of the Video
    """
    global file_name
    html = f"""
                <!doctype html>
    <html>
        <head>
            <title>{file_name}</title>
            <meta charset="utf-8">
            <meta name="description"content="Startseite">
            <meta name="viewport"content="width=device-with, userscalable=yes, initinal-scale=1, maximum.scale=3">
            <meta name="author"content="xL10N_">
        </head>
        <body>
                """
    # add every video
    for i in links:
        html += f"""<iframe width="560" height="315" src="https://www.youtube.com/embed/{i}" 
                title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
                clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
             """
    # add the closing tag for html and body
    html += "</body></html>"
    # create the html file and write the html code in it
    f = open(f"{file_name}.html", "w")
    f.write(html)
    f.close()
    # close the window
    root.destroy()


def add_link():
    # add the link from the textbox intp the links list
    link = link_input.get("1.0", "end-1c")
    links.append(link)
    link_input.delete("1.0", "end")


root = tk.Tk()
#  backgroundcolor
root.configure(background='white')
# scree size
root.geometry("600x600")
label1 = tk.Label(root, text="Youtube iframe creater", font=("arial", 30, "bold"), fg="black", bg="white")
label1.pack()
# here you should past the embed link
link_input = tk.Text(root, width=100, height=20, bg="white", fg="black")
link_input.pack()
# add links button
add_button = tk.Button(root, text="Add", fg="red", width=20, height=20, font=("arial", 25, "bold"), command=add_link)
add_button.pack(side="left")
# create button
create_button = tk.Button(root, text="Create", fg="red", width=20, height=20, font=("arial", 25, "bold")
                          , command=create_html_with_youtube)
create_button.pack(side="right")
root.mainloop()







