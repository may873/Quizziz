import flet as ft


def main(page: ft.Page):
    page.title=("Quizziz")
    page.bgcolor="black"

    txtR1=ft.TextField(label="ingresa el indice de tu respuesta")
    
    lblP1=ft.Text("¿Que es la tecnologia?",color="white")
    lblia=ft.Text("a)",color="white")
    lblib=ft.Text("b)",color="white")
    lblic=ft.Text("c)",color="white")

    page.add(
        ft.Column(
            controls=[
                ft.Row(controls=[lblP1], alignment="CENTER"),
                ft.Row(controls=[lblia,lblib,lblic],alignment="CENTER"),
                ft.Row(controls=[txtR1],alignment="CENTER"),
                ],alignment="CENTER")
        )


ft.app(main)
