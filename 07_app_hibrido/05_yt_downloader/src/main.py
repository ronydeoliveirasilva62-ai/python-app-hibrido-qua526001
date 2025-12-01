import flet as ft
from pytubefix import youtube

import os
import threading

def main(page: ft.Page):
    page.title = "youtube Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/youtube.png"

    caminho_videos = 'videos' 
    caminho_audios = 'audios'
    os.makedirs(caminho_videos, exist_ok=True)
    os.makedirs(caminho_audios, exist_ok=True)

    titulo = ft.text("use uma URL", color=ft.colors.BLECK,size=20,weight=ft.FontWeight.BOLD)
    url =ft.TextField(label="cole a URL do video do youtube aqui ",width=400, border_radus=10)

    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets","logo.png")
    logo_cabecalho = ft.image(src=logo_path, width=300,height=200)

    video_info = ft.Container(
        content= ft.colulumn([]),
        visible=False,
        padding=10,
        bgcolor=ft.colors.Blue_Grey_50,
        border_radius=10,
        width=400
    )

    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.colors.BLUE,
        bgcolor=ft.colors.BLUE_GREY_100
    )

    status_text = ft.text(
    "",
    color=ft.colors.BLECK,
    size=14,
    text_align=ft.TextAlign.CENTER
    )

    def mostrar_infor_videos(yt):
        try:
            #limpar o container
            video_info.conteint.controls.clear()

            #adicionar informacoes do video
            video_info.content.controls.extend([
                ft.text(f"titulo:{yt.title}",size=14,weight=ft.FontWeight.BOLD),
                ft.text(f"canal:{yt.autor}",size=12,),
                ft.text(f"duracao:{yt.lenth/60}:{yt.length%60:02d}",size=12),
                ft.text(f"visualizacoes:{yt.views:,}",size=12),

                video_info.visible = True
                page.update()

    def baixar_videos(e)
        if not url.value.strp():
           status_text.value ="por favor, insira uma URL valida."
           status_text.value = ft.colors.ORANGE
           page.update()

    def donwload_thread():
        try:
            # mostrar progresso
            progress_bar.visible = True
            status_text.value = "Analisando video..."
            status_text.color = ft colors.BLUE
            page.update()

            #cria objeto do youtube
            yt = youtube(url.value.strip())

            mostrar_info_videos(yt)

            status_text.value =f"baixando video: {yt.title}..." 
            page.update()

            stream = yt.streams.get_highest_resolution()

            #todo: fazer if else do stream

            
        ecept Exception as e:
            progress_bar.visible = False 
            status_text.value = f"Erro{str(e)}."
            srtatus_text.color = ft.colors.reversed
            page.update()

            #executa em thread separada nao travar a interface
            threading.thread(target=donwload_download,daemon=true).start()   





            ])




        except Exception as e :
            status_text.volume = f"Erro ao obter informacoes:{str(e)}."
            status_text.color = ft.colors.RED
            page.update()



    page.add(
        ft.SafeArea(
            ft.Container(
                
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
