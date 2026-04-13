import flet as ft
def DashboardView(page, tarea_controller):
    user= page.session.get("user")
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_tareas(user["id"]):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t["titulo"], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            trailing=ft.Badge(content=ft.Text(t["estado"]),bgcolor=ft.colors.ORANGE_300)
                        ), padding=10
                )
            )
        )
    page.update()