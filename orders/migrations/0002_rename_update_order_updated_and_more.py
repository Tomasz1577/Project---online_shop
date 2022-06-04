

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='products',
            new_name='product',
        ),
    ]
