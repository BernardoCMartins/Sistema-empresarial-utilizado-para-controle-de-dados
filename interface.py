import customtkinter as ctk
from PIL import Image
import main

janela = ctk.CTk()
#janela principal
janela.title("Sistema Best Shoes")
janela.geometry("900x500")
janela.resizable(width= False, height= False)
janela._set_appearance_mode("dark")
janela.configure(fg_color="#06141e")

def botao_login():
    print("login")


#frame

frame = ctk.CTkFrame(master= janela, width=285, height= 415)
frame.configure(fg_color="#1e2b34") 
frame.place(x=596, y=43)

txt_titulo = ctk.CTkLabel(janela, text="Best Shoes", font=("arial bold",48), ).pack(pady=0, padx=0)
txt_login = ctk.CTkLabel(janela, text="Login", fg_color="#1e2b34",bg_color="#1e2b34", font=("arial",24))
txt_login.place(x=612, y=106)
txt_usuario = ctk.CTkEntry(janela, width=242, bg_color="#1e2b34", placeholder_text= "Seu login")
txt_usuario.place(x=618, y=155)
txt_senha = ctk.CTkEntry(janela, width=242 ,bg_color="#1e2b34", placeholder_text= "Sua senha", show="*")
txt_senha.place(x=618, y=219)
btn_login = ctk.CTkButton(janela,width=242,text="Entrar", bg_color="#1e2b34", command=botao_login )
btn_login.place(x=618, y=295)


 

#imagem
img = ctk.CTkImage(Image.open("tenis.png"),size=(350,350),)
label_img = ctk.CTkLabel(janela, image=img, text="",)
label_img.place(x=50, y=80)



janela.mainloop()