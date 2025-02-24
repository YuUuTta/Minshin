# Generated by Django 3.0.8 on 2020-07-30 03:53

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rulepage',
            name='rule_text',
        ),
        migrations.AddField(
            model_name='rulepage',
            name='content',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, help_text='Add about title', max_length=100, null=True)), ('text', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about content', max_length=1000, null=True))]))], blank=True, null=True),
        ),
    ]
