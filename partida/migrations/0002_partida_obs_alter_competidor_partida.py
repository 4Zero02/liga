# Generated by Django 4.1 on 2023-03-20 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("partida", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="partida",
            name="obs",
            field=models.TextField(blank=True, null=True, verbose_name="Observações"),
        ),
        migrations.AlterField(
            model_name="competidor",
            name="partida",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="partida.partida",
            ),
        ),
    ]
