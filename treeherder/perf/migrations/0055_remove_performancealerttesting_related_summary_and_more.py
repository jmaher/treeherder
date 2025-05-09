# Generated by Django 5.1.2 on 2024-10-16 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("perf", "0054_performancealert_confidence_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="performancealerttesting",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="performancealerttesting",
            name="related_summary",
        ),
        migrations.RemoveField(
            model_name="performancealerttesting",
            name="summary",
        ),
        migrations.RemoveField(
            model_name="performancealerttesting",
            name="classifier",
        ),
        migrations.RemoveField(
            model_name="performancealerttesting",
            name="series_signature",
        ),
        migrations.RemoveField(
            model_name="performancealert",
            name="confidence",
        ),
        migrations.RemoveField(
            model_name="performancealert",
            name="detection_method",
        ),
        migrations.DeleteModel(
            name="PerformanceAlertSummaryTesting",
        ),
        migrations.DeleteModel(
            name="PerformanceAlertTesting",
        ),
    ]
