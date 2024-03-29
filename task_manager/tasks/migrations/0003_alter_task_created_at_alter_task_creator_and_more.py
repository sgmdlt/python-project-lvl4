# Generated by Django 4.1.4 on 2022-12-19 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("labels", "0002_alter_label_created_at_alter_label_name"),
        ("statuses", "0002_alter_status_created_at_alter_status_name"),
        ("tasks", "0002_tasklabel_task_labels"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(auto_now=True, verbose_name="created at"),
        ),
        migrations.AlterField(
            model_name="task",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="creator",
                to=settings.AUTH_USER_MODEL,
                verbose_name="creator",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="executor",
                to=settings.AUTH_USER_MODEL,
                verbose_name="executor",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                blank=True,
                related_name="labels",
                through="tasks.TaskLabel",
                to="labels.label",
                verbose_name="labels",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.CharField(max_length=50, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="statuses.status",
                verbose_name="status",
            ),
        ),
    ]
