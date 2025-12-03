import flet as ft
from pytubefix import YouTube

import os
import threading

def main(page: ft.Page):
    page.title = "Youtube Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/youtube.png"

    caminho_videos = 'videos' 
    caminho_audios = 'audios'
    os.makedirs(caminho_videos, exist_ok=True)
    os.makedirs(caminho_audios, exist_ok=True)

    titulo = ft.Text("use uma URL", color=ft.Colors.BLACK,size=20,weight=ft.FontWeight.BOLD)
    url =ft.TextField(label="cole a URL do video do YouTube aqui ",width=400, border_radius=10)

    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets","logo.png")
    logo_cabecalho = ft.image(src=logo_path, width=300,height=200)

    video_info = ft.Container(
        content= ft.Column([]),
        visible=False,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        width=400
    )

    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.Colors.BLUE,
        bgcolor=ft.Colors.BLUE_GREY_100
    )

    status_text = ft.text(
    "",
    color=ft.Colors.BLACK,
    size=14,
    text_align=ft.TextAlign.CENTER
    )

    def mostrar_info_videos(yt):
        try:
            #limpar o container
            video_info.conteint.controls.clear()

            #adicionar informacoes do video
            video_info.content.controls.extend(
                [
                ft.Text(f"titulo:{yt.title}",size=14,weight=ft.FontWeight.BOLD),
                ft.Text(f"canal:{yt.autor}",size=12,),
                ft.Text(f"duração:{yt.lenth/60}:{yt.length%60:02d}",size=12),
                ft.Text(f"visualizações:{yt.views:,}",size=12),
            ]
            )
            video_info.visible = True
            page.update()
        except Exception as e :
            status_text.volume = f"Erro ao obter informacoes:{str(e)}."
            status_text.color = ft.Colors.RED
            page.update()

    def baixar_video(e):
        if not url.value.strip():
            status_text.value= "por favor, insira uma URL valida."
            status_text.color = ft.Colors.ORANGE
            page.update()
            
            #REVIW:verificar se return e necessario nessa parte do codigo


        def download_thread():
            try:
                #mostrar progresso
                progress_bar.visible = True
                status_text.value = "analisando video..."
                status_text.color = ft.Colors.BLUE
                page.update()

                yt = YouTube(url.value.strip())

                mostrar_info_videos(yt)

                status_text.value ="Extranindo audio de {yt.title}..."
                page.update

                stream = yt.streams.get_highest_resolution()
                if stream:
                    stream.download(caminho_audios)
                
                    progress_bar.visible = False
                    status_text.value = "Download concluido com sucesso."
                    status_text.color = ft.Colors.GREEN
                    page.update()
                else:
                    progress_bar.visible = False
                    status_text.value = "nao foi possivel baixar o video."
                    status_text.color = ft.Colors.RED
                    page.update()
                
            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"erro {str(e)}."
                status_text.color = ft.Colors.RED
                page.update()

                threading.Thread(target=download_thread, daemon=True).start()

        def extrair_audio(e):
                if not url.value.strip():
                    status_text.value = "favor inserir uma URL"
                    status_text.color = ft.Colors.ORANGE
                    page.update()

                def download_thread():
                    try:
                        progress_bar.visible = True
                        status_text.value = "analisando video..."
                        status_text.color = ft.Colors.BLUE
                        page.update()

                    yt = YouTube(url.value.strip())

                    mostrar_info_videos(yt)

                    status_text.value = f"Extraindo Audio de {yt.title}..."
                    page.update()

                    stream = yt.streams.download(caminho_audios)

                base, extens = os.path.splitext()
                novo_audio = base +".mp3"
                os.rename( novo_audio)

                progress_bar.visible = False
                status_text.value = f"audio salvo como {os.path.basename(novo_audio)}"
                status_text.color = ft.Colors.GREEN
                page.update()

                else:
                progress_bar.visible = False
                status_text.value = "nao foi possivel baixar o audio."
                status_text.color = ft.Colors.RED
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
            style= ft.ButtonStyle(bgcolor= ft.Colors.BLUE, color=ft.Colors.white,elevation=3,text_style=ft.TextThemeStyle(size=18))
        )
            audio_btn =ft.ElevatedButton(
            text="baixar audio",
            width=150,
            on_click=extrair_audio,
            style= ft.ButtonStyle(bgcolor= ft.Colors.BLUE, color=ft.Colors.white,elevation=3,text_style=ft.TextThemeStyle(size=18))
        )
            clear_btn =ft.IconButton(
            on_click=limpar_campo,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREY,
                color=ft.Colors.WHITE,
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
           status_text.value = ft.Colors.ORANGE
           page.update()

    def donwload_thread():
        try:
            # mostrar progresso
            progress_bar.visible = True
            status_text.value = "Analisando video..."
            status_text.color = ft.Colors.BLUE
            page.update()

            #cria objeto do youtube
            yt = YouTube(url.value.strip())

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
                status_text.color = ft.Colors.GREEN
                page.update()
            else:
                progress_bar.visible = False
                status_text.value = "nao foi possivel baixar o video."
                status_text.color = ft.Colors.RED
                page.update()
                
        except Exception as e:
            progress_bar.visible = False 
            status_text.value = f"Erro{str(e)}."
            status_text.color = ft.Colors.reversed
            page.update()

            #executa em thread separada nao travar a interface
            threading.thread(target=donwload_download,daemon=True).start()  

        def extrair_audio(e):
        if not url.value.strip()
        status_text.value = "favor inserir uma URL"
        status_text.color = ft.Colors.ORAGE
        page.update()

        def download_thread():

        try:
            pass
        except Exception as e:
                

        ]


            page.add(
            ft.colomn(
            [logo_cabecalho,linha_url,
             ft.dividir(height=0, color=ft.colors.TRANSPARENT),
             video_info, botoes,
             ft.divider(height=10,color=ft.Colors.TRANSPARENT),
             progress_bar, status_text
             ],
        )
            spacinng=15
            alignment=ft.crossaxisalignment.CENTER,
            horizontal_alignment=ft.crossaxisagnment.CENTER,
            scrll=ft.scrollmode.Auto 
        
    )


ft.app(main)
