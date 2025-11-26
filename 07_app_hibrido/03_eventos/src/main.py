import flet as ft


def main(page: ft.Page):
    # funcao do evento
    def exibir_nome(e):
        nome_saida.value = nome.value
        nome_saida.update()

    page.title = "App de manipulacao de eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # declaracao de variaveis
    nome= ft.TextField(label="informe seu nome", on_submit=exibir_nome)
    nome_saida = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com eventos", size=35, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        nome,
        ft.ElevatedButton("Enviar", on_click=exibir_nome),
        nome_saida
    )


ft.app(main)
