import flet as ft
def LoginView(page, auth_controller):
    email_input= ft.TextField(
        label = "Correo electrónico",
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    pass_input= ft.TextField(
        label = "Contraseña", 
        password=True,
        can_reveal_password=True, 
        width=350,
        border_radius=10)
    
    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.Snackbar(ft.Text("Por favor, complete todos los campos."))
            page.snack_bar.open = True
            page.update()
            return
        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
    return ft.View("/",
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            appbar=ft.AppBar(title=ft.Text("Iniciar Sesión")),
            
            controls=[
                ft.Column([
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    ft.TextButton("crear cuenta", on_click=lambda _: page.go("/register")),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    tight=True,
                    spacing=20
                ),
            ])