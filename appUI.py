import customtkinter as ctk
from customtkinter import filedialog
from app import getLyrics

def checkEntry(*args):
    if userInputEntry.get().strip():
        userSearchButton.configure(state="normal")
    else:
        userSearchButton.configure(state="disabled")

def setOutput(text):
    outputTextbox.configure(state="normal")
    outputTextbox.delete("1.0", "end")
    outputTextbox.insert("1.0", text)
    outputTextbox.configure(state="disabled")
    saveButton.configure(state="normal")

def callAppFunc():
    query = userInputEntry.get().strip()
    if not query:
        return
    userSearchButton.configure(state="disabled")

    try:
        sourceMap = {"Genius": "genius", "LyricAdvisor": "lyricadvisor"}

        source = sourceMap.get(sourceVar.get(), "genius")
        
        lyrics = getLyrics(query, source)
        setOutput(lyrics)
    except Exception as error:
        setOutput(str(error))
    finally:
        checkEntry()

def saveToFile():
    filePath = filedialog.asksaveasfilename(
        title="Save Lyrics As...",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filePath:
        return

    text = outputTextbox.get("1.0", "end-1c")
    try:
        with open(filePath, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception as error:
        setOutput(f"Error saving file: {error}")

app = ctk.CTk()
app.geometry("600x500")
app.title("Give Me The Lyrics")

ctk.set_appearance_mode("dark")

userInputLabel = ctk.CTkLabel(app, text="Enter song query:")
userInputEntry = ctk.CTkEntry(app)
userSearchButton = ctk.CTkButton(app, text="Search", state="disabled", command=callAppFunc)

sourceVar = ctk.StringVar(value="Genius")
userSourceOptionMenu = ctk.CTkOptionMenu(app, variable=sourceVar, values=["Genius", "LyricAdvisor"])

outputTextbox = ctk.CTkTextbox(app, state="disabled", wrap="word")
saveButton = ctk.CTkButton(app, text="Save Lyrics", state="disabled", command=saveToFile)


app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure((0, 1, 2, 3), weight=1)

userInputEntry.bind("<KeyRelease>", checkEntry)

userInputLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
userInputEntry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
userSourceOptionMenu.grid(row=0, column=2, padx=6, pady=6, sticky="ew")
userSearchButton.grid(row=0, column=3, padx=5, pady=5)

saveButton.grid(row=1, column=0, columnspan=4, padx=5, pady=(0, 5), sticky="ew")
outputTextbox.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

if __name__ == '__main__':
    app.mainloop()
