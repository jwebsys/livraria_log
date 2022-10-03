# Generated by Django 4.1.1 on 2022-10-03 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0004_livro_autores_alter_livro_categoria_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Carrinho"),
                            (2, "Realizado"),
                            (3, "Pago"),
                            (4, "Entregue"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="compras",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
