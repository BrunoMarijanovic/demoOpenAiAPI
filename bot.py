import tkinter as tk
import openai

openai.api_key = "YOUR_KEY"

ventana = tk.Tk()
ventana.geometry("675x350")

def responder():
    pregunta = texto.get("1.0", tk.END)

    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta)
    respuesta.config(text=completion.choices[0].text)

titulo = tk.Label(ventana, text="Escribe tu pregunta")
titulo.grid(row=0, column=0, padx=10, pady=10)

texto = tk.Text(ventana, height=5, border=5, wrap="word")
texto.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

boton = tk.Button(ventana, text="Enviar", command=responder)
boton.grid(row=2, column=0, padx=10, pady=10)

respuesta = tk.Label(ventana, text="")
respuesta.grid(row=3, column=0, padx=10, pady=10)

ventana.mainloop()
