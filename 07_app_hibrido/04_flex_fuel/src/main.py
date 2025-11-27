import flet as ft


def main(page: ft.Page):
    def calcular_combustivel(e):
        if not gasolina.value:
            gasolina.error_text = "valor da gasolina nao pode ficar vazio."
            page.update()
        else:
            gasolina.error_text = ""
            page.update()
        if not Etanol.value:
            Etanol.error_text = "valor da Etanol nao pode ficar vazio."
            page.update()
        else:
            Etanol.error_text = ""

            gasolina.value =float(gasolina.value.replace(",","."))
            Etanol.value =float(Etanol.value.replace(",","."))
            resultado = "gasolina" if Etanol.value >=gasolina.value*0.7 else "Etanol"
            dlg_modal.content.value = resultado
            gasolina.value = ""
            Etanol.value = ""

            page.open(dlg_modal)

            page.update()
        
        
    page.title = "App Flex Fuel"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    gasolina = ft.TextField(
        label="Valor da gasolina",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    Etanol = ft.TextField(
        label="Valor do Etanol",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    dlg_modal = ft.AlertDialog(
        modal = True,
        title=ft.Text("Melhor abastecer com: "),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("Ok", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )
    
    page.add(
        ft.SafeArea(
            ft.Container(
               ft.Text("Flex Fuel", size=40, weight="Bold", color="yellow"),
                alignment=ft.alignment.center,bgcolor="blue",
                padding=100
            ),
            expand=True,
        ),
        ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm":6, "md":4, "xl":2}),
                ft.Container(Etanol, col={"sm":6, "md":4, "xl":2})
                                            
                                            
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("calcular", on_click=calcular_combustivel),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
            )
            
    )


ft.app(main)
