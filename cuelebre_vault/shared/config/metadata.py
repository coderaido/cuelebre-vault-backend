description = """

## 🧱 Características

- Gestión de usuarios
- Cuentas asociadas a entidades bancarias
- Registro de ingresos, gastos y transferencias
- Presupuestos por categoría
- Comparativa gasto vs presupuesto
- Subida de documentos (fotos, PDF)

## 🔐 Seguridad

- Autenticación JWT
- Soporte para login OAuth2 (GitHub, Google, etc.)
- Separación de dominios y roles (futuro)


"""

summary = (
    "Sistema moderno de gestión financiera personal y empresarial, con control de cuentas, "
    "presupuestos y transacciones"
)

license_info = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT",
}
tags_metadata = [
    {
        "name": "auth",
        "description": "🔐 Operaciones relacionadas con autenticación y gestión de usuarios (login, registro, OAuth).",
    },
    {
        "name": "accounts",
        "description": "🏦 Endpoints para gestión de cuentas bancarias por usuario.",
    },
    {
        "name": "transactions",
        "description": "💳 Registro, consulta y análisis de transacciones financieras.",
    },
    {
        "name": "budgets",
        "description": "📊 Control y comparación de presupuestos definidos por el usuario.",
    },
    {
        "name": "system",
        "description": "⚙️ Endpoints internos para salud del sistema, versión, etc.",
    },
]
