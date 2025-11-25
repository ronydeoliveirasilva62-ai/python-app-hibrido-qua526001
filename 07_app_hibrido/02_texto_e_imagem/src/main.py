import flet as ft


def main(page: ft.Page):
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("minha primeira aplicacao.",size=50,weight="bold"),
                alignment=ft.alignment.center,
            )
            
            ),
            ft.Container(
            ft.Image(
                src="coracao.jpg",
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("nao foi possivel carregar a imagem.")
            
        ),
        alignment=ft.alignment.center,
        expand=True
            )
    )


ft.app(main)
