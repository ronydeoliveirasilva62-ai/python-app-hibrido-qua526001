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
            ]
            )
            video_info.visible = True
            page.update()
        except Exception as e :
            status_text.volume = f"Erro ao obter informacoes:{str(e)}."
            status_text.color = ft.colors.RED
            page.update()

    def download_thread():
        try:
            progress_bar.visible =True
            status_text.value = "analisando video..."
            status_text.color = ft.colors.BLUE
            page.update()

            yt = youtube(url.value.strip())

            mostrar_info_videos(yt)

            status_text.value ="Extranindo audio de {yt.title}..."
            page.update
            stream =yt.streams.filter(only_audio=True).first()
            if stream:
                audio_file = stream.download(caminho_audios)

                base, extens = os.path.splitext(audio_file)
                novo_audio = base +".mp3"
                os.rename(audio_file, novo_audio)

                progress_bar.visible = False
                status_text.value = f"audio salvo como {os.path.basename(novo_audio)}"
                status_text.color = ft.colors.GREEN
                page.update()

            else:
                progress_bar.visible = False
                status_text.value = "nao foi possivel baixar o audio."
                status_text.color = ft.colors.RED
                page.update()

            threading.Thread(target=download_thread,oemon=True).start()
    def limpar_campo(e):
        url.value =""
        video_info.visible = False
        progress_bar.visible = False
        status_text.value =""
        page.update()

        video_btn =ft.ElevatedButton(
            text="baixar video",
            width=150,
            on_click=baixar_video,
            style= ft.ButtonStyle(bgcolor= ft.colors.BLUE, color=ft.colors.white,elevation=3,text_style=ft.TextThemeStyle(size=18))
        )
        audio_btn =ft.ElevatedButton(
            text="baixar audio",
            width=150,
            on_click=extrair_audio,
            style= ft.ButtonStyle(bgcolor= ft.colors.BLUE, color=ft.colors.white,elevation=3,text_style=ft.TextThemeStyle(size=18))
        )
        clear_btn =ft.IconButton(
            on_click=limpar_campo,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREY,
                color=ft.colors.WHITE,
                elevation=1

                
            )
        )
    linha_url =ft.Row([url,clear_btn],
                      spacing=10,
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.CENTER)
    
    botoes=ft.Row([video_btn,audio_btn],
                      spacing=15,
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.CENTER)
    
    



    def baixar_videos(e):
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

            if stream:
                stream.download(caminho_videos)
                #sucesso
                progress_bar.visible =False
                status_text.value = "download concluido com sucesso."
                status_text.color = ft.colors.GREEN
                page.update()
            else:
                progress_bar.visible = False
                status_text.value = "nao foi possivel baixar o video."
                status_text.color = ft.colors.RED
                page.update()
                
        except Exception as e:
            progress_bar.visible = False 
            status_text.value = f"Erro{str(e)}."
            status_text.color = ft.colors.reversed
            page.update()

            #executa em thread separada nao travar a interface
            threading.thread(target=donwload_download,daemon=true).start()  

    def extrair_audio(e):
        if not url.value.strip()
        status_text.value = !"favor inserir uma URL"
        status_text.color = ft.colors.ORAGE
        page.update()

        def download_thread():
        try:
            pass
        except Exception as e:
                 





            ])







    page.add(
        ft.SafeArea(
            ft.Container(
                
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
