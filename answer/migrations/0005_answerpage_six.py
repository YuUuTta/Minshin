# Generated by Django 3.0 on 2020-12-08 03:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0004_auto_20201101_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerpage',
            name='six',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True))])), ('full_richtext', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.RichTextBlock()), ('links', wagtail.core.blocks.CharBlock(blank=True, help_text='Add about title', max_length=100, null=True))]))], blank=True, null=True),
        ),
    ]
